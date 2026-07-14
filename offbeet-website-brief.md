# Offbeet Website — Project Brief

## Overview
Static website for Offbeet, an instrumental trio (now quartet) based in Ottawa. Replaces the current Google Sites page. No backend, no CMS, no build step — plain HTML/CSS/JS hosted on GitHub Pages.

## Band
- Instrumental group blending electric guitar, bass, drums, and keyboards
- Influences: rock, classical, world, TV themes
- Signature visual: the beet-bodied electric guitar (beet/beat play on words) — a refreshed version may be used, but the motif stays
- Current lineup: Jim Gamo, Fabio Katz, Dan (new), Rob (new) — Paul has left the band

## Visual Direction
- White background, minimalistic, generous whitespace (Apple-style restraint)
- Black-and-white photography for member bios
- Full-color band logo as the single accent element on the page
- Clean sans-serif typography, no clutter

## Page Structure (single page, scroll sections, sticky nav)

Sticky top nav with anchor links (Home / Members / Music / Tickets / Contact) so Tickets is reachable in one tap from anywhere on the page — no full scroll required.

### 1. Hero
- Color band logo
- Tagline
- Next show banner: date, venue, ticket status (placeholder for now)

### 2. About
- Short 2–3 sentence bio reflecting the new lineup (placeholder text)
- Band group photo placeholder

### 3. Members
- 4 cards: Jim Gamo, Fabio Katz, Dan [surname], Rob [surname]
- Each card: B&W photo placeholder, name, instrument(s), bio placeholder

### 4. Music / Videos
- Grid of embedded YouTube videos
- Carry over existing videos, plus placeholders for new material

### 5. Shows & Tickets
- Show details: date, venue, price
- Ticket purchase: e-transfer instructions (email address + note to include in transfer) — no payment processor, manual e-transfer only

### 6. Contact / Follow
- Email
- Social links (placeholders if not yet set up)

## Technical Approach
- Plain HTML/CSS/JS, no framework
- One GitHub repo, deployed via GitHub Pages from `main`
- Frequently-changing content (next show date, price, ticket status) isolated in one clearly-marked block (e.g. `content.json` or top of `index.html`) so future edits are fast and low-risk
- Member photos stored in a `/members` folder, referenced by filename
- Images pre-sized/optimized on upload

## Content Still Needed
- Band logo (color, Apple-style)
- B&W photos: Jim, Fabio, Dan, Rob
- Band group photo
- Photo of the beet-bodied guitar (current or refreshed)
- Updated bios: all 4 members, with instrument(s) each plays
- Updated band bio (About section)
- Next show details
- E-transfer email + instructions text
- Social links (if any)

## Maintenance Model
- No local dev setup needed for routine updates
- Future changes (e.g. "update next show to Aug 14, $20") can be described in plain language to Claude Code, which edits the file, commits, and pushes — GitHub Pages updates automatically
