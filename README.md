# FOOTNOTE

**An independent magazine and cultural archive from Jammu and Kashmir.**

FOOTNOTE documents the region's voices, music, languages, creative scenes and cultural memory, with contemporary hip-hop at its centre. It is a publication first: reported stories, interviews, essays, criticism, photography and archival work.

## Issue 001 — The Sound We Made

The first issue explores how sound, music and memory shape cultural identity across Jammu and Kashmir. Contemporary hip-hop is central, alongside distinct coverage of regional languages, poetry, folk music and cultural histories.

The regional lens includes Jammu, Poonch, Rajouri, the Chenab Valley and the Kashmir Valley. These places are not treated as one interchangeable culture.

## The website

The root `index.html` is the current magazine website. It includes:

- Responsive editorial homepage and issue cover.
- Magazine-style spread reader with previous and next controls.
- Editorial story previews clearly marked as work in development.
- Regional coverage section and publication information.
- Mobile navigation and keyboard controls for the reader.

The current reader is a designed preview, not a completed or fact-checked 14-page issue. Planned story directions must not be presented as published reporting.

## Deploying on Cloudflare Pages

This is a static website. Connect the GitHub repository to Cloudflare Pages and use:

- Framework preset: **None**
- Build command: leave empty
- Build output directory: `/` (repository root, if accepted by the dashboard)
- Root directory: leave blank

The deployed output must contain the root `index.html` file. No Node build step is required for this static version.

## Editorial standards

- Verify names, dates, quotations and historical claims before publication.
- Prefer primary sources, archival records and direct interviews.
- Attribute information clearly and distinguish fact, opinion and interpretation.
- Use numbered references where appropriate and provide full citations at the end of each issue.
- Obtain permission for photographs, artwork, recordings and other material.
- Represent communities and regional traditions with context and care.
- Never invent quotes, sources, archival evidence or images.

Read [EDITORIAL-CHARTER.md](EDITORIAL-CHARTER.md) before preparing material for publication.

## Repository contents

- `index.html` — current website and magazine reader.
- `ISSUE-001.md` — editorial brief for the first issue.
- `EDITORIAL-CHARTER.md` — purpose, scope and editorial standards.
- `content/` — planned home for issue and story content.
- `public/` — planned home for magazine covers, photographs, textures and fonts.

## Project status

The website is an active foundation. The next stages are to build out the full issue reader, individual article pages, a reliable content structure, contributor information and the editorial archive. The design preview is not a substitute for reporting, editing, fact-checking or image permissions.
