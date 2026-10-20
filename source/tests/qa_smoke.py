import asyncio, json
from pathlib import Path
from playwright.async_api import async_playwright
HTML=Path(__file__).resolve().parents[2] / 'active_matter_solo_pve_field_guide.html'
async def main():
 async with async_playwright() as pw:
  browser=await pw.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
  page=await browser.new_page(viewport={'width':1440,'height':1000},accept_downloads=True)
  errs=[];page.on('pageerror',lambda err: errs.append(str(err)))
  await page.set_content(HTML.read_text(encoding='utf-8'),wait_until='load',timeout=120000)
  await page.wait_for_timeout(300)
  results=[]
  async def test(name,func):
   try:result=await func();results.append((name,bool(result),str(result)[:160]))
   except Exception as e:results.append((name,False,str(e)[:220]))
  async def check_map():
   await page.locator('button[data-tab="localatlas"]').first.click()
   await page.wait_for_timeout(100)
   return await page.locator('#laIsoToggle').count()==1 and 'rotate(45deg)' in await page.locator('#laWorld').get_attribute('style')
  await test('iso default 45 degrees',check_map)
  async def rotate():
   a=await page.locator('#laWorld').get_attribute('style');await page.locator('#laRotateRight').click();b=await page.locator('#laWorld').get_attribute('style');await page.locator('#laZoomIn').click();c=await page.locator('#laWorld').get_attribute('style');await page.locator('#laIsoToggle').click();d=await page.locator('#laWorld').get_attribute('style');return a!=b and b!=c and 'scale(1.25, 0.825' in c and d!=c
  await test('rotate/zoom/flat',rotate)
  async def maps():
   count=0
   for o in await page.locator('#laMap option').all():
    v=await o.get_attribute('value');await page.locator('#laMap').select_option(v); t=await page.locator('#laTitle').inner_text();assert await page.locator('#laStatus').count()==1 and t.strip() and 'undefined' not in t
    count+=1
   return count==14
  await test('14 maps',maps)
  async def marker_click():
   await page.locator('#laMap').select_option('airport');await page.wait_for_timeout(200)
   await page.locator('#laWorld .la-pin').first.click(force=True)
   return 'Relative coordinate' in (await page.locator('#laDetails').inner_text())
  await test('marker selection after projection',marker_click)
  async def pvp():
   await page.locator('button[data-tab="am21pvp"]').click();await page.locator('#am21PvpRole').select_option('squad')
   await page.locator('#am21PvpPrep input').first.check();await page.locator('#am21PvpNote').fill('test notes')
   await page.locator('#am21PvpAdd').click();return 'test notes' in await page.locator('#am21PvpHistory').inner_text()
  await test('pvp checklist and debrief',pvp)
  async def home():
   await page.locator('button[data-tab="am21home"]').click();return await page.locator('#am21HomeCards .card').count()==6
  await test('homebase',home)
  async def musicloot():
   await page.locator('button[data-tab="am21signals"]').click();await page.locator('#am21SignalNew').fill('My tape')
   await page.locator('#am21SignalAdd').click();return 'My tape' in await page.locator('#am21SignalEntries').inner_text()
  await test('cassette tracker',musicloot)
  async def theme():
   await page.locator('#amThemeSelect').select_option('notebook');return (await page.locator('body').get_attribute('data-am-theme'))=='notebook'
  await test('new theme',theme)
  async def aud():return await page.locator('#amAudioTrack option').count()==11
  await test('11 original music loops',aud)
  async def tour():
   await page.locator('#am21StartTour').click();assert await page.locator('#am21Tour').evaluate('(el)=>el.open')
   await page.locator('#am21TourNext').click();b='2 / 6' in await page.locator('#am21TourCount').inner_text();await page.locator('#am21TourClose').click();return b
  await test('guided tour',tour)
  async def backup():
   await page.locator('button[data-tab="backupcenter"]').first.click();await page.locator('#backupInventory').click();return await page.locator('#backupStats').count()==1
  await test('backup center',backup)
  await page.locator('button[data-tab="localatlas"]').click();await page.locator('#laMap').select_option('airport');await page.screenshot(path=str(Path(__file__).resolve().parents[2]/'previews'/'map_v21_smoke.png'),full_page=False)
  print('TEST_RESULTS',json.dumps(results,indent=2));print('PAGE_ERRORS',errs[:15]);print('PASSED',sum(x[1] for x in results),'of',len(results))
  await browser.close()
asyncio.run(main())
