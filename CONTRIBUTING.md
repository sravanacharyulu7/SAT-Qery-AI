# Contributing / Team Workflow

## Branching
- `main` — always demo-ready. Never push directly to it.
- `feature/<name>-<short-task>` — e.g. `feature/asha-sam2-integration`
- Open a PR into `main` when a piece works standalone (even roughly). Merge fast — hackathon speed, not perfection.

## Commit messages
Keep them short and descriptive: `feat: wire VLM output into SAM2 mask input`, `fix: tiling script crashes on non-square images`.

## Daily sync (recommended)
A 10-minute standup, twice a day is usually enough for a hackathon:
1. What did you finish since last sync?
2. What are you doing next?
3. Are you blocked on anyone else's piece?

## Task board
Use GitHub Projects (free, built into the repo) or Trello. Suggested columns: `Backlog` → `In Progress` → `Blocked` → `Done`.

## Definition of "done" for the MVP
Before polishing anything further, get this single path working end-to-end:
1. Upload one sample satellite image
2. Type one hardcoded-style query ("highlight the flooded area")
3. See a mask overlay rendered on the frontend

Everything else (fine-tuning, Geo-RAG, multi-query robustness) is enhancement on top of that one working path.
