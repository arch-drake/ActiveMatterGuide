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
