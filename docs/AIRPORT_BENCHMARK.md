# Airport — faithful map benchmark (not yet game-exact)
Priority **P0 / active benchmark**, as of 2026-10-20. Companion [master roadmap](MAP_FIDELITY_MASTER_ROADMAP.md).
Map identifier `airport` · **22 sampled candidate markers** · no approved authoritative basemap in repository · verified current markers: **0/22**.

## Confirmed context (NOT coordinates)
Airport is a Central Africa raid featuring hangars, service roads and a passenger aircraft caught in a gravity anomaly. Do not confuse it with northern Dalniy Island's Soviet airfield. Community guide: https://active-matter.wiki/maps/airport/. Official patch 0.4.0.173 **moved stationary exits nearer buildings and added cover**, and adjusted Airport Devourer spawn locations: https://activematter.game/en/news/349.

## Authentic overhead map reference found (20 October)
- [Airport Active Matter Help entry](https://activematterhelp.ru/wiki/maps/africa_airport) publicly embeds a genuine-looking tile-based overhead basemap as a raster pyramid; [regional map explorer](https://activematterhelp.ru/maps?map=forsaken_africa) also has the broader Forsaken Africa reference.
- Example source tile: https://activematterhelp.ru/map-tiles/forsaken_africa_tiles/3/4/5.webp . Adjacent tiles share roofs, roads, vegetation and terrain at identical scale; source tile bounds/zoom/projection and the Airport raid crop **have not been calibrated**. They must not be treated as 22-pin coordinate correspondence yet.
- The wiki reports **8 permanent, 11 timed and 1 final exit** in its Airport reference, whereas the guide's historic **22 sampled markers are all types combined**. This signals undercoverage, not a contradiction about total exit count. PvE/Open distinction needs independent checking before publishing.
- See [detailed source audit](AUTHENTIC_MAP_TILE_SOURCE_DISCOVERY.md). External image rights and rehosting permission remain to be reviewed.

## Input capture specification
| Field | Required value / safeguard |
|---|---|
| Map/build/variant | Airport, actual game build, mode/variant (Isolated PvE vs Open) and date |
| Input | full original PNG/WebP screenshot of game's 2D map, at native resolution, unmagnified; do not strip compass or labels before recording |
| Crop/orientation | screenshot pixels W×H, image crop rectangle, north angle, whether the in-game map zoomed |
| Source provenance | author's original screenshot / page URL, creator/rights holder, license or explicit publication permission |
| Fixed geometry | hangar corners, runway intersection, hard compound edges, service roads, named junctions, aircraft/bubble outline where actually discernible |
| Vertical claims | separate oblique same-build shots, verifiable height source, measured vs estimated; otherwise `height: null` |

## Calibration and controls
1. Start with accurate flat screenshot; no pre-smoothing that alters geography.
2. Select **at least four** spatially spread fixed FIT landmarks (at most one per cluster) plus **two independently selected** CHECK landmarks. Record exact pixels / normalized percentages and labels.
3. Fit only FIT points; report fit RMS, held-out RMS (in percent and pixel equivalent), screenshot size, transform parameters, outliers and uncovered source area.
4. If CHECK controls conflict, return to crop/orientation/source version and inspect; **do not adjust E/T exit pins or locations to make a fit appear better**.
5. For each candidate map POI record a decision with screenshot evidence and version, never overwrite original source coordinates.
6. Make only two released visual outputs: a reference flat layer backed by actual image/geometry and an editorial enhancement derived from that same geometry.

## Landmark and POI evidence worksheet
| Feature | Expected relationship | Verification result |
|---|---|---|
| Hangar clusters | visually distinctive group, exact footprint and number unknown until sourced | NEED IMAGE |
| Airport apron/runway | continuous surface and recognizable junctions | NEED IMAGE |
| Suspended passenger aircraft / gravity zone | landmark, may be above/below other playable geometry | NEED IMAGE |
| Service roads/compound edges | must be traced from game capture, not guessed | NEED IMAGE |
| Extraction points (6 legacy candidate E/T symbols in older audit) | **changed by 0.4.0.173**; event-specific states separately | PATCH-SENSITIVE |
| Investigations, loot, anomalies | source-led, evidence tags and raid-variant conditions | NEED REVIEW |
| Multi-level routes | top-down overlap alone cannot establish floor/height | UNKNOWN |

**Note:** airport has 22 limited source-sample records, not all POIs. The independent source website lists more markers and modes; do not confuse their totals with the 22 internal historic samples.

## Acceptance checklist (Airport)
- [ ] Current licensed/permissioned game map capture and build.
- [ ] Crop + orientation + SHA256 + landmark manifest committed (no personal information).
- [ ] Four dispersed FIT plus two independent CHECK; residual report saved.
- [ ] Flat basemap uses verifiable roads, runway, roofs, boundaries without invented detail.
- [ ] Every one of 22 candidate pins reviewed and annotated with source/mode/patch status.
- [ ] Extraction marker positions validated post-0.4.0.173.
- [ ] Independent comparison against another trusted same-build source.
- [ ] Building elevations omitted until evidence exists; isometric render visually checked.
- [ ] Browser regression (modes, 200% zoom, click targets, keyboard, exports).
- [ ] Windows file:// and backup/restore smoke test; release signoff.

## Evidence files structure (suggested)
`map-evidence/airport/manifest.json` and `reviewed/*.json` contain metadata only. Do NOT check raw copyrighted captures into a public repo until publication rights are established. Raw files may remain in the owner's offline private workspace. PNG map export must be permission reviewed.

## Failure / rollback
If sources disagree, keep prior illustration and label as not navigational; hide or flag disputed candidate pins, never silently substitute. Release only audited individual maps, not a blanket 14-map accuracy claim.
