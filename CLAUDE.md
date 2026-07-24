# Offbeet website — notes for Claude Code

Single-page static site for Offbeet, an instrumental quartet in Ottawa.
Plain HTML/CSS, **no JavaScript, no build step, no framework** — keep it that way.

- Live: https://katzfabio.github.io/offbeet/ (GitHub Pages, auto-deploys from `main`, root)
- Repo: github.com/katzfabio/offbeet
- Deploys take ~30–60s after push; verify with `curl` against the live URL.

## Maintenance model

Fabio describes changes in plain language ("update next show to Aug 14, $20");
edit, commit, push. No local tooling needed.

**Show details live in TWO places that must stay in sync** (both marked in index.html):

1. Hero banner — search `NEXT-SHOW`
2. Tickets section — search `TICKETS-INFO`

Tickets are sold by manual Interac e-transfer to offbeetottawa@gmail.com.
Never add a payment processor.

## Design rules

- White background, system font stack (Apple-style restraint).
- Spacing is deliberately tighter than the original "generous whitespace" draft —
  Fabio found that version too airy (July 2026). Keep breathing room, but don't
  reintroduce the big clamps; the vertical rhythm now tops out around 4rem for
  section padding.
- Single accent color: beet crimson `--beet: #a91e4f` (sampled from the logo).
- B&W photography only; member photos get `filter: grayscale(1)` as a safety net.
- Keep grids strictly aligned — Fabio reads intentional offsets as bugs.
- The beet-guitar motif is the band's signature and must stay through any redesign.

## Images

- Optimize before committing: JPEG ~82 quality, max ~1400px wide (`sips` works).
- Member photos: `members/<firstname>.jpg`, square, B&W.
- `assets/offbeet01.png` is a local source file, gitignored.

### Replacing the About group photo (`assets/band.jpg`)

`.about-photo` has **no** `filter: grayscale(1)` — unlike the member photos,
this one is not protected, so a colour photo would ship in colour. Steps:

1. Convert to B&W and optimize:
   `sips -m "/System/Library/ColorSync/Profiles/Generic Gray Gamma 2.2 Profile.icc" band.jpg`
   then `sips -Z 1400 band.jpg` and re-encode at ~82 quality.
2. Update `width`/`height` on the `<img class="about-photo">` in index.html —
   they're hardcoded (currently 1400×1120) and a stale pair causes layout shift.
3. Rewrite its `alt` text; the current one describes the AI-generated image.

## Current content status (July 2026)

- Lineup: Jim Gamo (drums), Fabio Katz (guitar/mandolin/Chapman Stick),
  Dan Sharon (bass), Rob Coplan (keyboards). Paul Migneault left the band.
- `assets/band.jpg` (About section) is **AI-generated** (ChatGPT) — the band was
  shooting a real group photo at practice on July 24, 2026. Swap it in when
  Fabio provides it, following "Replacing the About group photo" above.
- Dan's headshot is a stock image Fabio found online, contrast-boosted by him.
  Treat it as final — Dan isn't supplying a better picture. Don't re-encode it
  (that would soften the added contrast); only swap it if Fabio says so.
  Rob's is a real photo of him.
- All four bios are real (content from Fabio).
- Next show: Friday, September 11, 2026 · Hummingbird Hall · $20 ·
  doors 6:30 PM, music 7–9 PM.
- Social links: none yet; commented-out block ready in the Contact section.
- Videos: three YouTube embeds carried over from the old Google Sites page.
