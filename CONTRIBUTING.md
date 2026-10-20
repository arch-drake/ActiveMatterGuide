# Community contributions

Thanks for helping improve Field Operations. Accuracy and player progress safety come before feature count.

## Report a correction

Use **Issues → New issue** and choose **Bug report** or **Map / data correction**. Please include:

1. The **current game patch** (if visible), **map** and **raid variant** (PvE/PvP, Open/Isolated, etc.).
2. What the guide currently claims and what you observed instead.
3. An official source link, community source or your own description of repeatable steps.
4. Whether the information is verified, player-reported or still uncertain.

Do **not** attach your browser backup (it may contain private journal information), game account credentials, unlicensed game screenshots or others' copyrighted map artwork. A link to a permissible source is preferable.

## Game-faithful map submissions
Use [the master roadmap](docs/MAP_FIDELITY_MASTER_ROADMAP.md), [Airport benchmark](docs/AIRPORT_BENCHMARK.md), and [14-map register](docs/MAP_PRODUCTION_REGISTER.md).

For each map correction, provide:
- An in-game reference capture with the **game build, raid variant, capture date, north/orientation, original image dimensions and crop**.
- A stable physical feature (road junction, building roof corner, shoreline) and its normalized source/target coordinates. Prefer four spatially separated FIT landmarks plus two independent CHECK landmarks.
- The map/POI name, proposed correction, source URL, what has changed since the previous patch, and confidence level.
- Explicit image attribution/permission if requesting republication of a game map or contributor-annotated texture. Content appearing online does not by itself establish publication rights. You can submit metadata/citations without uploading image bytes.
- If mapping elevations, an independent height reference or multiple oblique views. Keep unknown height flat.
- No unsupported "verified" status solely because the affine RMS is low; per-point gameplay validity needs separate checks.

Map evidence exports from [offline workbench](tools/map_reconciliation.html) do not contain screenshots. Never share your personal browser backup or account data.

## Development standards

- Favor **lasagna-style modular changes**: core → data validation → application services → features → presentation.
- Preserve existing `localStorage` keys and include a migration strategy when schemas change.
- Maintain separate Solo/Team PvE and PvP data.
- Do not invent exact marker art, damage multipliers, guaranteed loot or geometry.
- Run the JavaScript checks and browser smoke/deep suite; log anything that was not testable.
- No game injection, process inspection, overlays that interfere with anti-cheat, subscriptions or involuntary telemetry.

Maintainers will decide whether and how to integrate contributions. A general source license has not yet been selected.
