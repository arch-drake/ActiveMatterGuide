/* FIELD OPERATIONS 2.1 / PvP playbook — never changes PvE storage keys */
(function(){'use strict';const A=window.AM21,key='am_v21_pvp';
 const $=A.pick,record=A.read(key,{role:'solo',map:'airport',prep:{},history:[]});
 if(!record||typeof record!=='object')return;
 record.prep=record.prep&&typeof record.prep==='object'?record.prep:{};record.history=Array.isArray(record.history)?record.history:[];
 const tasks=[['kit','Inspect armor condition, weapon and matching ammunition'],['heal','Reserve healing and a fallback retreat route'],['objective','Identify main objective, extraction and abort condition'],['audio','Check audio awareness; never depend on footsteps alone'],['cover','Identify hard cover and at least one alternate exit'],['risk','Decide whether valuable loot is worth remaining exposed'],['reload','After a fight, check ammo, healing and surroundings before looting']];
 const advice={solo:['Avoid third-party fights when the objective is complete.','Do not investigate every gunshot: identify whether it affects your route.','Choose an exit before opening a contested objective.','After firing, relocate; assume your previous position is known.'],squad:['Assign a caller and communicate contact locations clearly.','Avoid stacking everyone at one doorway or extraction approach.','Agree on regroup points before the next engagement.','Confirm friendly positions and firing lanes: accidental friendly fire can matter.']};
 const mode=$('#am21PvpRole'),map=$('#am21PvpMap');for(const o of $('#laMap').options){const c=document.createElement('option');c.value=o.value;c.textContent=o.textContent;map.appendChild(c)}
 mode.value=['solo','squad'].includes(record.role)?record.role:'solo';map.value=record.map||'airport';
 function persist(){record.role=mode.value;record.map=map.value;A.write(key,record)}
 function render(){const group=mode.value;$('#am21PvpPrep').innerHTML=tasks.map(([id,t])=>`<label><input type="checkbox" data-am21-prep="${id}" ${record.prep[group+'-'+id]?'checked':''}><span>${A.esc(t)}</span></label>`).join('');
 $('#am21PvpAdvice').innerHTML='<ol>'+advice[group].map(t=>'<li>'+A.esc(t)+'</li>').join('')+'</ol>';
 $('#am21PvpHistory').innerHTML=record.history.length?record.history.slice(0,30).map(r=>`<div class="am21-record"><b>${A.esc(r.map)}</b> · ${A.esc(r.role)} · ${A.esc(r.outcome)} · ${Number(r.contacts)||0} contacts · <small>${A.esc(r.date)}</small><p>${A.esc(r.note)}</p></div>`).join(''):'<p class="small muted">No saved PvP sessions yet.</p>';
 }
 mode.addEventListener('change',()=>{persist();render()});map.addEventListener('change',persist);
 $('#am21PvpPrep').addEventListener('change',e=>{const k=e.target.dataset.am21Prep;if(!k)return;record.prep[mode.value+'-'+k]=e.target.checked;persist()});
 $('#am21PvpAdd').onclick=()=>{record.history.unshift({date:new Date().toISOString(),map:map.value,role:mode.value,outcome:$('#am21PvpOutcome').value,contacts:Math.max(0,Math.min(99,Number($('#am21PvpContacts').value)||0)),note:$('#am21PvpNote').value.slice(0,5000)});record.history=record.history.slice(0,200);persist();$('#am21PvpNote').value='';render()};
 $('#am21PvpExport').onclick=()=>A.jsonExport('active-matter-pvp-field-records.json',{format:'am-pvp-v21',record});
 $('#am21PvpClear').onclick=()=>{if(!confirm('Delete your local PvP history and checklist? Export a full guide backup first.'))return;record.history=[];record.prep={};persist();render()};render();
})();
