/* Offline local link and release entry checks; external hosts tested separately. */
'use strict';
const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path');
const root=path.resolve(__dirname,'..');
const files=['README.md','README_START_HERE.md','index.html',
  'docs/PLAYER_GUIDE.md','tools/all_maps_live_reference.html',
  'docs/ALPHA_RELEASE_NOTES.md','OWNER_PUBLICATION_STEPS.md',
  'docs/PUBLISH_TO_GITHUB.md','docs/UPLOAD_RELEASE_2_1_1.md'];
let count=0;
function check(file,raw){
  const target=decodeURIComponent(raw.trim().split(/[?#]/)[0]);
  if(!target||/^(https?:\/\/|mailto:|javascript:|data:|blob:|\/)/i.test(target))return;
  const targetFile=path.resolve(root,path.dirname(file),target);
  assert(targetFile.startsWith(root+path.sep),'Link escapes project: '+file+' '+raw);
  assert(fs.existsSync(targetFile),'Broken local link '+file+' '+raw);
  count++;
}
for(const file of files){
  const body=fs.readFileSync(path.join(root,file),'utf8');
  for(const match of body.matchAll(/(?:href|src)=["']([^"']+)["']/g))check(file,match[1]);
  if(file.endsWith('.md'))for(const match of body.matchAll(/\]\(([^)\n]+)\)/g))check(file,match[1]);
}
const homepage=fs.readFileSync(path.join(root,'index.html'),'utf8');
const readme=fs.readFileSync(path.join(root,'README.md'),'utf8');
assert(homepage.indexOf('Explore Source Atlas')<homepage.indexOf('Open offline field companion'));
assert(readme.includes('GitHub Pages is not yet enabled'));
console.log('PASS alpha links: '+count+' local links resolve; online site described truthfully');
