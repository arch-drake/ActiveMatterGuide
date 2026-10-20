/* FIELD OPERATIONS 2.1 / core & persistence — standalone, isolated from legacy state */
window.AM21=(function(){
 'use strict';
 const pick=(s)=>document.querySelector(s),all=(s)=>Array.from(document.querySelectorAll(s));
 function read(key, fallback){try{const v=localStorage.getItem(key);return v===null?structuredClone(fallback):JSON.parse(v)}catch(e){return JSON.parse(JSON.stringify(fallback))}}
 function write(key,value){try{localStorage.setItem(key,JSON.stringify(value));return true}catch(e){return false}}
 function esc(t){return String(t??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
 function jsonExport(name,value){const b=new Blob([JSON.stringify(value,null,2)],{type:'application/json'}),u=URL.createObjectURL(b),a=document.createElement('a');a.href=u;a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(u),2500)}
 const home=[
  {title:'Mission terminal',tag:'Choose mode & map',text:'Select the location, variant and party setting; always confirm whether Open or Isolated is actually available before deployment.'},
  {title:'Stash & equipment',tag:'Pack deliberately',text:'Organize recovered items and inspect equipment condition, ammunition and protection before committing a loadout.'},
  {title:'Workshop / processing',tag:'Convert recovered material',text:'Processing and crafting use resources found across raids. The current in-game interface is authoritative for recipe inputs, yields and prerequisites.'},
  {title:'Research & Monolith',tag:'Plan long-term progress',text:'Use the research and progression interfaces to inspect what is unlocked and what resources are missing. Avoid assuming every upgrade follows one fixed order.'},
  {title:'Investigations',tag:'Track stages separately',text:'Check exact current objective text, completion conditions and gear requirements; the guide’s 53 curated chains are not the whole live catalogue.'},
  {title:'Extraction & recovery',tag:'Close the loop',text:'Use a known exit, confirm carried objective items, and review what actually returned to the shelter. Saved guide notes are not game save files.'}
 ];
 return {pick,all,read,write,esc,jsonExport,home};
})();
