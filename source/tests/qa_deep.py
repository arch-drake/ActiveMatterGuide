import asyncio, json, tempfile
from pathlib import Path
from playwright.async_api import async_playwright
html=(Path(__file__).resolve().parents[2] / 'active_matter_solo_pve_field_guide.html').read_text(encoding='utf-8')

async def main():
 results=[]; errors=[]
 async with async_playwright() as pw:
  browser=await pw.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
  page=await browser.new_page(viewport={'width':1365,'height':850},accept_downloads=True)
  page.on('pageerror',lambda e:errors.append(str(e)))
  seed={'activeMatterSoloGuide.v1':json.dumps({'checks':{'legacy_check_protected':True},'quests':[], 'notes':[], 'mapPlans':{}}),'am_stage_progress_v1':json.dumps({'legacy-progress':{'1':True}}),'am_local_atlas_notes_v1':json.dumps({'airport':[{'id':'historic','label':'Historic map pin','x':.51,'y':.49,'category':'note','quality':'user note'}]})}
  await page.evaluate('''(seed)=>{window.__backing={...seed};const local={getItem(k){return Object.prototype.hasOwnProperty.call(window.__backing,k)?window.__backing[k]:null},setItem(k,v){window.__backing[k]=String(v)},removeItem(k){delete window.__backing[k]},clear(){window.__backing={}},key(i){return Object.keys(window.__backing)[i]??null},get length(){return Object.keys(window.__backing).length}};Object.defineProperty(window,'localStorage',{configurable:true,value:local});}''',seed)
  await page.set_content(html,wait_until='load',timeout=120000)
  async def check(name, predicate):
   try:
    val=await predicate(); results.append({'name':name,'pass':bool(val)})
   except Exception as e:results.append({'name':name,'pass':False,'details':str(e)[:300]})
  async def stage1():
   await page.locator('button[data-tab="localatlas"]').click()
   orig=await page.locator('#laWorld').get_attribute('style')
   await page.locator('#laRotateRight').click();r=await page.locator('#laWorld').get_attribute('style')
   await page.locator('#laIsoToggle').click();flat=await page.locator('#laWorld').get_attribute('style')
   await page.locator('#laIsoToggle').click();iso=await page.locator('#laWorld').get_attribute('style')
   await page.locator('#laRotationReset').click();rest=await page.locator('#laWorld').get_attribute('style')
   return 'rotate(45deg)' in orig and 'rotate(60deg)' in r and 'rotate(15deg)' in flat and 'scale(1, 0.66)' in iso and 'rotate(45deg)' in rest
  await check('isometric rotation 45→60→flat15→iso60→reset45',stage1)
  async def views():
   observed=[]
   for o in await page.locator('#laMap option').all():
    val=await o.get_attribute('value');await page.locator('#laMap').select_option(val)
    for view in ['laGrid','laTopo','laDetail','laArt']:
     await page.locator('#'+view).click()
     observed.append((val,view,await page.locator('#laWorld').get_attribute('style')))
   await page.locator('#laGrid').click();return len(observed)==56 and all('transform:' in st for _,__,st in observed)
  await check('14 maps x 4 projections = 56 render checks',views)
  async def marker():
   await page.locator('#laMap').select_option('airport')
   await page.locator('#laWorld .la-pin').first.click(force=True)
   return 'Relative coordinate' in await page.locator('#laDetails').inner_text()
  await check('map marker click after projection',marker)
  async def add_personal():
   await page.locator('#laMap').select_option('gigastructure')
   await page.locator('#laAddNote').click();await page.locator('#laViewport').scroll_into_view_if_needed()
   p=await page.locator('#laViewport').bounding_box()
   page.on('dialog',lambda d:asyncio.create_task(d.accept('Deep QA note')))
   await page.mouse.click(p['x']+p['width']*.5,p['y']+p['height']*.5);await page.wait_for_timeout(200)
   return bool(await page.evaluate('''()=>JSON.parse(localStorage.getItem('am_local_atlas_notes_v1')||'{}')?.gigastructure?.length'''))
  await check('isometric personal marker stored',add_personal)
  async def pvp():
   await page.locator('button[data-tab="am21pvp"]').click()
   await page.locator('#am21PvpRole').select_option('squad');await page.locator('#am21PvpPrep input').first.check()
   await page.locator('#am21PvpNote').fill('<script>unsafe</script> copied from user notes')
   await page.locator('#am21PvpAdd').click()
   stored=await page.evaluate('''()=>JSON.parse(localStorage.getItem('am_v21_pvp'))''')
   return stored['role']=='squad' and stored['prep']['squad-kit'] is True and '<script>unsafe' in stored['history'][0]['note'] and await page.locator('#am21PvpHistory script').count()==0
  await check('PvP separate storage / notes escaped',pvp)
  async def musicloot():
   await page.locator('button[data-tab="am21signals"]').click()
   await page.locator('#am21SignalNew').fill('Live test cassette');await page.locator('#am21SignalAdd').click()
   await page.locator('#am21SignalEntries input').first.check()
   return await page.evaluate('''()=>JSON.parse(localStorage.getItem('am_v21_signals'))?.entries[0]?.collected''')
  await check('cassette journal persists in own key',musicloot)
  async def favorite():
   await page.locator('#am21OpenMusic').click()
   await page.locator('#am21AudioFav').click()
   await page.locator('#am21AudioFavOnly').click()
   await page.locator('#amAudioNext').click()
   return await page.evaluate('''()=>JSON.parse(localStorage.getItem('am_v21_audio_favorites'))?.only===true''')
  await check('music favorites mode',favorite)
  async def theme():
   for opt in await page.locator('#amThemeSelect option').all():
    v=await opt.get_attribute('value');await page.locator('#amThemeSelect').select_option(v)
    assert await page.locator('body').get_attribute('data-am-theme')==v
   await page.locator('#am21Density').select_option('accessible')
   return (await page.locator('body').get_attribute('data-am-density'))=='accessible'
  await check('all 12 themes + density setting',theme)
  async def backup():
   await page.locator('button[data-tab="backupcenter"]').click()
   async with page.expect_download() as d:
    await page.locator('#backupExport').click()
   dl=await d.value
   t=Path(tempfile.mkstemp(suffix='.json')[1]);await dl.save_as(t)
   content=json.loads(t.read_text());t.unlink()
   ks=content.get('keys',{})
   return seed['activeMatterSoloGuide.v1']==ks.get('activeMatterSoloGuide.v1') and all(k in ks for k in ['am_v21_pvp','am_v21_signals','am_v21_atlas_projection','am_v21_audio_favorites','am_v21_ui_preferences'])
  await check('complete backup contains original + new keys',backup)
  async def old_keys():
   now=await page.evaluate('''()=>window.__backing''')
   return all(now[k]==v for k,v in seed.items() if k!='am_local_atlas_notes_v1') and 'Historic map pin' in now['am_local_atlas_notes_v1']
  await check('legacy saved state unchanged',old_keys)
  # title and homebase and tour
  async def home_count():return (await page.locator('#am21HomeCards .card').count())==6
  await check('homebase cards',home_count)
  async def pvp_count():return (await page.locator('button[data-tab="am21pvp"]').count())==1
  await check('new PvP nav tab',pvp_count)
  async def audio_count():return (await page.locator('#amAudioTrack option').count())==11
  await check('11 music options',audio_count)
  print(json.dumps({'passed':sum(r['pass'] for r in results),'total':len(results),'checks':results,'pageErrors':errors},indent=2))
  await browser.close()
asyncio.run(main())
