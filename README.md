# ACTIVE MATTER // FIELD OPERATIONS — Community Edition

![Field Operations map interface](previews/map_v21_smoke.png)

**Version:** 2.1.1 · **Updated:** October 20, 2026 · **Status:** free community download available; GitHub Pages setup pending

> Independent fan-made reference tool. Not affiliated with or endorsed by the Active Matter developers. It does not read, alter, inject into, or automate the game.

**Open immediately:** [Launch the guide](./active_matter_solo_pve_field_guide.html) by downloading and opening the HTML, or [download the complete ZIP](./downloads/Active_Matter_Field_Operations_2_1_1_Community_Edition.zip). Once GitHub Pages is enabled, the site landing page (`index.html`) also provides a browser launch option.

## Support the guide

The project is free and always optional to support: [☕ Buy Me a Coffee](https://buymeacoffee.com/elderdrake). No subscriptions or donation-gated features.

## Instructions for players

**[Read the full player guide](docs/PLAYER_GUIDE.md)** for installation, PvE and PvP, rotating maps, collectibles, backup/restore, and troubleshooting.

## What it does

- **14 interactive maps** with flat and pseudo-isometric viewing, rotation, zoom and manual map notes; 12 with limited community-derived coordinate markers.
- **PvE and optional PvP:** Solo/Team PvE checklists, a separate Open Solo/Squad PvP field log, route planning and investigation progress.
- **20 monster/anomaly dossiers**, 53 curated investigation chains with 217 documented criteria (coverage is **not** guaranteed exhaustive).
- **Signal Archive:** personal music collectible field journal, cited community location leads and 11 original synthesizer tracks.
- **12 themes**, guided tour, Homebase explainer, quick navigation and exportable browser-local backups.
- **Fully offline gameplay companion:** no login, subscription, overlay, game-memory inspection or mod installation.

## Quick start

1. Download and extract the [complete ZIP](./downloads/Active_Matter_Field_Operations_2_1_1_Community_Edition.zip).
2. Open `active_matter_solo_pve_field_guide.html` in Chrome, Edge or another modern browser.
3. Choose your mode and explore. Ctrl+K opens the guide search.
4. Before updating or moving the HTML, **Backup → Export complete backup** and keep that JSON file safe. Browser `file://` storage can vary by path and browser.

> **Maps are not guaranteed 1:1 game geography.** Artwork is original illustrative scenery; community-sourced coordinate markers have their own provenance. The isometric tilt is a 2D projection, not measured elevation. A same-crop current in-game screenshot plus verified permissions is required for game-exact rendering. See [map accuracy notes](docs/MAP_PROVENANCE_AND_ACCURACY.md).

## Map Reconciliation Workbench — screenshots first

**[Open the updated Map Reconciliation Workbench source](tools/map_reconciliation.html)** · [How to use it](docs/MAP_WORKBENCH_USER_GUIDE.md) · [QA report](docs/MAP_WORKBENCH_QA.md)

This free, offline companion utility aligns **your own current in-game screenshots** to 275 historic community marker samples. It records **fit points and independent held-out check points**, computes separate 2D alignment-error estimates, and exports local evidence JSON without uploading screenshots. It does not automatically produce game-exact terrain, actual game icon graphics, or building heights. **The October 20 source update is newer than the packaged 2.1.1 ZIP; the ZIP may contain the older workbench.** See [map evidence requirements](docs/MAP_FIDELITY_EVIDENCE.md).

## Share & contribute

Found a wrong loot lead, a missing monster behavior, a broken control or a patch change? Open a GitHub **Issue** using the templates in `.github/ISSUE_TEMPLATE/`. Include the current game patch, mode/variant, map, and evidence when you can. See [CONTRIBUTING.md](CONTRIBUTING.md).

**Please do not post personal browser backup files, authentication tokens, game account credentials or copyrighted in-game map textures in issues.**

## Development and testing

Development follows a layered *lasagna architecture*. New UI/features/persistence logic live in focused `source/modules/` files; a bundled single HTML is shipped for easy offline use. See [developer notes](source/README_DEV.md) and [2.1 QA report](docs/TEST_REPORT_2.1.md). The automated browser tests use in-memory browser storage, **not actual `file://` persistence**; testers should verify backups manually.

## Credits and rights

- Active Matter is the intellectual property of its respective creators and publisher.
- Music in this project was procedurally synthesized for this guide; see [audio permissions](docs/ORIGINAL_AUDIO_PERMISSIONS.md).
- Original tactical artwork is **not official game imagery**. Coordinate sample provenance and third-party map-data considerations: [map source notes](docs/MAP_PROVENANCE_AND_ACCURACY.md).
- No general software license has been selected for the source repository yet. Public visibility does not automatically grant permission for reuse; see [RIGHTS_AND_ATTRIBUTION.md](RIGHTS_AND_ATTRIBUTION.md).

[Release notes](docs/CHANGELOG_2.1.md) · [Full offline ZIP](downloads/Active_Matter_Field_Operations_2_1_1_Community_Edition.zip) · [Steam community discussion](https://steamcommunity.com/app/2887580/discussions/0/569300630414416421/)
