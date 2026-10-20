# Map fidelity program — 2.1.1 evidence gate

**The 14 included tactical backgrounds are illustrations, not game screenshots.** Rotation is a 2D pseudo-isometric transform, not a height-aware reconstruction. Accurate buildings and pin icons must follow source images and alignment testing.

## Source evidence needed for each map
1. Current game build and raid mode/variant, with north/orientation and cropping consistent between screenshots.
2. Full in-game map screen, preferably at native resolution, and close-ups of named regions.
3. In-game pin legend/icons and dynamic-spawn state differences.
4. For correct 3D heights: multiple photographed angles or other licensed height references. An overhead screenshot alone cannot determine height.
5. Rights to reuse or transform the source imagery, or user's own screenshots.

## Reconciliation process
- Start with flat game reference and a manifest of source image SHA256 + crop/orientation.
- Match at least 3 non-collinear control points; more landmarks reduce ambiguity. Compute map-to-image transforms explicitly, log residuals, flag conflicts; do not shift pins by guesswork.
- Reconcile each marker by category, exact in-game icon artwork (when legally usable), coordinates, variant, source, verification date, and game build.
- Maintain real height only if measured/verified; show unknown structures flat instead of fabricating heights.
- Regression-test pan/zoom/rotation and marker clicks; preserve local notes and all storage keys.

## Map status (14)
| Map | Geography | Height | Marker verification |
|---|---|---|---|
| Airport | Concept art | Unknown | Community references only |
| Cargo Port | Concept art | Unknown | Community references only |
| Dam | Concept art | Unknown | Community references only |
| Dogorsk | Concept art | Unknown | Community references only |
| Downtown | Concept art | Unknown | Community references only |
| Factory | Concept art | Unknown | Community references only |
| Headquarters | Concept art | Unknown | Community references only |
| Military Base | Concept art | Unknown | Community references only |
| Ozernoe | Concept art | Unknown | Community references only |
| Park | Concept art | Unknown | Community references only |
| Scrapyard | Concept art | Unknown | Community references only |
| Shegolskoe | Concept art | Unknown | Community references only |
| Gigastructure | Concept art | Unknown | No verified in-guide coordinate layer |
| Dalniy Island | Regional conceptual view | Unknown | No verified local layer |

Potential evidence: official patch notes https://activematter.game/en/news; source provenance https://github.com/rileyedward/portal-atlas/blob/main/docs/data-import.md. Do **not** redistribute copyrighted game/community maps without permission.

## Live-build accuracy gate — October 2026

Official notes document that several extraction positions changed after the historic marker sampling:

- [Update 0.4.0.163](https://activematter.game/en/news): extraction points around Dalniy Island shifted (30 September).
- [Update 0.4.0.173](https://activematter.game/en/news/349): stationary extraction points in Headquarters, Airport and Downtown moved near new cover (5 October).
- [Update 0.4.0.192](https://activematter.game/en/news/356): Military Base: Unstable Zone monster-artifact marker timing changed (15 October); dynamic indicators should not be treated as fixed landmarks.

**Rule:** Mark E/T extraction and dynamic anomaly markers as patch-sensitive by default. Never transform one historically sourced marker into a verified current marker solely because it participates in a low-error affine fit. Use FIT/CHECK role separation, independent screenshots of physical structures, and current mode/build-specific evidence. Building heights require multi-angle or licensed measured data. Do not replace the 14 illustrated backgrounds with guessed geometry.

The standalone workbench source now supports independent check points and export metrics. It remains a preparation tool; neither the current 2.1.1 release ZIP nor these automated tests establish game-exact geography.
