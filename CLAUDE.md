# Offbeet website — notes for Claude Code

Single-page static site for Offbeet, an instrumental quartet in Ottawa.
Plain HTML/CSS, **no JavaScript, no build step, no framework** — keep it that way.

- Live: https://offbeet.ca (GitHub Pages, auto-deploys from `main`, root).
  Custom domain via the `CNAME` file; DNS at CanSpace (apex A/AAAA to GitHub,
  `www` CNAME to katzfabio.github.io). The old katzfabio.github.io/offbeet/
  URL 301s to the apex.
- Repo: github.com/katzfabio/offbeet
- Deploys take ~30–60s after push; verify with `curl` against the live URL.

## Maintenance model

Fabio describes changes in plain language ("update next show to Aug 14, $20");
edit, commit, push. No local tooling needed.

**Show details live in TWO places that must stay in sync** (both marked in index.html):

1. Hero banner — search `NEXT-SHOW`
2. Tickets section — search `TICKETS-INFO`

Tickets are sold by manual Interac e-transfer to offbeetottawa@gmail.com,
in advance only — no cash at the door. Never add a payment processor.

### Marking a show sold out

`index.html` carries two commented-out `SOLD-OUT SWAP` blocks (hero + tickets),
with the CSS already live. To flip: comment out the live block and uncomment the
sold-out one, in **both** places. Fabio also removes the e-transfer address at
the bank so late transfers bounce rather than being accepted — the sold-out copy
says so, so the two steps go together. Reverse both when the next show goes up.

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
   they're hardcoded (currently 1400×787) and a stale pair causes layout shift.
3. Rewrite its `alt` text to match the new photo.

## Current content status (August 2026)

- Lineup: Jim Gamo (drums), Fabio Katz (guitar/mandolin/Chapman Stick),
  Dan Sharon (bass), Rob Coplan (keyboards). Paul Migneault left the band.
- `assets/band.jpg` (About section) is the real group photo from the July 2026
  practice shoot (B&W, 1400×787) — final.
- All four member headshots are real photos, B&W and square.
- All four bios are real (content from Fabio).
- Next show: Sunday, September 13, 2026 · Hummingbird Hall,
  900 Greenbank Rd, Ottawa · $20 · doors 6:30 PM, music 7–9 PM.
- Social links: none yet; commented-out block ready in the Contact section.
- Videos: three YouTube embeds carried over from the old Google Sites page.
