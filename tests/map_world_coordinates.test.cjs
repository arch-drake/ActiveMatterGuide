/* Derived world-coordinate source-crosswalk test; no browser/network or game inspection.
 * node tests/map_world_coordinates.test.cjs */
'use strict';
const assert=require('node:assert/strict');
const fs=require('node:fs'),path=require('node:path');
const root=path.join(__dirname,'..');
const raw=fs.readFileSync(path.join(root,'map-evidence','world_coordinate_crosswalk_2026_10_20.json'),'utf8');
const x=JSON.parse(raw),html=fs.readFileSync(path.join(root,'tools','map_reference_atlas.html'),'utf8');
assert.equal(x.format,'am-world-coordinate-source-crosswalk-v1');
assert.equal(x.maps.length,12);
assert.equal(x.summary.legacyCandidates,275);
assert.equal(x.summary.sourceCoordinateMatches,201);
assert.equal(x.summary.notSourceMatched,74);
const unique=new Set(x.maps.map(m=>m.id));assert.equal(unique.size,12);
let direct=0,unmatched=0;
for(const map of x.maps){
 direct+=map.sourceMatchedCount;unmatched+=map.sourceUnmatchedCount;
 assert.equal(map.sourceMatchedCount+map.sourceUnmatchedCount,map.oldGuideSampleCount);
 assert(map.fitSampleCount>=7&&map.independentCheckCount>=2);
 assert(map.holdoutRmsHorizontalMeters<0.08,'Check residual inflated: '+map.id);
 assert(map.trainRmsHorizontalMeters<0.08,'Train residual inflated: '+map.id);
 assert(map.sourceBlobSha.length===40,'Missing source provenance hash');
 assert(map.coordinates.worldX.slopeMetersPerPercent>0);
 assert(map.coordinates.worldZ.slopeMetersPerPercent<0);
 assert.equal(map.unmatchedSourceMarkerIds.length,map.sourceUnmatchedCount);
}
assert.equal(direct,201);assert.equal(unmatched,74);
const js=html.slice(html.indexOf('<script>')+8,html.lastIndexOf('</script>'));
new Function(js);
const s=js.indexOf('const WORLD_CALIBRATIONS='),e=js.indexOf('const MOVABLE=',s);
assert(s>=0&&e>s,'Viewer embed must contain source crosswalk');
const view=new Function(js.slice(s,e)+';return WORLD_CALIBRATIONS;')();
assert.equal(view.length,12);
for(const m of x.maps){
 const v=view.find(a=>a.id===m.id);assert(v,'Viewer missing '+m.id);
 assert.equal(v.worldX.slopeMetersPerPercent,m.coordinates.worldX.slopeMetersPerPercent);
 assert.equal(v.worldZ.interceptMeters,m.coordinates.worldZ.interceptMeters);
 const pct={x:32.5,y:75.25};
 const worldX=v.worldX.slopeMetersPerPercent*pct.x+v.worldX.interceptMeters;
 const worldZ=v.worldZ.slopeMetersPerPercent*pct.y+v.worldZ.interceptMeters;
 const backX=(worldX-v.worldX.interceptMeters)/v.worldX.slopeMetersPerPercent;
 const backY=(worldZ-v.worldZ.interceptMeters)/v.worldZ.slopeMetersPerPercent;
 assert(Math.abs(backX-pct.x)<1e-9);
 assert(Math.abs(backY-pct.y)<1e-9);
}

const details=JSON.parse(fs.readFileSync(path.join(root,'map-evidence','legacy_marker_world_estimates_v1.json'),'utf8'));
assert.equal(details.totals.records,275);assert.equal(details.totals.sourceDirectMatches,201);assert.equal(details.totals.affineOnlyEstimates,74);
assert.equal(details.totals.independentlyGameVerified,0);
assert.equal(details.records.length,275);
assert.equal(new Set(details.records.map(r=>r.legacyMarkerId)).size,275);
for(const p of details.records){
 const m=x.maps.find(r=>r.id===p.mapId);assert(m,'Unknown map '+p.mapId);
 const estimatedX=Math.round((m.coordinates.worldX.slopeMetersPerPercent*p.originalMapXPercent+m.coordinates.worldX.interceptMeters)*100)/100;
 const estimatedZ=Math.round((m.coordinates.worldZ.slopeMetersPerPercent*p.originalMapYPercent+m.coordinates.worldZ.interceptMeters)*100)/100;
 assert(Math.abs(estimatedX-p.inferredGameWorldX)<.011);
 assert(Math.abs(estimatedZ-p.inferredGameWorldZ)<.011);
 assert.equal(p.correlationType,m.unmatchedSourceMarkerIds.includes(p.legacyMarkerId)?'TRANSFORM_ONLY_NO_DIRECT_SOURCE_RECORD':'MATCHED_SHARED_SOURCE_RECORD');
}
assert(html.includes('id="exportWorldCsv"'),'Reference Atlas CSV export button missing');
assert(html.includes('function exportWorldCsv()'),'Source estimate export function missing');
console.log('PASS world coordinate crosswalk: 201 direct source matches, 74 without direct match, 12 independently held-out maps, exact inverse round-trips');
