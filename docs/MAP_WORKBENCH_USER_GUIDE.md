# Active Matter // Map Fidelity Starter Pack (2026-10-20)

This **separate, offline** evidence workbench is an early step toward replacing the conceptual maps in the Field Operations 2.1.1 guide with source-grounded geography. It does **not** replace the full game companion or automatically generate accurate game maps.

## Open and use

1. Extract the ZIP. Open `map_reconciliation.html` in desktop Chrome or Edge; it runs locally with no network.
2. Choose the actual raid map and mode. Enter the current game build number.
3. Upload **your own unedited full in-game map screenshot**. The image stays in this page; only its filename and dimensions are retained in metadata.
4. Choose a recognizable **stable physical landmark** from the dropdown, leave **Independent check point** unchecked, click **Select screenshot position**, then click the landmark in the screenshot. Repeat for at least **three well-separated, non-collinear FIT points**; four or more is preferable. Existing evidence imports remain supported.
5. For at least **two additional landmarks**, check **Independent check point** before clicking the screenshot. These CHECK points are excluded from the fit. Compare **Training RMS** with **Check RMS**; a near-zero training error with a large check error suggests a mismatch, crop/orientation problem, displaced marker, or source error. Neither number independently proves an authentic in-game location.
6. Optionally record building-height evidence from confirmed floor counts, licensed documentation, or multiple in-game screenshots. **Do not invent heights or convert floor counts into meter measurements.**
7. Use **Export map evidence JSON**. Keep the screenshot and evidence together privately; only share screenshots you have rights to share.
8. When reopening, use **Import evidence JSON**. Screenshot pixels are not stored and must be re-uploaded to display.

## Accuracy limitations

- The built-in 275 source-relative marker sample across 12 raid maps is a historical community dataset. Gigastructure and Dalniy Island have no matched coordinate sets in this guide.
- There is **no** verified reproduction of the game's actual icon artwork in this pack. E/T/K/D/Q/P/A/M/C/L/S are guide category codes only.
- Image registration is an affine 2D transform, not a 3D terrain reconstruction. Nonuniform map warping, interiors, multilevel spaces and rotated/mismatched map crops require additional source material.
- Exact building height cannot be derived from a top-down screenshot alone. A future 3D/isometric height layer should only use measured or properly evidenced geometries.
- Entries are candidates for review, not vetted by the game's developers. Game patches and raid modes can change exit locations and marker behavior.

## What to capture for each map

- Full in-game map screen at native resolution, with visible orientation/compass and boundaries, in the intended raid mode/variant.
- A separate legend screenshot showing the actual **icons** for extraction, timed extraction, quests, keys, loot, portals, threats, etc.
- Close-up map crops for areas where labels and building footprints are not legible.
- At least **three distinct ground-level views**, from known directions, of important structures if height and building style are to be modeled.
- Game version, date, source owner, any license/permission, and whether an image is altered or cropped.

## Source and rights notes

Public research leads include [developer patch notes](https://activematter.game/en/news), [Active Matter Wiki](https://activematter.wiki.gg), [Active Matter Help](https://activematterhelp.ru) and [Portal Atlas](https://github.com/rileyedward/portal-atlas/blob/main/docs/data-import.md). Their resources are **not automatically licensed for republication**. Verify ownership, permission, screenshot origin, matching game build, and map variant before distributing any game image or marker collection.

## GitHub publication

The workbench is now **published** at [tools/map_reconciliation.html](https://github.com/arch-drake/ActiveMatterGuide/blob/main/tools/map_reconciliation.html). Once GitHub Pages is enabled its direct interactive link will be https://arch-drake.github.io/ActiveMatterGuide/tools/map_reconciliation.html . It can also be downloaded and opened locally without Pages.

The primary companion and full release ZIP are still required separately in the main repository. Uploading the entire large package ZIP as one item in the root does not extract it or enable an online guide.
### Patch-sensitive control points

Avoid using extraction portals, timed exits, enemy/anomaly spawns, or other moving map symbols as alignment controls. Prefer a fixed structure visible in both source and game screenshots. The historical community marker layer includes some marker types that are not immovable landmarks.

**5 Oct 2026 — build 0.4.0.173:** stationary extraction points shifted in Headquarters, Airport and Downtown. **30 Sep 2026 — build 0.4.0.163:** Dalniy Island extraction changes were also recorded. Check a current raid rather than trusting those old coordinates. The independent validation check catches some mismatches but cannot turn an old or incorrectly matched image into verified game geography.

Patch references: https://activematter.game/en/news/349 and https://activematter.game/en/news (0.4.0.163).

**Release note:** GitHub's `tools/map_reconciliation.html` includes independent check points as of the 20 October source update. The previously packaged 2.1.1 ZIP may predate this update; use the latest GitHub source for the new validation controls.

## New: dual-image physical-landmark workflow (20 October 2026 source revision)

1. Export your map evidence JSON before switching game builds or crops.
2. Select the map, target raid variant/build and provenance. Upload the original current in-game overhead screenshot as **target**.
3. Upload a separate reference basemap under **Fixed physical landmarks**. This source can be an owner's screenshot or a source whose display/use rights are documented; it is loaded locally.
4. Enter a physical landmark name. Mark a FIT point (uncheck Independent check) and click **Match fixed landmark**. Click the identical feature first in the reference image and then in the target screenshot. Add **at least four** spaced FIT landmarks, then switch to CHECK and record **two** geographically separated holdouts.
5. Inspect training/holdout RMS and manually examine geometry. If only three points train, the fit may conceal severe errors.
6. If the reference image is **not exactly the same coordinate crop/orientation as the historic community marker dataset**, leave the **same legacy crop** checkbox unchecked. Historic source marker pins are intentionally hidden during manual-coordinate calibration in that case.
7. Export JSON and store capture version, source URL, rights and crop separately. No screenshot image bytes leave the browser via this tool.

A correctly aligned reference screenshot does not validate extraction-point permanence, current loot, real building height or game-variant correctness. Gigastructure and Dalniy support manual landmark calibration even though they have no legacy per-raid candidate pin set; regional/floor-level coordinate systems must be documented explicitly.

**Status:** geometry and import-validation checks pass; manual file-picker and Windows file:// workflow require interactive browser testing before this release can be certified.

## Verified screenshot viewer integration

Use [Reference Atlas](../tools/map_reference_atlas.html) to display your local image, pan and zoom, search historic source markers and inspect source/variant links. The visual viewer now blocks projection of candidate pins unless imported map-specific workbench JSON contains **at least four FIT and two independently excluded CHECK controls**, a six-coefficient affine matrix, the exact screenshot filename and native dimensions, matching game build/play mode/raid variant, and compatible marker-coordinate crop. New workbench exports additionally record a local SHA-256 digest when supported; historical exports without hashes require explicit identity confirmation. **Do not assume calibration quality certifies extraction state**; all pins remain candidate positions and are not silently written back to the shipping guide.

### Practical use order
1. In Workbench: select raid and its exact variant, set build/mode, upload the target screenshot, import a source reference, and record at least four fixed physical FIT landmarks and two independent CHECK landmarks.
2. Review independent-check residuals and source crop; set identical-legacy-crop confirmation **only** if measured from source metadata. Export JSON after screenshot hash finishes.
3. In Reference Atlas: select the same map/variant and build/mode, upload the **exact same target screenshot**, then its matching evidence JSON. Resolve any identity or coordinate warning.
4. Explicitly enable provisional marker overlay, inspect physical landmarks and patch-sensitive exits. Do not publish a corrected pin without current gameplay validation.

Image pixels stay local. This is a companion to the existing single HTML guide, not a replacement for verified shipped basemaps.
