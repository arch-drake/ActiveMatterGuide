# Deploy Active Matter Source Atlas on Vercel

This repo is a static HTML/CSS/JS website. It needs **no framework, dependencies or build step**. The top-level `index.html` is the launcher, and `tools/all_maps_live_reference.html` is the source-raster map viewer. `vercel.json` pins framework preset to **Other** and publishes the repository root, preserving existing relative links.

## Import the EXISTING repo (do not fork or clone it)

1. Open [Vercel New Project](https://vercel.com/new), log in and choose **Import Git Repository**.
2. Select the existing GitHub repo `arch-drake/ActiveMatterGuide`. If missing, grant the Vercel GitHub integration access to that repository.
3. Choose project name `active-matter-guide` if available, **Root Directory** `./` and **Production Branch** `main`.
4. Confirm **Other** as framework, **Build Command** blank, and **Output Directory** `.`; do not enter any paid service credentials or environment variables.
5. Click **Deploy**. Only report success once Vercel returns **Ready** and its actual `.vercel.app` URL responds.
6. Smoke-check `/` (homepage), `/tools/all_maps_live_reference.html` (13 raster references + Gigastructure floor special), `/tools/map_reference_atlas.html` (evidence viewer), `/tools/map_fidelity_dashboard.html`, and the offline companion's static HTML. Click **Load overhead map** only when you consent to contact the community raster host.

## Accuracy and rights

- Community-hosted source tiles are fetched only after a visitor's opt-in and are not bundled; tile-host availability is separate from Vercel serving the site.
- The primary Atlas has **no reconciled marker overlays**; Gigastructure is a local multi-floor reference, not a finished flat map.
- The old 2.1.1 downloadable offline companion contains illustrative, potentially unaligned maps and historic marker leads. Keep this distinction on the landing page.
- This Vercel configuration does **not** enable GitHub Pages or create a GitHub Release.
- If Vercel warns about file size, bandwidth, or plan charges, review before accepting any non-free plan; no paid hosting tier is required for the static-site design.

## If deployment commands aren't accessible

A connected Vercel service in ChatGPT is not the same as a successfully created Vercel project. The published deployment needs either working Vercel API/actions or a one-time authorization in the Vercel project dashboard. Do not invent a URL; use the assigned domain shown on a successful Vercel deployment.
