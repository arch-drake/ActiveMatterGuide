/* FIELD OPERATIONS 2.1 / introductory help and homebase */
(function(){'use strict';const A=window.AM21,$=A.pick;
 $('#am21HomeCards').innerHTML=A.home.map((x,i)=>`<article class="card"><span class="am-tag">${String(i+1).padStart(2,'0')} / FIELD SYSTEM</span><h3>${A.esc(x.title)}</h3><p class="am-subtitle">${A.esc(x.tag)}</p><p>${A.esc(x.text)}</p></article>`).join('');
 const tour=[
 ['Choose your mode','Solo / Team toggle changes PvE advice. Open Raid brings rival players: visit the separate PvP tab for solo or squad planning.'],
 ['Maps in two projections','Every one of the 14 maps now has Flat and Isometric controls. Rotate in 15° steps, zoom and pan, but remember that fictional terrain art is not an in-game map scan.'],
 ['Investigations & creatures','Use Investigations for manually tracking researched stages and Monsters for evidence-tagged dossiers and personal observations. The guide does not read your game progress.'],
 ['Homebase systems','Visit Homebase for a quick workflow from extraction to equipment, processing and your next deployment. Always verify current crafting prerequisites inside the game.'],
 ['Signal Archive','Record personal music cassette discoveries and review community-only location hints. The guide soundtrack contains 11 original instrumental synth loops.'],
 ['Protect your progress','Export a complete JSON backup from Backup before moving this HTML to a new folder, browser or computer. Your saved checklists belong to your browser profile.']
 ];
 let idx=0;const dialog=$('#am21Tour');
 function draw(){const t=tour[idx];$('#am21TourBody').innerHTML=`<h3>${A.esc(t[0])}</h3><p>${A.esc(t[1])}</p>`;$('#am21TourCount').textContent=(idx+1)+' / '+tour.length;$('#am21TourBack').disabled=idx===0;$('#am21TourNext').textContent=idx===tour.length-1?'Finish ✓':'Next →'}
 function open(){idx=0;draw();if(!dialog.open)dialog.showModal()}
 $('#am21StartTour').onclick=open;$('#am21HomeTour').onclick=open;$('#am21TourClose').onclick=()=>dialog.close();
 $('#am21TourBack').onclick=()=>{idx=Math.max(0,idx-1);draw()};
 $('#am21TourNext').onclick=()=>{if(idx===tour.length-1){dialog.close();return}idx++;draw()};
})();
