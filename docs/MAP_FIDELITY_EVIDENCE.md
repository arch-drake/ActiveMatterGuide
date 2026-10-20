# Map Fidelity & Marker Reconciliation — Evidence Gate

**Status (20 October 2026): evidence collection required. The existing 14 illustrated maps are not accurately surveyed game maps.**

## Non-negotiable release acceptance

Each map's geography (roads, footprints, shorelines, landmarks) must align to user-supplied in-game screenshots or imagery with documented reuse rights. Verify screenshot **game build, raid variant, orientation, map crop, and native aspect ratio**. For every source coordinate dataset, derive an explicit pixel-to-map transform and record fit residuals against at least three non-collinear visible control landmarks; ideally use 5–8 dispersed anchors. If source positions use a different map crop, reproject explicitly rather than overlay by eye.

**Isometric height rule:** a 2D perspective transform is not 3D geometry. Render height only if building floor count, roof height or scale is supported by screenshots or other reliable measurements. Mark missing heights as *unknown / not modelled*, not guessed. For interiors, multi-level maps need distinct floor plans and floor-aware pins.

**Marker icon rule:** preserve source layer/category, icon reference image, variant, category mapping, label, position, evidence URL/date and status. Claim an icon is game-exact only after visually comparing the original in-game UI icon. The current codes (E/T/K/D/Q/P/A/M/C/L/S) are **guide symbols**, not replicas of game icons. Dynamic extraction and other random markers must be distinguished from static landmarks.

## Required source capture per named raid map

- One full **in-game map-interface screenshot** at native resolution with compass/orientation visible, without panning and with patch version recorded.
- Close-up screenshots for hard-to-read regions, including building outlines, roads, rivers and extraction labels.
- One **in-game icon/legend capture** showing each exact marker type. If the appearance differs by raid mode or quest state, capture all variants.
- For real 3D building heights: several oblique ground-level images from documented directions, or other permissioned height evidence. An ordinary top-down map cannot establish building height.
- Permission/provenance record for each image and marker pack. Source URL and capture date in a manifest.

## Coverage ledger

| Map | Current geography | Coordinate evidence | Game screenshot | Height evidence | Icon reconciliation |
|---|---|---|---|---|---|
| Airport | Concept art | Community sample | Needed | Needed | Needed |
| Cargo Port | Concept art | Community sample | Needed | Needed | Needed |
| Dam | Concept art | Community sample | Needed | Needed | Needed |
| Dogorsk | Concept art | Community sample | Needed | Needed | Needed |
| Downtown | Concept art | Community sample | Needed | Needed | Needed |
| Factory | Concept art | Community sample | Needed | Needed | Needed |
| Headquarters | Concept art | Community sample | Needed | Needed | Needed |
| Military Base | Concept art | Community sample | Needed | Needed | Needed |
| Ozernoe | Concept art | Community sample | Needed | Needed | Needed |
| Park | Concept art | Community sample | Needed | Needed | Needed |
| Scrapyard | Concept art | Community sample | Needed | Needed | Needed |
| Shegolskoe | Concept art | Community sample | Needed | Needed | Needed |
| Gigastructure | Concept art | **No verified dataset** | Needed | Needed | Needed |
| Dalniy Island | Regional conceptual view | **No verified local dataset** | Needed | Needed | Needed |

## Source leads (not blanket reuse licenses)

- Official update notes: https://activematter.game/en/news (changes to extracted locations and cover can invalidate older coordinates)
- Active Matter Wiki: https://activematter.wiki.gg/
- Portal Atlas data/provenance: https://github.com/rileyedward/portal-atlas/blob/main/docs/data-import.md (its own README identifies Active Matter Help's map records as © Active Matter Help; do not scrape and republish without permission)
- Community map sources may be useful for verification *only*; they are not automatically redistribution-cleared.

## Lasagna-style implementation phases

1. **Source ingestion:** immutable per-image and per-marker provenance with checksum, rights and version.
2. **Coordinate calibration:** map-specific transform and anchor-fitting tests, separate from artwork.
3. **Geometry:** building footprints, validated heights/floors and roads under a versioned schema.
4. **Renderer:** flat game-reference view first; optional true height-aware isometric projection, rotation/pan/zoom second.
5. **Pin UI:** icon sprite sheet, categories, visibility, floor filtering, selected pin, dynamic marker warnings.
6. **Regression tests:** marker click targets through all transforms, zoom/rotation/resize/mobile, storage preservation, provenance flags and screenshot comparisons.

**Never promote a map to “game-faithful” without corresponding screenshots and verification.**
