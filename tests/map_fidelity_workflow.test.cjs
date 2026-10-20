/* Regression suite: evidence registry, two-image landmark calibration and import hardening.
 * node tests/map_fidelity_workflow.test.cjs
 * No game assets, internet or personal files required.
 */
'use strict';
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const root=path.join(__dirname,'..');
const file=path.join(root,'tools','map_reconciliation.html');
const html=fs.readFileSync(file,'utf8');
const board=fs.readFileSync(path.join(root,'tools','map_fidelity_dashboard.html'),'utf8');
assert(board.includes('No game-exact basemaps certified'),'Board must not claim basemap verification');
assert(board.includes('map_reconciliation.html?map='),'Board must link to map-specific workbench');
const data=JSON.parse(fs.readFileSync(path.join(root,'map-evidence','map_fidelity_register.v1.json'),'utf8'));
const between=(a,b)=>{const x=html.indexOf(a),y=html.indexOf(b,x);assert(x>=0&&y>x,`Missing source fragment: ${a}`);return html.slice(x,y)};
const js=between('<script>','</script>').replace('<script>','');
new Function(js); // JS syntax verification, not browser interactive proof.
const maps=data.maps;
assert.equal(maps.length,14);
assert.equal(new Set(maps.map(x=>x.id)).size,14);
assert.equal(maps.reduce((n,x)=>n+x.legacyMarkerSampleCount,0),275);
assert.equal(maps.filter(x=>x.legacyMarkerSampleCount===0).length,2);
assert(maps.every(x=>x.basemapStatus==='illustration'&&!x.geometryVerified&&x.markerCountCurrentScreenshotVerified===0));
for(const id of ['referencefile','referenceImage','referenceCanvas','landmarkName','startLandmark','sameLegacyCrop','asCheck','canvas']){
 assert(html.includes('id="'+id+'"'),`Missing control ${id}`);
}
assert(html.includes("!anchors.some(a=>a.manual===true)||e.sameLegacyCrop===true"),'Legacy marker crop guard');
const g=new Function(between('function linearSolve(','function refreshOptions(')+';return {evaluateAlignment,project};')();
const controls=[
 {id:'manual-1-0',manual:true,code:'F',label:'north roof',x:7,y:5,u:11.5,v:11.25,role:'fit'},
 {id:'manual-2-1',manual:true,code:'F',label:'east runway',x:92,y:12,u:92.55,v:25.9,role:'fit'},
 {id:'manual-3-2',manual:true,code:'F',label:'south hangar',x:16,y:90,u:26,v:84.6,role:'fit'},
 {id:'manual-4-3',manual:true,code:'F',label:'west jetway',x:82,y:88,u:91.3,v:86.4,role:'fit'},
 {id:'manual-5-4',manual:true,code:'F',label:'holdout 1',x:39,y:59,u:45.05,v:58.15,role:'check'},
 {id:'manual-6-5',manual:true,code:'F',label:'holdout 2',x:60,y:23,u:61.9,v:36.95,role:'check'},
];
// Synthetic affine map: u=.95*x+.05*y+4.6; v=.12*x+.85*y+6.2
for(const p of controls){p.u=.95*p.x+.05*p.y+4.6;p.v=.12*p.x+.85*p.y+6.2}
const good=g.evaluateAlignment(controls);
assert(good.candidate&&good.candidate.rms<1e-7&&good.checkRms<1e-7);
const shifted=controls.map(x=>({...x}));shifted[5].u+=8;
assert(g.evaluateAlignment(shifted).checkRms>5,'Moved holdout must trip discrepancy');
assert.equal(g.evaluateAlignment(controls.slice(0,2)).candidate,null);
const fn=new Function('MARKERS','ALL_MAPS','state','save','$','updateMap','input',
 between('function importEvidence(data){','function downloadJSON(')+';return importEvidence(input);');
let active='';const state={},save=()=>{},updateMap=()=>{};
const dollar=s=>({set value(v){active=v}});
const blank={format:'am-map-evidence-v1',map:'airport',anchors:[],heights:[],rights:'personal',mode:'Isolated PvE'};
fn({airport:[{id:'old',x:10,y:15}]},['airport'],state,save,dollar,updateMap,{...blank,anchors:[controls[0]]});
assert.equal(state.airport.anchors[0].manual,true);
const reject=(candidate)=>assert.throws(()=>fn({airport:[{id:'old',x:10,y:15}]},['airport'],state,save,dollar,updateMap,candidate));
reject({...blank,anchors:[{...controls[0],x:101}]});
reject({...blank,anchors:[{...controls[0],label:'   '}]});
reject({...blank,anchors:[controls[0],controls[0]]});
reject({...blank,anchors:[{id:'old',x:100,y:15,u:20,v:20}]});
reject({...blank,anchors:[{id:'spoof',x:1,y:1,u:2,v:2}]});
const review={status:'observed',evidence:'Current game screenshot from build 0.4.0.192',build:'0.4.0.192',mode:'Isolated PvE',recordedAt:'2026-10-20'};
fn({airport:[{id:'old',x:10,y:15}]},['airport'],state,save,dollar,updateMap,{...blank,reviews:{old:review}});
assert.equal(state.airport.reviews.old.status,'observed');
assert.equal(state.airport.reviews.old.kind,'user-report');
reject({...blank,reviews:{nonexistent:review}});
reject({...blank,reviews:{old:{...review,status:'verified-official'}}});
reject({...blank,anchors:[{...controls[0],id:'manual-danger" onclick="alert(1)'}]});
console.log('PASS: syntax, 14-map manifest/275 markers, landmark controls, crop guard, 4 FIT/2 CHECK, displaced holdout, review classification and import validation');
