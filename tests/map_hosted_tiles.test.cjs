/* Runtime-safe tile source audit; no requests to external imagery are made. */
'use strict';
const assert=require('node:assert/strict');
const fs=require('node:fs'),path=require('node:path');
const root=path.join(__dirname,'..');
const raw=JSON.parse(fs.readFileSync(path.join(root,'map-evidence','hosted_game_raster_tile_sources.v1.json'),'utf8'));
const html=fs.readFileSync(path.join(root,'tools','map_reference_atlas.html'),'utf8');
assert.equal(raw.maps.length,14);
assert.equal(raw.maps.filter(x=>x.mode==='live-regional-raster-preview').length,13);
assert.equal(raw.maps.filter(x=>x.mode==='local-floor-reference-required').length,1);
assert.equal(raw.maps.find(x=>x.id==='gigastructure').sourceTile,null);
assert(raw.maps.every(x=>x.raidBoundaryCertified===false&&!x.markerGeoReferenced));
assert(raw.rightsPolicy.includes('not bundled'));
const code=html.slice(html.indexOf('<script>')+8,html.lastIndexOf('</script>'));
new Function(code);
assert(html.includes('id="useOnlineTiles"'),'Missing source tile activation control');
assert(html.includes('id="stopOnlineTiles"'),'Missing source tile cancellation');
assert(html.includes('id="tileLayer"'),'Missing tile host');
assert(code.includes('if(onlineMode||!'), 'Live source tiles must never display legacy markers');
assert(code.includes("if(onlineEnabled)showTiles()"),'Map switching should refresh opted-in source');
const st=code.indexOf('const TILE_ANCHORS='),en=code.indexOf('const TILE_HOST=',st);
const anchors=new Function(code.slice(st,en)+';return TILE_ANCHORS;')();
assert.equal(Object.keys(anchors).length,13);
const valid=new Set(['dalniy_tiles','forsaken_africa_tiles','america_abandoned_tiles']);
const ids=new Set(raw.maps.map(x=>x.id));assert.equal(ids.size,14);
for(const m of raw.maps){
 const a=m.sourceTile;
 if(!a)continue;
 assert.deepEqual(anchors[m.id],a);
 assert(valid.has(a.tiles));
 assert(Number.isInteger(a.z)&&a.z>=3&&a.z<=4);
 const length=2**a.z;
 assert(a.x>=0&&a.x<length&&a.y>=0&&a.y<length);
 assert(a.source.length>10);
}
assert.equal(raw.maps.filter(x=>x.sourceTile?.tiles==='dalniy_tiles').length,10);
assert.equal(raw.maps.filter(x=>x.sourceTile?.tiles==='forsaken_africa_tiles').length,2);
assert.equal(raw.maps.filter(x=>x.sourceTile?.tiles==='america_abandoned_tiles').length,1);
console.log('PASS live-source tile manifests: 13 geo-raster map views, 14 entries, 3 region servers, opt-in controls and disabled uncalibrated pins');
