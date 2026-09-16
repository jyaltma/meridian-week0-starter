# meridian-week0-starter

Week 0 starter repository for the Claude Architect Bootcamp. This is the repo
referenced as `meridian-week0-starter` in `w0m1`, `w0m2` and `w0m3` — fork it
into your cohort's GitHub organization, then fork *that* into your own account
for the labs.

## What's in here

- `week0/api/` — empty on purpose. This is where you build your own Python
  script against the mock CRM during the `w0m2` lab.
- `week0/code/` — a Python extract of Meridian's quote pricing logic and a
  TypeScript branch-surcharge client, each with a seeded, realistic defect.
  Used in `w0m1` (confirm the failures exist, leave them alone) and fixed in
  `w0m3`.
- `docs/ENVIRONMENT.md`, `docs/API-NOTES.md`, `docs/TEST-NOTES.md` — templates
  you fill in as you go. Each module's lab tells you when to open one.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate        # .venv\Scripts\activate on Windows
pip install -r requirements.txt

npm ci
```

Copy `.env.example` to `.env` and fill in real values before running anything
that talks to the mock CRM (`w0m2` onward).

## Running the seeded tests

The three seeded failures are split across two test runners — run both to see
all three:

```bash
pytest -q                 # 2 failing tests, in week0/code/tests/
npm test                  # 1 failing test, in week0/code/ts/test/
```

Leave them failing until `w0m3`. `w0m1` only asks you to confirm the count.

## Mock CRM

This repo does not include the mock CRM / ERP / ITSM stack itself — that's a
separate infrastructure repo (`meridian-mock-systems` in the courseware),
brought up with `docker compose up` and expected to answer on the ports listed
in the main courseware README's "Conventions worth preserving" section. If
your cohort organization doesn't have that repo yet, you'll need it before the
`w0m2` API lab and everything from `w0m4` onward.
