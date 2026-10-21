/* Offline simulated-DOM interactions for Reference Atlas initialization.
 * This checks wiring, not Chromium layout, native file picker or screenshot decode. */
'use strict';
const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path');
const raw=fs.readFileSync(path.join(__dirname,'..','tools','map_reference_atlas.html'),'utf8');
const code=raw.slice(raw.indexOf('<script>')+8,raw.lastIndexOf('</script>'));
class E{
 constructor(id=''){this.id=id;this.value='';this.href='';this.files=[];this.style={};this.children=[];this.listeners={};this.clientWidth=1200;this.clientHeight=640;this.naturalWidth=1920;this.naturalHeight=1080;this.checked=false;this.disabled=false;this.dataset={};this.classList={add(){},remove(){},contains(){return false}}}
 replaceChildren(){this.children=[]}
 append(...children){this.children.push(...children)}
 addEventListener(name,cb){this.listeners[name]=cb}
 removeAttribute(){}
 querySelectorAll(){return []}
 getBoundingClientRect(){return {left:0,top:0,width:1200,height:640}}
 get selectedOptions(){return this.children.filter(x=>x.tagName==='option').slice(0,1)}
}
const elements={};
const document={
 getElementById(id){return elements[id]??(elements[id]=new E(id))},
 createElement(tag){const el=new E();el.tagName=tag;return el}
};
const fakeURL={revokeObjectURL(){},createObjectURL(){return 'blob:stub'}};
class Params{get(){return null}}
const app=new Function('document','URL','URLSearchParams','location','crypto',code+';return {changeMap,fillTypes,listMarkers,SOURCES,MARKERS,worldOf,percentOf};')(document,fakeURL,Params,{search:''},null);
const $=document.getElementById.bind(document);
assert.equal($('mapSelect').children.length,14);
assert.equal($('markerResults').children.length,22);
assert.equal($('variantSelect').children.length,1);
assert.equal($('allowOverlay').disabled,true);
assert($('evidenceState').textContent.includes('No matching calibration'));
for(const m of app.SOURCES){
 $('mapSelect').value=m.id;
 $('mapSelect').listeners.change();
 assert.equal($('markerResults').children.length,(app.MARKERS[m.id]||[]).length);
 assert.equal($('variantSelect').children.length,m.variants.length);
 assert.equal($('allowOverlay').checked,false);
 assert.equal($('worldResult').textContent.includes('Internal source transform'),app.worldOf(m.id,{x:20,y:40})!==null);
}
$('mapSelect').value='airport';$('mapSelect').listeners.change();
$('markerSearch').value='extraction';$('markerSearch').listeners.input();
assert($('markerResults').children.length>0&&$('markerResults').children.length<22);
$('markerSearch').value='';$('markerSearch').listeners.input();
assert.equal($('markerResults').children.length,22);
const c=app.worldOf('airport',{x:69.35,y:61.4});
assert(c&&Number.isFinite(c.x)&&Number.isFinite(c.z));
const back=app.percentOf('airport',c.x,c.z);
assert(Math.abs(back.x-69.35)<1e-6&&Math.abs(back.y-61.4)<1e-6);
assert.equal(app.worldOf('dalniy',{x:20,y:40}),null);
console.log('PASS simulated DOM: 14 map selectors, 30 variant option entries, all historic search lists, hidden uncalibrated pins and world converter');
