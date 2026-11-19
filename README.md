# Daily Frame API: merge-docs demo

A small FastAPI backend for the Daily Frame puzzle. It exists to demo **merge-docs**, which turns API contracts into documentation automatically.

- **API catalogue (GitHub Pages):** built from the code on every push to `main`. Search by feature, path or field name.
- **API changes comment:** every pull request that changes an endpoint or a Pydantic model gets one comment listing the contract changes. The comment also flags notes in `docs/features/` that the PR made stale.

How it works:
- `.github/workflows/catalogue.yml` builds the static site with `tools/merge-docs` and deploys it to Pages.
- `.github/workflows/api-changes.yml` posts or updates the PR comment using the workflow's `GITHUB_TOKEN`.

Nothing here uses an LLM. The code is read statically and never run.
