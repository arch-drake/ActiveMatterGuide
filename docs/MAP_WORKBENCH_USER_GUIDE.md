# Active Matter // Map Fidelity Starter Pack (2026-10-20)

This **separate, offline** evidence workbench is an early step toward replacing the conceptual maps in the Field Operations 2.1.1 guide with source-grounded geography. It does **not** replace the full game companion or automatically generate accurate game maps.

## Open and use

1. Extract the ZIP. Open `map_reconciliation.html` in desktop Chrome or Edge; it runs locally with no network.
2. Choose the actual raid map and mode. Enter the current game build number.
3. Upload **your own unedited full in-game map screenshot**. The image stays in this page; only its filename and dimensions are retained in metadata.
4. Choose a recognizable static community-source landmark from the dropdown, click **Select screenshot position**, then click that landmark's position in the image. Repeat at least **four or five** well-spaced points. Three can produce a fit, but three alone cannot independently validate it.
5. Review predicted overlay pins and the RMS misalignment. A low RMS doesn't prove authenticity; deliberately cross-check landmarks that were **not** used to calibrate.
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