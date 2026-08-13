# Releases and versioning

Tanu uses [Semantic Versioning](https://semver.org/) and is deliberately in the `0.x` development
series. The product does not yet promise a stable public API or production support policy. Version
`1.0.0` will be an explicit project milestone rather than an automatic consequence of an early
breaking change.

The checked-in `0.0.0` version means “not released yet.” The first releasable feature after the 2026
reboot will become `0.1.0` automatically.

## What changes a version

The pull request title becomes the squash commit on `main`, so it must follow
[Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/):

| Change | Title example | Version effect before 1.0 |
| --- | --- | --- |
| Backwards-compatible feature | `feat(library): add story collections` | Minor |
| Backwards-compatible bug fix | `fix(reader): preserve paragraph spacing` | Patch |
| Breaking change | `feat(accounts)!: replace the login identifier` | Minor |
| Documentation or maintenance | `docs: explain local backups` | None on its own |

A `BREAKING CHANGE:` footer is equivalent to `!` in a full commit message. Once Tanu reaches
`1.0.0`, breaking changes increase the major version in the usual way.

## Automated release flow

1. Changes reach `main` through a squash-merged pull request with a validated Conventional Commit
   title.
2. Release Please collects releasable commits and opens or refreshes one release pull request.
3. That pull request updates `pyproject.toml`, `uv.lock`, `.release-please-manifest.json`, and
   `CHANGELOG.md`.
4. Merging the release pull request creates the matching `vX.Y.Z` tag and GitHub release.

There is no package-registry publication step. A GitHub release marks a tested source revision; a
future deployment or distribution pipeline should remain a separate, explicit decision.

The first automated release starts after the repository's 2026 foundation-reboot boundary. The
`bootstrap-sha` in `release-please-config.json` deliberately excludes the obsolete starter-project
history from the first generated changelog.

## One-time GitHub settings

A repository administrator should configure these settings after the files reach the default
branch:

- Under **Settings → General → Pull Requests**, allow squash merging and use the pull request title
  as the default squash commit message. Disable other merge methods so the checked title is the
  commit Release Please reads.
- Under **Settings → Actions → General → Workflow permissions**, allow GitHub Actions to create pull
  requests. The release workflow itself grants only the permissions it needs.
- Protect `main`: require a pull request, the `CI / Quality` check, and the
  `PR title / Conventional title` check; require the branch to be current before merging.

The workflow works with GitHub's built-in token. For CI to run automatically on Release Please's own
pull request, create a fine-grained token or GitHub App token with repository contents and pull
request write access, save it as `RELEASE_PLEASE_TOKEN`, and keep the workflow's existing fallback.
Without that optional secret, GitHub intentionally suppresses follow-on workflow runs created by
the built-in token; maintainers can still inspect and merge the generated release pull request.

## Maintainer release checklist

- Confirm the release pull request groups the expected user-facing changes.
- Edit inaccurate source pull request titles rather than hand-editing generated history.
- Confirm CI passes against the release version.
- Merge the release pull request; do not create the tag first or rewrite an existing release.
- Check that the GitHub release and `vX.Y.Z` tag point to the same commit.

If a published release needs a correction, make a new patch release. Released version contents are
immutable.
