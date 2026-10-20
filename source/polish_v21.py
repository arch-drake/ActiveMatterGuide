from pathlib import Path
r=Path(__file__).resolve().parent.parent;p=r/'active_matter_solo_pve_field_guide.html';s=p.read_text()
old='''#laWorld .la-pin .la-pin-badge,#laWorld .la-pin .la-pin-label{transform:none}#laIsoToggle.active{border-color:var(--am-accent);background:var(--panel2)}'''
new='''#laWorld .la-pin .la-pin-badge,#laWorld .la-pin .la-pin-label{transform:scaleY(var(--am-map-correction,1)) rotate(var(--am-map-angle,0deg));transform-origin:center center}#laIsoToggle.active{border-color:var(--am-accent);background:var(--panel2)}
body[data-am-theme="notebook"] .hero p,body[data-am-theme="notebook"] .hero .kicker,body[data-am-theme="notebook"] .am-theme-tools label{color:#224655}
body[data-am-theme="notebook"] .heroart strong{color:#fff0e8;background:#18222bea}
body[data-am-theme="notebook"] .badge,body[data-am-theme="notebook"] .pill{color:#2c5160;border-color:#668895}
body[data-am-theme="notebook"] .la-panel,body[data-am-theme="notebook"] .la-infobox,body[data-am-theme="notebook"] .la-source-control,body[data-am-theme="notebook"] .am-map-quickbar,body[data-am-theme="notebook"] .am21-hero .am21-record{color:#e9f5f8}
body[data-am-theme="notebook"] .la-panel>p:not(.la-terrain-warning),body[data-am-theme="notebook"] .la-panel label,body[data-am-theme="notebook"] .la-map-legend{color:#d2eaf0}
body[data-am-theme="notebook"] .la-panel .la-terrain-warning{color:#dce9e6}
body[data-am-theme="notebook"] .la-panel h3{color:#b9eeff}
body[data-am-theme="notebook"] .la-panel input,body[data-am-theme="notebook"] .la-panel select{color:#eaf1f3;background:#101e27}
body[data-am-theme="notebook"] .am-theme-chips button{background:var(--chip)!important}
body[data-am-theme="notebook"] .am-metric span,body[data-am-theme="notebook"] .am-mini-card p,body[data-am-theme="notebook"] .card>p{color:#3e555a}
body[data-am-theme="notebook"] .am21-checklist label{color:#28434b}
body[data-am-density="compact"] .card{padding:10px}body[data-am-density="compact"] .am21-hero{padding:12px}
body[data-am-density="compact"] .am21-checklist{gap:3px}body[data-am-density="compact"] .am21-checklist label{padding:5px 7px}
body[data-am-density="accessible"]{font-size:17px;line-height:1.65}body[data-am-density="accessible"] button,body[data-am-density="accessible"] input,body[data-am-density="accessible"] select{min-height:46px}
body[data-am-density="accessible"] .la-pin{font-size:14px}
'''
assert old in s;s=s.replace(old,new)
# display mode dropdown just after theme select; unique anchor inside theme settings
anchor='<option value="notebook">Field Notebook / Light</option></select><div id="amThemeChips"'
replacement='<option value="notebook">Field Notebook / Light</option></select><label for="am21Density">Display</label><select id="am21Density" aria-label="Display density"><option value="standard">Standard</option><option value="compact">Compact</option><option value="accessible">Accessible</option></select><div id="amThemeChips"'
assert anchor in s;s=s.replace(anchor,replacement)
# add audio buttons in player dock, persist favorites independently
needle='<button id="amAudioDownload" type="button" title="Save the original track separately">Save MP3</button>'
assert needle in s;s=s.replace(needle,'<button type="button" id="am21AudioFav" title="Favorite current original track">☆ Favorite</button><button type="button" id="am21AudioFavOnly" aria-pressed="false" title="Next and shuffle favorites only">☆ Favorites only: OFF</button>'+needle)
# insert custom module before closing script v21
code='''/* FIELD OPERATIONS 2.1 / accessibility & soundtrack preferences */
(function(){'use strict';const A=window.AM21,$=A.pick,density=$('#am21Density'),key='am_v21_ui_preferences',audioKey='am_v21_audio_favorites';
 let prefs=A.read(key,{density:'standard'});if(!prefs||typeof prefs!=='object')prefs={density:'standard'};
 density.value=['standard','compact','accessible'].includes(prefs.density)?prefs.density:'standard';document.body.dataset.amDensity=density.value;
 density.addEventListener('change',()=>{document.body.dataset.amDensity=density.value;prefs.density=density.value;A.write(key,prefs)});
 let favorites=A.read(audioKey,{names:[],only:false});if(!favorites||typeof favorites!=='object')favorites={names:[],only:false};favorites.names=Array.isArray(favorites.names)?favorites.names:[];
 const options=()=>Array.from($('#amAudioTrack').options).map(o=>o.value);
 function current(){return $('#amAudioTrack').value}
 function persist(){A.write(audioKey,favorites)}
 function draw(){const name=current();$('#am21AudioFav').textContent=favorites.names.includes(name)?'★ Favorited':'☆ Favorite';$('#am21AudioFavOnly').textContent=favorites.only?'★ Favorites only: ON':'☆ Favorites only: OFF';$('#am21AudioFavOnly').setAttribute('aria-pressed',String(!!favorites.only))}
 $('#am21AudioFav').onclick=()=>{const name=current();favorites.names=favorites.names.includes(name)?favorites.names.filter(x=>x!==name):[...favorites.names,name];if(!favorites.names.length)favorites.only=false;persist();draw()};
 $('#am21AudioFavOnly').onclick=()=>{if(!favorites.names.length){$('#amAudioState').textContent='Favorite a track first.';return}favorites.only=!favorites.only;persist();draw()};
 function handleNext(e,shuffle){if(!favorites.only)return;const list=options().filter(x=>favorites.names.includes(x));if(!list.length){favorites.only=false;persist();draw();return}e.stopImmediatePropagation();e.preventDefault();const name=current();let next;if(shuffle){const pool=list.filter(x=>x!==name);next=(pool.length?pool:list)[Math.floor(Math.random()*(pool.length||list.length))]}else{const i=list.indexOf(name);next=list[(i+1)%list.length]}$('#amAudioTrack').value=next;$('#amAudioTrack').dispatchEvent(new Event('change',{bubbles:true}));draw()}
 $('#amAudioNext').addEventListener('click',e=>handleNext(e,false),true);
 $('#amAudioShuffle').addEventListener('click',e=>handleNext(e,true),true);
 $('#amAudioTrack').addEventListener('change',draw);
 draw();
})();
'''
source=r/'source/modules/05_accessibility_music.js';source.write_text(code)
anchor='\n</script>\n</body>'
assert anchor in s
s=s.replace(anchor,'\n'+code+'\n</script>\n</body>',1)
p.write_text(s)
print('polished',p.stat().st_size)
