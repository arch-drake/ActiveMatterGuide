/* Regression guard: homepage source-first routing, 13 live source rasters,
 * Gigastructure floor-only separation and disabled unaligned legacy markers.
 * node tests/map_primary_experience.test.cjs
 * This is offline UI wiring/syntax QA, not a claim about tile availability or map accuracy. */
'use strict';
const assert=require('node:assert/strict');
const fs=require('node:fs'),path=require('node:path');
const root=path.join(__dirname,'..');
const page=fs.readFileSync(path.join(root,'index.html'),'utf8');
const html=fs.readFileSync(path.join(root,'tools','all_maps_live_reference.html'),'utf8');
const board=fs.readFileSync(path.join(root,'tools','map_fidelity_dashboard.html'),'utf8');
const notes=fs.readFileSync(path.join(root,'README.md'),'utf8');
const js=html.slice(html.indexOf('<script>')+8,html.lastIndexOf('</script>'));
assert(js.length>10000);
new Function(js);
assert(page.indexOf('Explore Source Atlas')<page.indexOf('Open offline field companion'),'Homepage map CTA must be primary');
assert(page.includes('Unreconciled legacy marker pins'));
assert(html.includes('id="specialList"')&&html.includes('HISTORICAL MARKER OVERLAYS: OFF'));
assert(!html.includes('tactical_detail.webp'),'No old geometric backgrounds in primary atlas');
assert(!js.includes('drawPins')&&!js.includes('pinLayer'),'Never render unaligned historic pins over live images');
assert(board.includes("all_maps_live_reference.html?map="),'QA cards should deep-link to correct source view');
assert(notes.includes('Primary map presentation and accuracy'));
class FakeElement {
  constructor(tag='div'){
    this.tagName=tag.toLowerCase();this.children=[];this.style={};this.dataset={};this.attrs={};
    this.listeners={};this.disabled=false;this.textContent='';this.value='';
    this.clientWidth=1200;this.clientHeight=680;
    this.classList={add(){},remove(){}};
  }
  append(...v){this.children.push(...v)}
  replaceChildren(...v){this.children=[...v]}
  setAttribute(k,v){this.attrs[k]=v}
  querySelector(tag){return this.children.find(x=>x.tagName===tag)||null}
  querySelectorAll(tag){return this.children.filter(x=>x.tagName===tag)}
  addEventListener(name,fn){this.listeners[name]=fn}
  getBoundingClientRect(){return {left:0,top:0,width:1200,height:680}}
}
class Params {constructor(query){this.q=query||''}get(k){const match=this.q.match(new RegExp('[?&]'+k+'=([^&]+)'));return match?decodeURIComponent(match[1]):null}}
function boot(query){
  const nodes=new Map();
  const doc={getElementById(id){if(!nodes.has(id))nodes.set(id,new FakeElement());return nodes.get(id)},
    createElement(tag){return new FakeElement(tag)}};
  const el=doc.getElementById.bind(doc);
  el('empty').append(new FakeElement('b'));
  el('markerPolicy').append(new FakeElement('span'));
  const app=new Function('document','URL','URLSearchParams','location',js+';return {M,switchMap,live};')
    (doc,{revokeObjectURL(){}},Params,{search:query});
  return {app,el};
}
const {app,el}=boot('?map=gigastructure');
const geo=app.M.filter(m=>m.region!==null);
const expected=['airport','headquarters','downtown','dam','cargo','factory','dogorsk','military','ozernoe','park','scrapyard','shegolskoe','dalniy'];
assert.deepEqual(geo.map(x=>x.id),expected);
assert.equal(app.M.length,14);
assert.equal(app.M.reduce((n,m)=>n+m.variants.length,0),30);
assert.equal(el('locationList').children.length,13);
assert.equal(el('specialList').children.length,1);
assert.equal(el('specialList').children[0].dataset.id,'gigastructure');
assert.equal(el('specialList').children[0].attrs['aria-current'],'true','Deep-linked special map needs a visible active selection');
assert(el('loadLive').disabled&&el('status').textContent.includes('special floor'));
app.live();
assert.equal(el('stage').children.length,0,'Special map must never create fabricated raster');
app.switchMap('airport');
assert.equal(el('specialList').children[0].attrs['aria-current'],'false');
assert.equal(el('locationList').children[0].attrs['aria-current'],'true');
assert.equal(el('stage').children.length,0,'No third-party tile requests before opt-in');
app.live();
assert.equal(el('stage').children.length,16,'Opt-in should generate 4x4 source tiles');
assert.equal(el('evidenceLink').href,'map_reference_atlas.html?map=airport');
for(const m of app.M){
  app.switchMap(m.id);
  assert.equal(el('stage').children.length,0,'Map switch must clear previous source tiles');
  assert.equal(el('evidenceLink').href,'map_reference_atlas.html?map='+m.id);
  assert(!el('markerPolicy').querySelector('span').textContent.includes('verified live positions'));
}
console.log('PASS primary atlas: homepage CTA, 13 raster sources, 1 isolated floor-only special, 30 variants, source opt-in, deep links, zero legacy overlays');
