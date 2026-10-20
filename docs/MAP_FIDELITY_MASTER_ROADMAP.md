# Active Matter — map fidelity master roadmap
Status: **in execution** · Owner priority: maps > marker reconciliation > presentation > editorial art
Baseline: Field Operations 2.1.1; current build date 2026-10-20
Companion: [Airport benchmark](AIRPORT_BENCHMARK.md) · [14-map production register](MAP_PRODUCTION_REGISTER.md) · [source/rights audit](MAP_ADOPTION_AND_VISUAL_EVIDENCE_2026_10_20.md)

## Definition of fidelity
A beautiful concept map is not a verified navigational map. We retain two explicitly distinguishable views:
- **Reference (flat)**: true north and authentic same-build map crop; only measured road/shore/structure outlines, named POIs and attributed, reviewed marker positions.
- **Enhanced (editorial)**: readable shaded/outlined version of **that same verified geometry**. Optional perspective and building volumes can only use confirmed footprints and height evidence. No invented floor counts, terrain, road links or placements.

Each marker carries map, mode/variant, build, source, image crop, alignment, verification date, source status and patch sensitivity. Historic coordinates are *candidates* until reconciled; a tight affine RMS alone does not verify in-game behavior.

## Delivery phases
### P0 — integrity & source review (required for all 14)
- Inventory all basemaps, marker datasets, image rights, release and build; hash each reference image.
- Record original publisher artwork vs third-party annotation separately. Public access, attribution or Steam engagement by developers is **not** automatically a reusable license. Store exact permission / platform policy before publishing copied basemaps.
- Keep published 2.1.1 guide intact until changed builds pass regression tests; export any prior browser progress first.
- Distinguish 12 local coordinate maps from two conceptual-only views (Gigastructure and Dalniy).

### P1 — Airport reference benchmark
- Obtain current in-game overhead screenshot(s), native pixel dimensions, north/up orientation, raid mode, crop, game build, and any credited licensed copy.
- Manually identify stable physical landmarks on both reference and historic coordinate source: at least **four geographically dispersed FIT** controls and **two independent CHECK** controls. Avoid extraction/anomaly/spawn symbols as calibration anchors.
- Preserve source and fitted coordinates separately; explicitly report fit RMS, holdout RMS, out-of-bounds, and residual conflicts. Investigate failures rather than repositioning markers silently.
- Draw buildings, hangars, runways, service roads, terrain and hard map boundaries **only where the screenshot supports them**. Do not invent roof shapes or elevations.
- Review all **22 Airport legacy candidate markers**, especially relocated exits after 0.4.0.173. Each is: current-confirmed / outdated / conflicting / unverified.
- Confirm visually with browser screenshot at normal and 200% zoom, then in an actual game build for player-facing marker claims.

### P2 — other local raids
- Run the identical protocol on Headquarters (21), Downtown (29) and then the nine remaining local datasets; scope and outstanding QA tracked in the [production register](MAP_PRODUCTION_REGISTER.md).
- Patch-sensitive changes in 0.4.0.173, 0.4.0.192 and subsequent updates supersede older pins and route claims.
- No use of a marker percentage across different map crops without an explicit, tested conversion.

### P3 — visual finish, without misrepresentation
- Reuse the verified flat map geometry to produce consistent high-resolution rendered layers; two-tier zoom textures, sharp text, readable night-mode contrast, clear icons and legend, optional uncluttered markers and filters.
- Isometric scene geometry only for measured building footprints and heights, with unknown-height structures rendered flat. Annotated 2D tilt must remain labelled pseudo-isometric.
- Layer location/creature/loot/sleeve/weapon concept illustrations in **editorial panels** with captions, not under live marker pins.
- Preserve accessibility: keyboard, high contrast, reduced motion, hover/focus tooltips, screenreader statuses, no flashing overlays.

### P4 — QA, distribution & release
- Run current deterministic geometry tests, manual fit/holdout rejection tests, full browser interactions, 14-map selector checks, marker filter and popup tests, backup/export/restore checks, security tests for imported JSON, and file:// Windows smoke test.
- Compare current shipping ZIP against *verified built source*, record asset hashes, update changelog and previews, then publish the ZIP.
- Only promote a location's status to VERIFIED after real screenshots, source permission, marker evidence, visual review and signoff. Mark all other views ARTISTIC or COMMUNITY CANDIDATE.

## Review gates / measurable metrics
| Gate | Acceptance evidence | State (20 Oct) |
|---|---|---|
| G0 Rights & version | documented source/capture and build per map | OPEN |
| G1 Geometry | current same-crop in-game screenshot and traced physical geometry | OPEN |
| G2 Calibration | >=4 spaced FIT and >=2 independent CHECK; RMS recorded | OPEN |
| G3 Markers | per-marker status & variant, stale exits highlighted | OPEN |
| G4 Heights | verified structure measurements/multi-views or omit volumes | OPEN |
| G5 QA & release | browser regression + personal backup compatibility + audited release | OPEN |

Performance targets are proposed UX goals, **not** measurements: map switch responsive on midrange PC, smooth pan/zoom, source layer legible at 200% zoom. A numerical fit/error **threshold** must be agreed against screenshot pixel scale and error budget; no invented absolute threshold or automatic “verified” promotion.

## Reproducibility / architecture
Lasagna layers: evidence schema → validation → geometry calibration → marker reconciliation → rendering → export/persistence → tests. Each slice can be tested independently; never couple imported source evidence to guide's saved progress keys.

## Source pointers
- Official 0.4.0.173: https://activematter.game/en/news/349
- Official 0.4.0.192: https://activematter.game/en/news/356
- Community map archive: https://activematter.guide/maps/
- Airport summary: https://activematterhelp.ru/guide/map-aeroport
- Original Steam discussion, linked by project owner (developer reply unverified in this environment): https://steamcommunity.com/app/2887580/discussions/0/569300630414416421/?tscn=1792520295

## Nonnegotiable honesty
**0/275 legacy markers authenticated against current in-game screenshots in this repo's audit.** Existing 14 picture basemaps are original illustrations, not current game geography. Work on these gates can proceed immediately; claiming all maps exact cannot.
