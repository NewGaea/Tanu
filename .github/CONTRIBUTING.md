# Contributing to Tanu

Thank you for helping build a durable, writer-controlled home for stories. Tanu is early, so clear
problem statements, research, documentation, accessibility work, and careful tests are as valuable
as feature code.

By participating, you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## Before opening work

Search the [issues](https://github.com/NewGaea/Tanu/issues) first. For a substantial product or
architecture change, open an issue before implementing it so ownership, privacy, accessibility, and
self-hosting trade-offs can be discussed while the design is still cheap to change.

Never put a suspected vulnerability, secret, private user information, or unpublished story content
in a public issue. Follow the [security policy](../SECURITY.md) instead.

## Set up the project

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) and run:

```console
uv sync --locked
uv run python manage.py migrate
uv run python manage.py runserver
```

SQLite is used unless `POSTGRES_HOST` is set. Docker Compose and the development container provide a
PostgreSQL environment; see the main [README](../README.md).

## Make a change

- Keep pull requests focused on one problem.
- Add or update tests for behaviour changes.
- Prefer semantic HTML and server-rendered behaviour; add browser JavaScript for demonstrated
  interaction needs.
- Treat keyboard access, visible focus, reduced motion, readable typography, and useful labels as
  acceptance criteria.
- Do not claim roadmap features are implemented until the complete user path exists and is tested.
- Add an architecture decision record when a choice will constrain future work or hosting.

Run the full local check before opening a pull request:

```console
uv run ruff check .
uv run ruff format --check .
uv run python manage.py makemigrations --check --dry-run
uv run coverage run manage.py test
uv run coverage report
uv run python manage.py check
uv run pip-audit
```

If your model change intentionally requires a migration, create it with
`uv run python manage.py makemigrations`, inspect it, and include it in the same change.

## Report a bug

Choose the appropriate [issue form](https://github.com/NewGaea/Tanu/issues/new/choose). The bug form
asks for the expected and actual behaviour, a small reproduction, the affected revision, relevant
environment details, and redacted evidence. Use the feature or design proposal forms before starting
work whose product or architecture direction has not been agreed.

## Commit and pull request style

Tanu follows [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/). Use this shape
for commit messages and pull request titles:

```text
type(optional-scope): concise imperative outcome
```

Common types are:

| Type | Use it for |
| --- | --- |
| `feat` | User-visible capability |
| `fix` | Bug fix |
| `docs` | Documentation only |
| `refactor` | Internal change without new behaviour or a bug fix |
| `perf` | Performance improvement |
| `test` | Test-only change |
| `build` | Dependencies or build system |
| `ci` | Automation and workflow changes |
| `chore` | Maintenance that fits no more specific type |
| `style` | Formatting with no behaviour change |
| `revert` | Reversal of an earlier commit |

Examples:

```text
feat(library): add chapter visibility rules
fix(reader): preserve focus after changing chapters
docs: explain the PostgreSQL setup
build(deps): update Django to 5.2.18
```

Add `!` before the colon for a breaking change, such as
`feat(accounts)!: replace the login identifier`, and explain the migration in the pull request. A
scope is helpful but optional. Do not invent a feature or fix type merely to force a release.

Pull requests should represent one logical change and use the supplied template. Explain the
user-facing outcome, trade-offs, and verification. For visual changes, include narrow and wide
screenshots with useful alt text. The title is checked automatically and becomes the commit on
`main` when the pull request is squash-merged.

The commit types drive Tanu's version and generated changelog. The complete policy and maintainer
setup are in [Releases and versioning](../docs/releases.md).

Contributions are licensed under the repository's GNU GPL v3.0 licence. Only submit work you have the
right to license, and identify third-party material and its licence clearly.
