# news-image-20261123 — "One Monday, Five Fractures"

A newspaper-front-page image summing up the world news of
**Monday 23 November 2026**: five verified stories of that day,
each one picture + short caption under a masthead naming the day.

1. **COP31 climate talks collapse** — no deal; the final draft omits
   the words "fossil fuels".
2. **Russian drone strike, Kyiv region** — at least 14 people missing
   (Zelenskiy).
3. **Indonesian factory fire** — 7 body bags recovered, 50 missing
   (candy factory).
4. **South Korea's education minister resigns** over an AI
   exam-cheating scandal.
5. **Nepal PM Balendra Shah meets PM Modi** in New Delhi (state visit).

## How it was built

Three connected providers (Gemini, Groq, Pollinations) each proposed a
layout; the survivor is Gemini's asymmetric front-page grid — a hero
COP31 panel, a Kyiv panel, and three panels below (fire, exam scandal,
Delhi) — chosen over two radial designs that would not read at 300px.
The five scene images were generated in-session with Pollinations
(flux) and composed with PIL into `entry.png`; all captions and the
masthead are PIL-drawn text, so no AI text artefacts appear.

## Running

`main.py` (Python 3.13, standard library only, no network) copies
`entry.png` to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR`).
Both runs write identical bytes.

## Files

- `main.py` — entry program
- `entry.png` — the finished image (1024×1024, ≤1 MiB)
- `LICENSE` — MIT
