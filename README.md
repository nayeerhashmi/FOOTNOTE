# FOOTNOTE

**An independent magazine and cultural archive from Jammu and Kashmir.**

FOOTNOTE documents the region's voices, music, languages, creative scenes and cultural memory, with contemporary hip-hop at its centre. It is a publication first: reported stories, interviews, essays, criticism, photography and archival work.

Its purpose is to give local artists, writers, communities and histories the context and attention they deserve.

## Editorial identity

FOOTNOTE is rooted in Jammu and Kashmir. Its coverage can move across Jammu, Poonch, Rajouri, the Chenab Valley and the Kashmir Valley. Hip-hop is a central lens, not the only subject. Regional languages, poetry, folk music, oral histories, visual culture and everyday cultural life belong in the magazine too.

The publication should feel literary, documentary and archival. Its visual language takes cues from independent music and culture magazines such as *The FADER*, *The Wire* and *The Face*, while developing an identity of its own. Think strong typography, warm paper, black ink, deep red accents and photographs with real documentary value.

## First issue

**Issue 001 — The Sound We Made**

The first issue explores how sound, music and memory shape cultural identity across Jammu and Kashmir. Contemporary hip-hop is central, while older musical traditions and regional histories receive their own considered space.

Planned editorial directions include:

- The history and present of hip-hop in Jammu and Kashmir.
- Regional languages, poetry and cultural expression.
- Folk music and musical traditions, including Dogri voices.
- Stories from Jammu, Poonch, Rajouri, the Chenab Valley and the Kashmir Valley.
- **Before the Spotlight: The People Who Built Jammu Hip-Hop.**

These are editorial directions, not claims that every story is already reported or verified.

## Editorial standards

- Verify names, dates, quotations and historical claims before publication.
- Prefer primary sources, archival records and direct interviews.
- Attribute information clearly and distinguish fact, opinion and interpretation.
- Use numbered references where appropriate and provide full citations at the end of each issue.
- Obtain permission for photographs, artwork, recordings and other material.
- Represent communities and regional traditions with context and care.
- Never invent quotes, sources, archival evidence or images.

Read [EDITORIAL-CHARTER.md](EDITORIAL-CHARTER.md) before proposing or preparing material for publication.

## Repository contents

- `.github/workflows/` — GitHub Actions workflow for the existing video-generation utility.
- `scripts/create_video.py` — experimental text-card video generator.
- `ISSUE-001.md` — editorial brief for the first issue.
- `EDITORIAL-CHARTER.md` — purpose, scope and standards for the magazine.

The video generator is a supporting production experiment. It is not the magazine itself and does not replace reporting, editing or fact-checking.

## Existing video utility

The current workflow can generate a simple vertical text-card video with computer-generated narration. To run it, open **Actions → Create FOOTNOTE video → Run workflow**, enter a subject, and download the resulting `footnote-video` artifact.

It does not produce researched journalism, cinematic footage or automatic social-media publishing. Review and fact-check all material before using it.

For local use, the utility requires Python 3, Pillow, FFmpeg and espeak-ng:

```bash
python scripts/create_video.py --idea "Your FOOTNOTE video idea" --output output/footnote-video.mp4
```

GitHub Actions usage is subject to the limits and terms of your GitHub plan.

## Project status

FOOTNOTE's editorial identity and first-issue direction are documented here. The magazine website, publishing system, issue layout and contributor workflow should be developed as publication infrastructure, without removing or breaking the existing video utility.
