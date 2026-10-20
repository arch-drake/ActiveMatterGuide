/* Offline deterministic check suite for the Map Reconciliation Workbench.
 * Run: node tests/map_reconciliation_checks.test.cjs
 * No game access, screenshot uploads or network needed.
 */
'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const html = fs.readFileSync(path.join(__dirname, '..', 'tools', 'map_reconciliation.html'), 'utf8');
const first = html.indexOf('function linearSolve(');
const last = html.indexOf('function refreshOptions()', first);
assert(first >= 0 && last > first, 'Geometry module must remain discoverable in workbench');
const geom = new Function(html.slice(first,last) + ';return {linearSolve,affineFit,project,evaluateAlignment};')();
function control(x,y,i,role='fit') {
  return {id:String(i),x,y,u:.7*x+.1*y+4,v:-.05*x+.8*y+3,role};
}
const points = [
  control(5,8,0), control(91,11,1), control(7,94,2),
  control(88,87,3,'check'), control(37,45,4,'check')
];
const perfect = geom.evaluateAlignment(points);
assert(perfect.candidate, 'Must produce candidate');
assert.equal(perfect.training.length,3);
assert.equal(perfect.checks.length,2);
assert(perfect.candidate.rms<1e-7,'Fit should match manufactured transform');
assert(perfect.checkRms<1e-7,'Independent checks should agree with correct transform');
const bad = points.map(x=>({...x}));bad[4].u+=8;
assert(geom.evaluateAlignment(bad).checkRms>5,'Independent check must reveal displaced source');
assert.equal(geom.evaluateAlignment(points.slice(0,2)).candidate,null,'Two fit points insufficient');
assert.equal(geom.evaluateAlignment(
  [control(0,0,0),control(10,10,1),control(20,20,2)]
).candidate,null,'Collinear fit points must be rejected');
const legacy=points.map(({role,...p})=>p);
assert(geom.evaluateAlignment(legacy).candidate,'Legacy anchor records without role remain compatible');
console.log('PASS map QA: exact affine fit, separate heldout RMS, moved check, underdetermined/collinear rejection, legacy imports');
