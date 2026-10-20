# Map adoption / visual evidence gate — October 20, 2026

## Decision
The 14 currently bundled backgrounds are illustrative, NOT exact Active Matter geography. Public community map pages are useful reference material but their availability does **not** establish permission to republish their textures, annotated screenshots, icons, or full databases. A Steam developer reply about the guide is not permission unless it explicitly covers use of those particular assets.

## Reference sources (links, not redistributed assets)
- Community interactive atlas: https://activematter.guide/maps/
- Community map breakdown example (Airport): https://activematterhelp.ru/guide/map-aeroport
- Alternative Airport field reference: https://active-matter.wiki/maps/airport/
- Official October 5 update 0.4.0.173: https://activematter.game/en/news/349
- Official October 15 update 0.4.0.192: https://activematter.game/en/news/356

## Map quality requirements
1. For each of the 14 maps, record the precise game build, mode/variant, orientation, crop, source URL, author, and redistribution permission.
2. Prefer original player-owned in-game screenshots (with their permitted usage confirmed) for accurate 2D roads/buildings/water, not image-generated geography.
3. Match at least four well-separated immovable landmarks, hold out two independent controls, report fit and check errors, flag extraction coordinates as patch-sensitive.
4. Confirm individually the 275 legacy marker samples; currently these are candidates, not authenticated locations. For Gigastructure and Dalniy, avoid a false per-raid coordinate map.
5. Reconcile map icon semantics by patch/mode and keep dynamic event markers separate from static POIs.
6. Build faithful flat geography first. Isometric elevations and floor counts require separate multi-angle or measurement evidence; unknown heights must remain unknown.
7. Retest map selector, zoom, pan, filters, notes, Solo/Team behavior, local screenshot alignment and backup/restore after updates.

## Patch-sensitive points
- 0.4.0.173 relocated stationary extraction points in **Headquarters, Airport and Downtown** nearer buildings and added cover.
- 0.4.0.192 changed monster-artifact marker timing in **Military Base: Unstable Zone**, and corrected Dogorsk extraction-area environment behavior.

## Original visual upgrade status
A separate **Visual Upgrade 2.1.2** offline installer was produced October 20 and saved to the owner's Active Matter Guide Library. It uses 32 original category-level concept scenes (16 new, 16 earlier), applies images to all 20 monster dossier cards and other encyclopedia cards, and adds an atmospheric 14-location selector. Scenes are explicitly NOT game screenshots, accurate weapon models or usable map basemaps. It does not adjust markers or map geometry.

Browser QA on the accessible earlier guide passed installer file selection/download, 20 illustrated monster cards, 14 visual map selectors, successful map-picker click and no runtime JavaScript exceptions. The exact GitHub 2.1.1 HTML has **not** yet been tested with that new installer, so the addon is NOT marked integrated or released from this repository.

## Permission checklist
Obtain either an explicit redistribution license from each map creator, or explicit permission from the rights holder covering the specific images/material and the guide's redistribution context. A general developer comment, open webpage, or attribution alone is insufficient to assume that license. If permission is unavailable, cite and open map pages externally; keep user-provided screenshots local and never package them without authorization.

Next benchmark: **Airport**, with a current-build in-game map screenshot, source link/permission record and stable landmark control points. After that, evaluate the remaining 13 maps one by one.

Independent fan guide — not affiliated with or endorsed by the developers/publisher.
