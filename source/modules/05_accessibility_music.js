/* FIELD OPERATIONS 2.1 / accessibility & soundtrack preferences */
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
