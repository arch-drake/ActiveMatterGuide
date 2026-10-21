# Authentic geography source discovery (20 October 2026)
Status: **usable as external reference, not locally redistributed** · [master roadmap](MAP_FIDELITY_MASTER_ROADMAP.md)

## What was actually inspected
The community Active Matter Help wiki embeds a game-derived raster **tile pyramid** on its public map pages, as opposed to the Field Operations guide's invented scenery.

- Airport overview: https://activematterhelp.ru/wiki/maps/africa_airport
- Multi-region interactive atlas: https://activematterhelp.ru/maps?map=forsaken_africa
- Example actual overhead raster tile: https://activematterhelp.ru/map-tiles/forsaken_africa_tiles/3/4/5.webp
- Adjacent verified URLs: `/map-tiles/forsaken_africa_tiles/3/5/5.webp`, `/3/4/6.webp`, `/3/5/6.webp`
- The tiles show consistent roads, roofs, shorelines, green areas, and other authentic-looking geography. They are **part of a larger overview**; a 2×2 sample is not the full map nor a verified playable Airport raid boundary.
- The public site also includes alternative "Main Map (3D)", HQ/Forsaken Africa, Abandoned America, and Gigastructure map categories. The original guide treats Dalniy as a regional view, not a single local raid.
- A separate atlas `https://activematter.guide/maps/` currently advertises 3,222 marker records for Main Map (Dalniy), 1,669 for HQ/Forsaken Africa, 360 for Abandoned America and 6 for Bunker (site-level advertised counts, not audited entries). Our 275 sampled coordinates are **not an exhaustive import**.

## Critical coordinate issue
These game-derived tiles use **tiled x/y/zoom coordinate space** with an unknown crop-to-raid transformation, whereas our guide samples use percentages of a historic source image with unknown orientation/crop. Do not directly place an old pin at matching normalized percentages of these tiles. A source tile number is **not** an in-game meter coordinate.

To construct faithful Airport geometry from the tiles, first obtain:
1. the full tile pyramid metadata or its source projection, bounds, region extent, x/y order, and zoom convention;
2. the precise Airport raid crop/extent and variant; and
3. at least four physical landmarks (FIT) and two withheld landmarks (CHECK), calibrated with the source screenshot. Then cross-check 22 historic pins against the October 5 patch.

Always preserve tile coordinates and marker original values as separate fields in any manifests.

## Copyright/permissions
The tiles are on a community site but depict game content. A screenshot of a game is not automatically public domain; the wiki's publication of a tile does not automatically grant us rehosting rights. The project owner wants a free derivative fan guide; secure the applicable official fan-content policy or permission before **bundling/rehosting** tiles or modified versions of the tiles. Linked/source-only references and user-loaded files are the current safe workflow. Do not scrape thousands of tiles or build an unauthorized bulk mirror.

## Airport content-source discrepancy that requires audit
The public Airport map guide currently distinguishes **8 permanent + 11 timed + final extraction** (PvP/open reference), while our legacy 275-sample register contains **only 22 Airport records total** and a subset of exit records. This is not a simple like-for-like discrepancy: the 22 samples mix keys, loot, quest and area labels, and the external site contains numerous additional objects.
- Detailed source: https://activematterhelp.ru/guide/map-aeroport
- Data-rich Airport wiki (PvP/PvE toggle): https://activematterhelp.ru/wiki/maps/africa_airport
- The external site's counts and loot assumptions can depend on PvE/PvP and current patch, and need a timestamp before advertising as stable facts.
- Official patch 0.4.0.173 relocated stationary evacuation points near buildings in HQ, Airport and Downtown and moved Devourer spawns away from Airport Investigation locations: https://activematter.game/en/news/349
- Official 0.4.0.192 changed Military Base: Unstable Zone artifact marker timing and Dogorsk extraction scenery behavior: https://activematter.game/en/news/356

## Practical next asset gate
**First deliverable for Airport:** a complete locally stored game-source raster of the airport area with documented permission and tile metadata, plus a named, same-build in-game screenshot for visual validation. If obtained, redraw a faithful flat layer first and only then add editorial shading and measured height overlays.

We cannot honestly mark any map's geometry game-accurate based on sample tile previews alone.
