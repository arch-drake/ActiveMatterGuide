# Map marker reconciliation register — 20 October 2026

## Audit scope and interpretation

The guide's historic community-relative marker samples form a **candidate layer**. Percent coordinates cannot be called verified or game-exact until aligned with an authentic **same-build, same-mode, same-orientation** in-game screenshot. Counts below describe the workbench's embedded sample, not independently confirmed locations. **Source image rights/redistribution permissions must be checked separately.**

| Raid | Sample markers | Extraction codes E/T | Patch-sensitive candidates (E/T/M/A) | Particular caution | Game-reference QA |
|---|---:|---:|---:|---|---|
| Airport | 22 | 6 | 11 | 0.4.0.173 extraction shifts | Unverified |
| Headquarters | 21 | 7 | 7 | 0.4.0.173 extraction shifts | Unverified |
| Downtown | 29 | 5 | 7 | 0.4.0.173 extraction shifts | Unverified |
| Dam | 21 | 6 | 8 | Check mode/build | Unverified |
| Cargo Port | 29 | 5 | 6 | Check mode/build | Unverified |
| Factory | 27 | 5 | 8 | Check mode/build | Unverified |
| Dogorsk | 25 | 8 | 10 | 0.4.0.192 extraction scenery bug fixed | Unverified |
| Military Base | 20 | 5 | 8 | 0.4.0.192 artifact display timing | Unverified |
| Ozernoe | 20 | 7 | 9 | Check mode/build | Unverified |
| Park | 22 | 6 | 10 | Check mode/build | Unverified |
| Scrapyard | 13 | 2 | 5 | Check mode/build | Unverified |
| Shegolskoe | 26 | 4 | 6 | Check mode/build | Unverified |
| **TOTAL** | **275** | **66** | **95** | | **0/275 authenticated** |

Conceptual overviews (no comparable coordinate sources in this build): **Gigastructure**, **Dalniy Island**. The guide additionally contains polygon shapes (74 listed in the 2.1.1 packaging audit); polygons do **not** establish real roads, building footprints or 3D elevations.

## Roadmap: screenshot → measurement → terrain → isometric

1. **Airport benchmark:** obtain the current build, full north-oriented in-game map screenshot and legend. Capture four or more well-spaced stable physical landmarks as FIT points, and two additional landmarks as CHECK points. Record patch, mode, rights and screenshot crop. Historical extraction markers are not preferred FIT controls.
2. Align the source reference, document independent check error, visibly review other POIs, and record each correction with source/version/variant. If checks disagree, do not draw new geography or move points silently.
3. Build a **faithful flat base first**, tracing only visible licensed/reference road edges, footprints, shorelines and named structures. Keep unknown areas unrendered or clearly labelled provisional. Never invent floor counts.
4. Collect multiple licensed/permissioned oblique views for 3D building volumes; apply height only where measured/confirmed. Isometric *tilt* is not a substitute for actual elevation.
5. Repeat for remaining raids; verify marker display in Solo/Team PvE and the relevant Open/Unstable variant separately. Retest modes after relevant official game patches.

## Latest official change notices affecting use

- [September 30 (0.4.0.163)](https://activematter.game/en/news): Dalniy Island extraction cover and position changes.
- [October 5 (0.4.0.173)](https://activematter.game/en/news/349): extraction relocations in Airport, Headquarters and Downtown.
- [October 15 (0.4.0.192)](https://activematter.game/en/news/356): Military Base Unstable monster-artifact marker appears earlier; several map environment fixes.

## Evidence gate

**Current state:** Original illustrated basemaps only; zero authentic user-provided same-crop map screenshots have been processed in this workbench review. Synthetic fits and check-point tests validate the mathematics, not the game map. Do not claim the 14 visuals are game-exact or that all 275 marker placements are verified.

Links: [Map workbench](../tools/map_reconciliation.html) · [Usage](MAP_WORKBENCH_USER_GUIDE.md) · [QA notes](MAP_WORKBENCH_QA.md) · [Fidelity standard](MAP_FIDELITY_EVIDENCE.md).
