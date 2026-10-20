# Publish on GitHub (quick setup)

Repository suggestion: `arch-drake/active-matter-field-operations` (create as a **public** repository).

1. Visit <https://github.com/new> while signed in.
2. Choose owner **arch-drake**, repository name **active-matter-field-operations**, visibility **Public**. Do **not** initialize with a README, .gitignore or license: those are included in this prepared folder.
3. Click **Create repository**.
4. In the empty repository select **uploading an existing file**. Drag the **contents** of this prepared folder (not the parent folder and not the ZIP itself) into GitHub, verify nested folders, then commit to `main`.
5. To enable online browser use, open **Settings → Pages → Build and deployment → Deploy from a branch → main / (root) → Save**. GitHub will show the resulting URL once published. You can also share the repository URL immediately.
6. In the repository **About** pane, set the description to: `Free unofficial Active Matter PvE/PvP field guide — offline maps, investigations, monster dossier, soundscapes and collectibles.` Optional topics: `active-matter`, `game-guide`, `pve`, `pvp`, `offline-first`.
7. Check the README, click the launcher and download ZIP on your own browser. If you want the Download button within GitHub's Releases area, choose **Releases → Draft a new release**, tag `v2.1.0`, attach the 9.3 MiB release ZIP (with the public-source QA-script typo fixed), and publish.

**Simple update policy:** Keep `active_matter_solo_pve_field_guide.html`, `downloads/…zip`, `manifest.json` and documentation synchronized in one commit per release. Never commit personal backup exports.

**License note:** This repository currently has no general software license. Select one deliberately before inviting third parties to reuse code; do not license game's trademarks or unlicensed community datasets on their behalf.

**In case the uploader doesn't accept a whole folder:** use GitHub Desktop → File → Add local repository / Create a repository from the prepared folder, commit, then **Publish repository** with visibility Public; or clone the empty repository and copy this folder's contents into the clone before commit/push.
