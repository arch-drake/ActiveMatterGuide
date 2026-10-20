/* FIELD OPERATIONS 2.1 / signal archive; community leads are not guarantees */
(function(){'use strict';const A=window.AM21,$=A.pick,k='am_v21_signals';
 const saved=A.read(k,{entries:[]});saved.entries=Array.isArray(saved.entries)?saved.entries:[];
 const suggestions=['Music cassette — unidentified track','Movie cassette (not necessarily music)','Cassette recorder — resource/item, not a music tape'];
 function clean(s){return String(s||'').slice(0,160)}
 function render(){const items=$('#am21SignalEntries');items.innerHTML=saved.entries.length?saved.entries.map((t,i)=>`<label><input type="checkbox" data-am21-signal="${i}" ${t.collected?'checked':''}><span>${A.esc(t.title)}</span><button type="button" data-am21-remove="${i}" aria-label="Remove ${A.esc(t.title)}">✕</button></label>`).join(''):'<p class="small muted">Add or mark your own cassette discoveries. The guide cannot infer actual game inventory.</p>'}
 function persist(){A.write(k,saved)}
 $('#am21SignalEntries').addEventListener('change',e=>{if(!('am21Signal' in e.target.dataset))return;const i=Number(e.target.dataset.am21Signal);if(saved.entries[i]){saved.entries[i].collected=!!e.target.checked;persist()}});
 $('#am21SignalEntries').addEventListener('click',e=>{const b=e.target.closest('[data-am21-remove]');if(!b)return;saved.entries.splice(Number(b.dataset.am21Remove),1);persist();render()});
 $('#am21SignalAdd').onclick=()=>{let t=clean($('#am21SignalNew').value.trim());if(!t)return;if(saved.entries.some(e=>e.title.toLowerCase()===t.toLowerCase()))return;saved.entries.push({title:t,collected:false});$('#am21SignalNew').value='';persist();render()};
 $('#am21SignalExport').onclick=()=>A.jsonExport('active-matter-cassette-collection.json',{format:'am-signals-v21',exportedAt:new Date().toISOString(),entries:saved.entries});
 const leads=[
 {name:'Shegolskoe cottages / floating houses',what:'Cassette recorders reported on loose shelves and in houses',confidence:'Community — anecdotal',url:'https://www.reddit.com/r/ActiveMatter/comments/1wyavyf/cassette_recorders/'},
 {name:'Factory dormitories',what:'Cassette recorders reportedly found in dormitories',confidence:'Community — anecdotal',url:'https://www.reddit.com/r/ActiveMatter/comments/1wyavyf/cassette_recorders/'},
 {name:'Gigastructure',what:'Player reported cassette recorders; Open-only reference, not Isolated PvE',confidence:'Community — anecdotal',url:'https://www.reddit.com/r/ActiveMatter/comments/1wyavyf/cassette_recorders/'},
 {name:'Garages / general loot containers',what:'Older reports list recorders among valuable household loot, not confirmed cassette tracks',confidence:'Community — older lead',url:'https://www.reddit.com/r/ActiveMatter/comments/1o4loyc/'}
 ];
 $('#am21SignalLeads').innerHTML=leads.map(x=>`<div class="am21-record"><b>${A.esc(x.name)}</b><p>${A.esc(x.what)}</p><span class="am-tag community">${A.esc(x.confidence)}</span> <a href="${x.url}" rel="noopener noreferrer" target="_blank">Community source ↗</a></div>`).join('');
 $('#am21OpenMusic').onclick=()=>{const dock=$('#amMusicDock');if(dock.classList.contains('minimized'))$('#amAudioCollapse').click();dock.scrollIntoView({behavior:'smooth',block:'nearest'});$('#amAudioPlay').focus()};
 render();
})();
