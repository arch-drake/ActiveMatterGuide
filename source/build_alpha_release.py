#!/usr/bin/env python3
"""Produce an extractable alpha bundle from verified repository files; no third-party map tiles."""
import hashlib
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
ROOT=Path(__file__).resolve().parents[1]
TAG="v2.2.0-alpha.1"
STEM="ActiveMatter-SourceAtlas-"+TAG
FILES=["index.html","README.md","README_START_HERE.md","RIGHTS_AND_ATTRIBUTION.md",
       "manifest.json","active_matter_solo_pve_field_guide.html",
       "downloads/Active_Matter_Field_Operations_2_1_1_Community_Edition.zip"]
DIRS=["docs","tools","assets/maps","assets/music","map-evidence","previews","tests"]
ALLOWED={".html",".md",".json",".webp",".mp3",".png",".jpg",".svg",".zip",".cjs"}
def main():
    selected=[ROOT / rel for rel in FILES]
    for name in DIRS:
        selected.extend(p for p in (ROOT / name).rglob("*") if p.is_file() and p.suffix.lower() in ALLOWED)
    if any(not p.is_file() for p in selected):
        raise SystemExit("Missing required alpha release file")
    dist=ROOT/"dist"
    dist.mkdir(exist_ok=True)
    target=dist/(STEM+".zip")
    with ZipFile(target,"w",ZIP_DEFLATED,compresslevel=6) as archive:
        for f in sorted(set(selected)):
            archive.write(f,f.relative_to(ROOT).as_posix())
        archive.writestr("ALPHA_START_HERE.txt",
            "Active Matter Source Atlas "+TAG+"\n"
            "Extract the complete ZIP, open index.html, choose Explore Source Atlas.\n"
            "Online community map tiles need internet and explicit user opt-in.\n"
            "The legacy 2.1.1 companion has older illustrated maps and unverified pins.\n"
            "Gigastructure is a local floor-reference-only workspace.\n"
            "See docs/ALPHA_RELEASE_NOTES.md for limitations and feedback.\n")
        archive.writestr("ALPHA_BUILD_INFO.json",json.dumps({
            "tag":TAG,"rasterReferences":13,"floorOnly":["gigastructure"],
            "primaryHistoricPinOverlays":0,"thirdPartyTilesBundled":False,
            "legacyOfflineCompanion":"2.1.1"},indent=2)+"\n")
    with ZipFile(target) as archive:
        assert archive.testzip() is None
        assert "tools/all_maps_live_reference.html" in archive.namelist()
    digest=hashlib.sha256(target.read_bytes()).hexdigest()
    (dist/(STEM+".sha256")).write_text(digest+"  "+target.name+"\n",encoding="utf-8")
    print("Built",target.name,"bytes",target.stat().st_size,"sha256",digest)
if __name__=="__main__":
    main()
