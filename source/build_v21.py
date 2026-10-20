from pathlib import Path
import re, json, base64, hashlib
root=Path(__file__).resolve().parent.parent
p=root/'active_matter_solo_pve_field_guide.html'
s=p.read_text()
# source input must be 2.0.2 before the added v21 code
assert '<!-- AM21 COMMUNITY EDITION START -->' not in s

def rep(a,b,limit=1):
 global s
 assert a in s, 'missing old patch anchor: '+a[:110]
 s=s.replace(a,b,limit)

# MAP PROJECTION: transform around center; preserve screen->map coordinate conversion under rotation and tilt
rep("let current='airport',selected=null,zoom=1,panX=0,panY=0,ownImage={},artMode=false,viewMode='grid',addNoteMode=false,routeStops=[],pointerState=null;",
"""let current='airport',selected=null,zoom=1,panX=0,panY=0,ownImage={},artMode=false,viewMode='grid',addNoteMode=false,routeStops=[],pointerState=null;
const ISO_KEY='am_v21_atlas_projection';
let isoPrefs=readJSON(ISO_KEY,{enabled:true,angle:0});if(!isoPrefs||typeof isoPrefs!=='object')isoPrefs={enabled:true,angle:0};
let isoEnabled=isoPrefs.enabled!==false, isoAngle=Number.isFinite(Number(isoPrefs.angle))?Number(isoPrefs.angle)%360:0;
const ISO_TILT=0.66;
function projectionAngle(){return (isoEnabled?45:0)+isoAngle}
function projectionPoint(x,y){const w=viewport.clientWidth||1240,h=viewport.clientHeight||800,dx=x-w/2,dy=y-h/2;
 const a=projectionAngle()*Math.PI/180,c=Math.cos(a),s=Math.sin(a),v=isoEnabled?ISO_TILT:1;
 return {x:panX+w/2+zoom*(dx*c-v*dy*s),y:panY+h/2+zoom*(dx*s+v*dy*c)};
}
function inverseProjection(clientX,clientY){const r=viewport.getBoundingClientRect(),w=viewport.clientWidth||1240,h=viewport.clientHeight||800;
 const dx=(clientX-r.left-panX-w/2)/zoom,dy=(clientY-r.top-panY-h/2)/zoom;
 const a=projectionAngle()*Math.PI/180,c=Math.cos(a),s=Math.sin(a),v=isoEnabled?ISO_TILT:1;
 return {x:(w/2+c*dx+s*dy)/w,y:(h/2+(-s*dx+c*dy)/v)/h};
}
function saveProjection(){writeJSON(ISO_KEY,{enabled:isoEnabled,angle:isoAngle})}
function projectionUI(){const toggle=q('#laIsoToggle'),val=q('#laRotationValue');if(toggle){toggle.textContent=isoEnabled?'◈ Isometric: ON':'▣ Flat: ON';toggle.setAttribute('aria-pressed',String(isoEnabled));toggle.classList.toggle('active',isoEnabled)}if(val)val.textContent=Math.round(((projectionAngle()%360)+360)%360)+'°'}
""")
rep("function styleWorld(){world.style.transform=`translate(${panX}px,${panY}px) scale(${zoom})`;q('#laZoomLabel').textContent=Math.round(zoom*100)+'%';}",
"""function styleWorld(){
 world.style.transform=`translate(${panX}px,${panY}px) rotate(${projectionAngle()}deg) scale(${zoom}, ${zoom*(isoEnabled?ISO_TILT:1)})`;
 world.style.transformOrigin='center center';
 world.style.setProperty('--am-map-angle',(-projectionAngle())+'deg');world.style.setProperty('--am-map-correction',String(1/(isoEnabled?ISO_TILT:1)));
 q('#laZoomLabel').textContent=Math.round(zoom*100)+'%';projectionUI();
}
""")
rep("function focusPin(p){zoom=Math.max(zoom,1.7);const w=viewport.clientWidth||1240,h=viewport.clientHeight||800,place=calPoint(p);panX=w/2-place.x/100*w*zoom;panY=h/2-place.y/100*h*zoom;styleWorld()}",
"""function focusPin(p){zoom=Math.max(zoom,1.7);panX=0;panY=0;const w=viewport.clientWidth||1240,h=viewport.clientHeight||800,place=calPoint(p),sc=projectionPoint(place.x/100*w,place.y/100*h);panX=w/2-sc.x;panY=h/2-sc.y;styleWorld()}
""")
# fix visual pin counter-rotation by applying transform to inner children, CSS injected later
rep("const rect=world.getBoundingClientRect();const xx=(e.clientX-rect.left)/rect.width,yy=(e.clientY-rect.top)/rect.height;", "const mapped=inverseProjection(e.clientX,e.clientY);const xx=mapped.x,yy=mapped.y;")
rep("const rect=world.getBoundingClientRect();if(!rect.width||!rect.height)return;const x=100*(e.clientX-rect.left)/rect.width,y=100*(e.clientY-rect.top)/rect.height;", "const mapped=inverseProjection(e.clientX,e.clientY);const x=100*mapped.x,y=100*mapped.y;")
# default iso grid status in map console
rep("q('#laZoomIn').onclick=()=>{zoom=Math.min(5,zoom*1.25);styleWorld()};",
"""q('#laIsoToggle').onclick=()=>{isoEnabled=!isoEnabled;saveProjection();resetView()};
q('#laRotateLeft').onclick=()=>{isoAngle=(isoAngle-15+360)%360;saveProjection();styleWorld()};
q('#laRotateRight').onclick=()=>{isoAngle=(isoAngle+15)%360;saveProjection();styleWorld()};
q('#laRotationReset').onclick=()=>{isoAngle=0;saveProjection();resetView()};
q('#laZoomIn').onclick=()=>{zoom=Math.min(5,zoom*1.25);styleWorld()};""")
rep("<div class=\"la-row\" style=\"justify-content:space-between\"><h3 id=\"laTitle\">Local map</h3><div class=\"la-row\"><button id=\"laZoomIn\">+</button><button id=\"laZoomOut\">−</button><span id=\"laZoomLabel\" class=\"la-inline-tag\">100%</span></div></div>",
"""<div class="la-row" style="justify-content:space-between"><h3 id="laTitle">Local map</h3><div class="la-row"><button id="laIsoToggle" type="button" aria-pressed="true">◈ Isometric: ON</button><button id="laRotateLeft" type="button" aria-label="Rotate map counterclockwise 15 degrees">↶ 15°</button><button id="laRotateRight" type="button" aria-label="Rotate map clockwise 15 degrees">↷ 15°</button><button id="laRotationReset" type="button" aria-label="Reset map rotation">⟲</button><span id="laRotationValue" class="la-inline-tag">45°</span><button id="laZoomIn" type="button" aria-label="Zoom in">+</button><button id="laZoomOut" type="button" aria-label="Zoom out">−</button><span id="laZoomLabel" class="la-inline-tag">100%</span></div></div>""")
rep('Map navigation stays inside this guide. Topographic-style relief is available for every view;', 'Map navigation stays inside this guide. Every map supports reversible isometric/flat projection, 15° rotation, zoom and pan. The projection is illustrative, not surveyed 3D geometry. Topographic-style relief is available for every view;')
# IMPORTANT: old map view uses pin append children - keep marker coords stable after projection

# Theme list + new theme styles; matches game-inspired concept not cloned game interface
rep("const amAllowedThemes=new Set(['fracture','shelter','reactor','rift','crimson','graphite','highcontrast']);",
"const amAllowedThemes=new Set(['fracture','shelter','reactor','rift','crimson','graphite','highcontrast','soviet','monolith','containment','anomalyfield','notebook']);")
rep('<option value="highcontrast">Signal / High Contrast</option></select>',
'''<option value="highcontrast">Signal / High Contrast</option><option value="soviet">Soviet Terminal / Phosphor</option><option value="monolith">Monolith Research / Blue</option><option value="containment">Containment Breach / Orange</option><option value="anomalyfield">Anomaly Field / Cyan</option><option value="notebook">Field Notebook / Light</option></select>''')
rep('</div><span class="am-tag official">OFFLINE GUIDE · LOCAL PROGRESS</span></div>',
'''<button type="button" title="Soviet Terminal" aria-label="Soviet Terminal" data-theme-choice="soviet" class="am-theme-extra" style="--chip:#83956b"></button><button type="button" title="Monolith Research" aria-label="Monolith Research" data-theme-choice="monolith" class="am-theme-extra" style="--chip:#80d3f9"></button><button type="button" title="Containment Breach" aria-label="Containment Breach" data-theme-choice="containment" class="am-theme-extra" style="--chip:#f79047"></button><button type="button" title="Anomaly Field" aria-label="Anomaly Field" data-theme-choice="anomalyfield" class="am-theme-extra" style="--chip:#53ece4"></button><button type="button" title="Field Notebook" aria-label="Field Notebook" data-theme-choice="notebook" class="am-theme-extra" style="--chip:#e9e5d9"></button></div><span class="am-tag official">OFFLINE GUIDE · LOCAL PROGRESS</span></div>''')
# Important controls are inside existing amThemeChips div (right before original closing div)

# Insert nav buttons into main section; command palette detects dynamic nav at page load
rep('<button data-tab="monstercompendium">Monsters</button><button data-tab="fieldmanual">Field Manual</button>',
'<button data-tab="monstercompendium">Monsters</button><button data-tab="am21pvp">PvP</button><button data-tab="am21home">Homebase</button><button data-tab="am21signals">Signals</button><button data-tab="fieldmanual">Field Manual</button>')
rep('<button type="button" id="amResume" title="Jump back to your last guide page">↶ Resume</button>',
'<button type="button" id="am21StartTour" title="Guide tour and help">? Start here</button><button type="button" id="amResume" title="Jump back to your last guide page">↶ Resume</button>')

# Extend soundtrack: five new original synth tracks, encoded locally in the 1-file release
tracks={'dead_relay':'DEAD RELAY','monolith_dream':'MONOLITH DREAM','red_zone':'RED ZONE','glass_reactor':'GLASS REACTOR','dawn_after_extraction':'DAWN AFTER EXTRACTION'}
for k,title in tracks.items():
 blob=(root/'assets/music'/f'{k}.mp3').read_bytes(); val=base64.b64encode(blob).decode('ascii')
 needle='const AMTRACKS={'
 i=s.find(needle); assert i>=0
 s=s[:i]+s[i:].replace(needle,f'const AMTRACKS={{"{k}":"data:audio/mpeg;base64,{val}",',1)
rep("const trackTitles={fracture:'FRACTURE SIGNAL',shelter:'SHELTER AFTERGLOW',perimeter_drift:'PERIMETER DRIFT',anomaly_choir:'ANOMALY CHOIR',midnight_extraction:'MIDNIGHT EXTRACTION',signal_interference:'SIGNAL INTERFERENCE'};",
"const trackTitles={fracture:'FRACTURE SIGNAL',shelter:'SHELTER AFTERGLOW',perimeter_drift:'PERIMETER DRIFT',anomaly_choir:'ANOMALY CHOIR',midnight_extraction:'MIDNIGHT EXTRACTION',signal_interference:'SIGNAL INTERFERENCE',"+','.join(k+":'"+title+"'" for k,title in tracks.items())+"};")
rep('<option value="signal_interference">Signal Interference</option></select>',
'<option value="signal_interference">Signal Interference</option>'+''.join(f'<option value="{k}">{title.title()}</option>' for k,title in tracks.items())+'</select>')

# Add section HTML right before last audio/music dock (sections remain in main? Need locate main closing)
idx=s.find('</main>')
assert idx>0
# inserting before opsdeck ensures older navigation sections unaffected; all new panels remain within main
sections='''<!-- AM21 COMMUNITY EDITION START -->
<section class="section" id="am21pvp"><div class="sectionhead"><div><div class="am-subtitle">OPTIONAL // PLAYER-VERSUS-PLAYER</div><h2>PvP Field Operations</h2><p>Open raids against rival operatives, with separate tracking and Solo / Squad planning. Isolated PvE progress remains untouched.</p></div><span class="pill">OPEN RAID · OPTIONAL</span></div>
<div class="am21-hero"><div><h3>Know your deployment</h3><p><strong>Open + Solo:</strong> rival solo operatives may be present. <strong>Open + Group:</strong> plan around other squads. <strong>Isolated:</strong> use the existing PvE guide instead. Confirm current queue and map mode in game; rules change with updates.</p><a href="https://steamcommunity.com/app/2887580/discussions/0/798966340583113708/" target="_blank" rel="noopener noreferrer">Developer explanation of raid modes ↗</a></div><div class="am21-selector"><label for="am21PvpRole">PvP playstyle</label><select id="am21PvpRole"><option value="solo">Solo Open Raid</option><option value="squad">Squad Open Raid</option></select><label for="am21PvpMap">Map (personal plan)</label><select id="am21PvpMap"></select></div></div>
<div class="am21-columns"><article class="card"><h3>Pre-deployment checklist</h3><div id="am21PvpPrep" class="am21-checklist"></div><p class="small muted">Checks are personal planning records, not game progress or inferred matchmaking state.</p></article><article class="card"><h3>Contact decisions</h3><div id="am21PvpAdvice"></div><div class="am21-grid-2"><label>Session outcome <select id="am21PvpOutcome"><option value="extract">Extracted</option><option value="lost">Failed extraction</option><option value="retreat">Disengaged / returned</option></select></label><label>Hostile contacts (optional)<input id="am21PvpContacts" type="number" min="0" max="99" value="0"></label></div><label for="am21PvpNote">After-action notes</label><textarea id="am21PvpNote" rows="3" placeholder="Routes tested, cover, extraction timing, lessons learned…"></textarea><button id="am21PvpAdd" class="am-action-primary" type="button">Save PvP debrief</button></article></div>
<div class="card"><div class="am21-row"><h3>Private Open Raid history</h3><button id="am21PvpExport" type="button">Export PvP JSON</button><button id="am21PvpClear" type="button">Clear PvP history</button></div><div id="am21PvpHistory" class="am21-history"></div></div><p class="la-terrain-warning">This is a tactical planner, not a competitive advantage overlay. It reads no game memory, never connects to servers, and does not automate or modify the game.</p></section>
<section class="section" id="am21home"><div class="sectionhead"><div><div class="am-subtitle">FIRST DEPLOYMENT // LOCAL SYSTEMS</div><h2>Homebase Systems</h2><p>How to get from found resources to a prepared expedition. Wording and recipes vary across patches; verify all requirements in the current game UI.</p></div><span class="pill">BEGINNER FRIENDLY</span></div>
<div class="am21-home-grid" id="am21HomeCards"></div><article class="card"><h3>Preparation pipeline</h3><div class="am21-pipeline"><span>Raid / Extract</span><b>→</b><span>Organize Loot</span><b>→</b><span>Refine / Research</span><b>→</b><span>Prepare Gear</span><b>→</b><span>Mission Terminal</span></div><p class="small muted">Workflow illustration, not a game-verified recipe graph. Some research/crafting prerequisites are separate or may unlock in different orders.</p><button id="am21HomeTour" type="button">Show quick guided tour</button></article></section>
<section class="section" id="am21signals"><div class="sectionhead"><div><div class="am-subtitle">FIELD RECORD // CASSETTES & AUDIO</div><h2>Signal Archive</h2><p>Music collectibles, player-reported search leads and the guide's independently created instrumental soundtrack. Never confuse cassette recorders with collectible music cassettes.</p></div><span class="pill">LOCATIONS NOT GUARANTEED</span></div>
<div class="am21-columns"><article class="card"><h3>Music collection journal</h3><p>Music cassettes are distinct from cassette recorders required by some objectives. Record personal finds, not claimed guaranteed drops.</p><div id="am21SignalEntries" class="am21-checklist"></div><label for="am21SignalNew">Custom cassette / track title</label><div class="am21-row"><input id="am21SignalNew" placeholder="Track or cassette name as displayed in-game"><button type="button" id="am21SignalAdd">Add</button></div><button id="am21SignalExport" type="button">Export journal JSON</button></article><article class="card"><h3>Community location leads</h3><div id="am21SignalLeads"></div><p class="small muted">These are reports of recorders and other collectibles; no guaranteed spawn, quantity, or song unlock is asserted.</p></article></div>
<article class="card"><h3>Original guide soundtrack · 11 tracks</h3><p>Use the music dock at the bottom of the page to play, shuffle or save the guide's 11 independently synthesized instrumental loops. All playable offline, no autoplay, no subscriptions, no in-game audio samples.</p><button id="am21OpenMusic" type="button">Open music controls</button></article></section>
<dialog id="am21Tour" class="am21-tour"><div class="am21-row"><strong>◈ FIRST DEPLOYMENT</strong><button type="button" id="am21TourClose" aria-label="Close tour">✕</button></div><div id="am21TourBody" class="am21-tour-body"></div><div class="am21-row"><button type="button" id="am21TourBack">← Previous</button><span id="am21TourCount" class="am21-small"></span><button type="button" id="am21TourNext" class="am-action-primary">Next →</button></div></dialog>
<!-- AM21 COMMUNITY EDITION CONTENT END -->
'''
s=s[:idx]+sections+s[idx:]

css='''<style id="am21ThemeAndFeatures">
/* Version 2.1 visual-token layers. UI additions are intentionally isolated. */
body[data-am-theme="soviet"]{--bg:#141912;--panel:#1e281e;--panel2:#29372a;--line:#778b68;--cyan:#c1deb0;--blue:#86aa70;--green:#c5eaa1;--gold:#d7c28a;--red:#e29877;--text:#eef3e2;--muted:#c1ccb6;--am-accent:#a7cb76;--am-glow:#94c36830;background:radial-gradient(ellipse at 80% 0%,#44512e90,transparent 72%),#101810}
body[data-am-theme="monolith"]{--bg:#091421;--panel:#122637;--panel2:#1a3851;--line:#477a98;--cyan:#c1efff;--blue:#8bcced;--green:#b6ebc8;--gold:#f2d2a1;--red:#f09aa5;--text:#eaf8fe;--muted:#b2d1de;--am-accent:#74d3f7;--am-glow:#74d3f733;background:radial-gradient(ellipse at 88% 0%,#19517a9c,transparent 68%),#081421}
body[data-am-theme="containment"]{--bg:#1b1210;--panel:#2a1a17;--panel2:#45231c;--line:#98623f;--cyan:#ffe1b1;--blue:#e69b65;--green:#e0d5a3;--gold:#ffbe70;--red:#ff8074;--text:#fff2e8;--muted:#dcc4b4;--am-accent:#ff9957;--am-glow:#ff885731;background:radial-gradient(ellipse at 90% 3%,#7d2b2199,transparent 70%),#1a100e}
body[data-am-theme="anomalyfield"]{--bg:#09151c;--panel:#0e2730;--panel2:#183543;--line:#378c91;--cyan:#9ffbff;--blue:#5bd7ed;--green:#9af7c9;--gold:#ffdcaa;--red:#ee8ca8;--text:#e9fbfd;--muted:#b4d7da;--am-accent:#62efe6;--am-glow:#67ddeb38;background:radial-gradient(ellipse at 93% 0%,#3d3e8b74,transparent 60%),#08151d}
body[data-am-theme="notebook"]{--bg:#ebe9e2;--panel:#f7f7f2;--panel2:#e6e8e2;--line:#7c9596;--cyan:#205267;--blue:#295a75;--green:#26704c;--gold:#84581f;--red:#a83e38;--text:#172e36;--muted:#415960;--am-accent:#235975;--am-glow:#37678819;background:#f2f0e9;color:#172e36}
body[data-am-theme="notebook"] header,body[data-am-theme="notebook"] nav{background:#dce2deed;color:#142931}
body[data-am-theme="notebook"] .card,body[data-am-theme="notebook"] .am21-hero{box-shadow:0 8px 20px #122e3522}
body[data-am-theme="notebook"] .am-musicdock{background:#ecf0eb;color:#17313a}
body[data-am-theme="notebook"] button,body[data-am-theme="notebook"] input,body[data-am-theme="notebook"] select,body[data-am-theme="notebook"] textarea{color:#12303b;background:#f7f8f3}
body[data-am-theme="notebook"] .am-theme-pill,body[data-am-theme="notebook"] nav button.active{color:#12313d}
.am21-hero{padding:18px 22px;margin:14px 0;background:linear-gradient(120deg,var(--panel2),var(--panel));border:1px solid var(--line);border-radius:14px;display:grid;grid-template-columns:2fr 1fr;gap:16px}
.am21-hero h3{color:var(--cyan);margin:0 0 7px}
.am21-columns{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:15px;margin:15px 0}
.am21-selector{display:grid;gap:6px;align-content:start}.am21-selector label{margin:0}
.am21-checklist{display:grid;gap:7px;margin:12px 0}.am21-checklist label{display:flex;gap:10px;align-items:start;margin:0;padding:10px;border:1px solid var(--line);border-radius:8px;background:var(--panel2);color:var(--text);font-size:.88rem}
.am21-checklist input[type=checkbox]{width:18px;min-width:18px;min-height:18px;height:18px;margin:2px 0}
.am21-row{display:flex;gap:10px;justify-content:space-between;align-items:center;flex-wrap:wrap;margin:9px 0}.am21-row h3{margin:0}.am21-row input{flex:1;min-width:200px}
.am21-grid-2{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:12px 0}.am21-history{display:grid;gap:9px;margin:10px 0}
.am21-record{border-left:3px solid var(--am-accent);background:var(--panel2);padding:10px 14px;border-radius:6px;font-size:.87rem;overflow-wrap:anywhere}
.am21-home-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:12px;margin:15px 0}.am21-home-grid .card{height:100%}
.am21-pipeline{display:flex;gap:9px;align-items:center;flex-wrap:wrap;margin:10px 0 20px}.am21-pipeline span{border:1px solid var(--line);background:var(--panel2);padding:10px;border-radius:8px}.am21-pipeline b{color:var(--am-accent)}
.am21-tour{max-width:min(650px,calc(100% - 24px));border:2px solid var(--am-accent);border-radius:15px;background:var(--panel);color:var(--text);padding:20px;box-shadow:0 30px 80px #000a}.am21-tour::backdrop{background:#000c;backdrop-filter:blur(5px)}
.am21-tour-body{min-height:155px;margin:17px 0}.am21-tour-body h3{font-size:1.2rem;color:var(--cyan)}.am21-tour-body p{line-height:1.6}.am21-small{font-size:.79rem;color:var(--muted)}
#laWorld .la-pin .la-pin-badge,#laWorld .la-pin .la-pin-label{transform:none}#laIsoToggle.active{border-color:var(--am-accent);background:var(--panel2)}
#laViewport{touch-action:none}#laWorld{will-change:transform}
@media(max-width:800px){.am21-hero,.am21-columns,.am21-grid-2{grid-template-columns:1fr}.am21-hero{padding:12px}}
@media(prefers-reduced-motion:reduce){.am21-tour *,#laWorld{transition:none!important}}
</style>
'''
rep('</head>',css+'</head>')

# Layered standalone source modules appended after existing scripts. Keep testable copies in source/.
source=root/'source'/'modules';source.mkdir(parents=True,exist_ok=True)
modules={}
modules['01_core.js']='''/* FIELD OPERATIONS 2.1 / core & persistence — standalone, isolated from legacy state */
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
'''
modules['02_pvp.js']='''/* FIELD OPERATIONS 2.1 / PvP playbook — never changes PvE storage keys */
(function(){'use strict';const A=window.AM21,{$p}= { $p:A.pick },key='am_v21_pvp';
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
'''
modules['03_music_collectibles.js']='''/* FIELD OPERATIONS 2.1 / signal archive; community leads are not guarantees */
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
 $('#am21OpenMusic').onclick=()=>{const dock=$('#amMusicDock');dock.classList.remove('minimized');dock.scrollIntoView({behavior:'smooth',block:'nearest'});$('#amAudioPlay').focus()};
 render();
})();
'''
modules['04_homebase_tour.js']='''/* FIELD OPERATIONS 2.1 / introductory help and homebase */
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
'''
for name,content in modules.items():(source/name).write_text(content)
js='\n'.join(modules.values())
s=s.replace('</body>','<script id="am21CommunityRuntime">\n'+js+'\n</script>\n</body>',1)
p.write_text(s)
print('html bytes',p.stat().st_size,'modules',len(modules),'tracks',len(tracks))
