# Active Matter Field Operations — continuation handoff
Updated: 20 October 2026 · Repository: https://github.com/arch-drake/ActiveMatterGuide
Original shipping guide: `active_matter_solo_pve_field_guide.html` (2.1.1)
Shipping offline ZIP: `downloads/Active_Matter_Field_Operations_2_1_1_Community_Edition.zip`
All new changes after that release are **source-only**; do not imply newer tools are inside the old ZIP.

## Owner's priorities and working rules
- Highest priority: **beautiful, sharp, accurate, game-faithful maps** for all 14 views. Correct landmarks, roads, structures, marker positions, and defensible perspective heights. No guesswork.
- Separate exact navigational geometry from cinematic concept art; attractive but incorrect scenery is worse than honest, clear reference material.
- Add original side pictures for creatures, locations, weapons, sleeves, loot and lore. Keep proper concept-art labels.
- Fully offline, no account/subscription, no game memory reading/injection, preserve all saved user progress. Lasagna-style modular changes with focused tests, reversible revisions and no license assumption from public web access.
- Source information may be combined when provenance and patch-specific build are recorded. A Steam community thread was provided: https://steamcommunity.com/app/2887580/discussions/0/569300630414416421/?tscn=1792520295 ; its developer reply has **not** been fetched or permission verified in the tools available.

## Work COMPLETED in source on Oct 20
- `docs/MAP_FIDELITY_MASTER_ROADMAP.md`: whole production lifecycle and honest release gates.
- `docs/AIRPORT_BENCHMARK.md`: benchmark capture, 4+ dispersed FIT, 2+ independent CHECK, 22 legacy Airport marker sample review and vertical-evidence specification.
- `docs/MAP_PRODUCTION_REGISTER.md`: 14 map work queue, real map source requirements and patch issues.
- `map-evidence/map_fidelity_register.v1.json`: 14-map machine-readable registry and **275 historical candidate pins, 0 independently current-verified**.
- `tools/map_reconciliation.html`: dual source-target image physical-landmark calibration (offline), separate heldout check RMS, source crop gate for historical pins, per-marker user review status with source/build/variant evidence, deep link per map, explicit benchmark-readiness indicator. Existing marker coordinates not rewritten.
- `tools/map_fidelity_dashboard.html`: dark themed 14-map QA overview, concept-basemap thumbnails labelled honestly, search/filter, local review counts, links into map workbench.
- `tools/visual_upgrade_2_1_2.html`: public optional offline installer with 32 original editorial concept scenes; original 2.1.1 guide remains intact.
- Updated contributor template, README, landing page, changelog, workflow instructions, release checklist.
- `tests/map_reconciliation_checks.test.cjs`, `tests/map_fidelity_workflow.test.cjs`: existing and added isolated JavaScript deterministic checks passed. Source JS parses, historic 275 count consistent, 4 FIT / 2 CHECK check points succeed, displaced check detected, malformed import and marker review status rejected. This does **not** substitute for full actual browser UI testing.
- Previous local 2.1.2 installer Chromium smoke on earlier 2.0 guide succeeded (20 monster portraits, 14 location images, no page errors). Exact 2.1.1+2.1.2 visual addon structural slots validated; an attempt to upload a combined >8 MB HTML as a single GitHub contents mutation failed and **nothing was published**. The optional installer is the actual delivery path.

## Facts still UNVERIFIED
- All **14** existing illustrated backgrounds are NOT verified in-game basemaps. **0/14** current-game geometry certifications; **0/275** source marker positions independently authenticated with same-build in-game screenshots.
- Gigastructure and Dalniy regional overview lack comparable local coordinate samples; Gigastructure is multi-floor and must not be flattened to a made-up heightmap.
- In-game building heights are unknown unless measured via multiple views or equivalent evidence. Tilted 2D is only pseudo-isometric.
- Official patch 0.4.0.173 relocated stationary extractions in Airport, Headquarters, Downtown. 0.4.0.192 changed Military Base Unstable monster-artifact marker timing and other map behavior.
- Current workbench has not had complete Chrome/Edge manual file-upload and file:// reload, clipboard, export/import or native Windows acceptance. GitHub Pages deployment not proven.
- Do not present third-party map texture republishing as authorized solely because a map is online, depicts the game or a developer commented in a forum.

## NEXT concrete actions
1. Acquire current in-game screenshot or licensed game-map basemap for **Airport**, including exact build, raid variant, dimensions, north/orientation, crop, imagery permission, and 4 FIT + 2 CHECK physical landmarks.
2. Use the upgraded `tools/map_reconciliation.html?map=airport` to align it with its reference, inspect errors and prepare a **truthful** flat map. Review its 22 marker candidates individually; prioritize extraction relocation after 0.4.0.173.
3. From the reviewed geometry, produce sharp faithful 2D and aesthetic map layers; only add actual isometric building heights when supported by source measurements.
4. Repeat for Headquarters, Downtown, then the other 9 local coordinate map views. Handle Gigastructure and Dalniy separately.
5. Run `node tests/map_reconciliation_checks.test.cjs` and `node tests/map_fidelity_workflow.test.cjs` from the repo; then actual browser tests for all maps and old progress preservation.
6. Integrate optional artwork into the tested current guide or continue shipping as local installer; preserve separate originals and route status.
7. Rebuild one verified offline ZIP, update screenshots, changelog, source audit, website; only describe maps as exact after individual evidence/review gates.

Review source truth: `docs/PUBLISH_CHECKLIST.md`, `docs/MAP_WORKBENCH_QA.md`, and `docs/MAP_PRODUCTION_REGISTER.md`.

**Never stop because the task is broad; continue source-supported, low-risk work autonomously. Never claim game-exact map geometry without authentic current reference evidence.**
