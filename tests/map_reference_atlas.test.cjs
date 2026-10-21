/* Self-contained map-reference atlas checks. Run with node tests/map_reference_atlas.test.cjs
 * Offline fixture verification; not a substitute for browser/manual map inspection. */
'use strict';
const assert=require('node:assert/strict');
const fs=require('node:fs'),path=require('node:path');
const root=path.join(__dirname,'..');
const html=fs.readFileSync(path.join(root,'tools','map_reference_atlas.html'),'utf8');
const code=html.slice(html.indexOf('<script>')+8,html.lastIndexOf('</script>'));
assert(code.length>30000&&html.includes('id="viewport"')&&html.includes('id="imageFile"')&&html.includes('id="evidenceFile"'));
new Function(code);
const first=code.indexOf('const SOURCES='),next=code.indexOf('const $=',first);
assert(first>=0&&next>first);
const table=new Function(code.slice(first,next)+';return {SOURCES,MARKERS};')();
const {SOURCES,MARKERS}=table;
assert.equal(SOURCES.length,14);
assert.equal(SOURCES.filter(m=>m.kind==='regional_overview').length,1);
assert.equal(SOURCES.reduce((n,m)=>n+(m.kind==='regional_overview'?0:m.variants.length),0),30);
assert.equal(Object.values(MARKERS).reduce((n,a)=>n+a.length,0),275);
assert.equal(SOURCES.find(m=>m.id==='headquarters').region,'Africa');
assert.equal(SOURCES.find(m=>m.id==='airport').region,'Africa');
for(const v of SOURCES.filter(x=>x.kind!=='regional_overview'))for(const ref of v.variants)assert(ref.url.startsWith('https://activematterhelp.ru/wiki/maps/'));
const start=code.indexOf('function project('),end=code.indexOf('function evalProof()',start);
assert(start>=0&&end>start);
const inputs={
  targetBuild:{value:'0.4.0.199'},
  targetMode:{value:'Isolated PvE'},
  variantSelect:{selectedOptions:[{textContent:'Airport'}]},
  confirmIdentity:{checked:false}
};
const $=id=>inputs[id]||(()=>{throw Error('Unknown input '+id)})();
const make=new Function('$','id','imgInfo','imgFile','sha',code.slice(start,end)+';return {project,assess};');
const state=()=>make($,'airport',{width:1920,height:1080},{name:'airport_game_capture.png'},'a'.repeat(64));
const anchors=[
 ...[[8,11],[89,9],[15,90],[82,82]].map(([x,y])=>({x,y,u:x,v:y,role:'fit',manual:true})),
 ...[[34,67],[64,35]].map(([x,y])=>({x,y,u:x,v:y,role:'check',manual:true}))
];
const fixture={
 format:'am-map-evidence-v1',map:'airport',
 version:'0.4.0.199',mode:'Isolated PvE',raidVariant:'Airport',
 screenshotFile:'airport_game_capture.png',screenshotSize:{width:1920,height:1080},
 screenshotSha256:'a'.repeat(64),sameLegacyCrop:true,
 calibration:{matrix:[1,0,0,0,1,0],trainingRmsPct:0,independentCheckRmsPct:0},
 anchors
};
const audit=state().assess;
assert.equal(audit(fixture).reasons.length,0, 'Matching image and 4FIT/2CHECK should permit manual opt-in');
function rejected(x,msg){assert(audit(x).reasons.length>0,msg)}
rejected({...fixture,map:'cargo'},'wrong map');
rejected({...fixture,version:'0.4.0.173'},'wrong patch');
rejected({...fixture,mode:'Open PvPvE'},'wrong mode');
rejected({...fixture,raidVariant:'Other'},'wrong variant');
rejected({...fixture,screenshotFile:'other.png'},'wrong screenshot name');
rejected({...fixture,screenshotSize:{width:1600,height:900}},'wrong screenshot dimensions');
rejected({...fixture,screenshotSha256:'b'.repeat(64)},'wrong SHA');
rejected({...fixture,sameLegacyCrop:false},'wrong coordinate crop');
rejected({...fixture,anchors:anchors.slice(1)},'insufficient training controls');
rejected({...fixture,anchors:anchors.filter(a=>a.role==='fit')},'missing holdout controls');
rejected({...fixture,calibration:{matrix:[1,0,0]}},'invalid matrix');
inputs.confirmIdentity.checked=false;
rejected({...fixture,screenshotSha256:null},'legacy evidence requires explicit image confirmation');
inputs.confirmIdentity.checked=true;
assert.equal(audit({...fixture,screenshotSha256:null}).reasons.length,0, 'Legacy explicit manual identity acceptance');
inputs.targetBuild.value='';
rejected(fixture,'target game build required');
console.log('PASS reference atlas: 14 maps / 30 raid variants / 275 historic markers, JS syntax, proper hash/crop/patch/mode/variant/fit/holdout gating');
