# Tanu

**Tanu is an open-source, self-hostable home for independent stories.**

The long-term aim is a calm publishing library where writers keep control of their source material,
readers can enjoy accessible chaptered books, and library operators can offer portable web and ebook
editions without tying their community to a commercial platform.

> [!IMPORTANT]
> Tanu is in a foundation reboot. It is not yet a publishing service. The repository currently
> provides a maintained application base, project homepage, account foundation, and development
> tooling for the product work ahead.

## Why this reboot?

The original 2023 repository never progressed beyond a Next.js starter. In August 2026 it was
replaced with a smaller server-rendered foundation chosen for Tanu's actual domain: Django 5.2 LTS,
Python 3.12, and PostgreSQL. The reasoning and alternatives are recorded in
[ADR-0001](docs/adr/0001-application-foundation.md).

## Quick start

The easiest local path uses SQLite, which is included with Python. Install
[uv](https://docs.astral.sh/uv/getting-started/installation/) and then run:

```console
uv sync --locked
uv run python manage.py migrate
uv run python manage.py runserver
```

Open <http://127.0.0.1:8000>. The health endpoint is available at
<http://127.0.0.1:8000/healthz/>.

To create an administrator for Django's built-in administration site:

```console
uv run python manage.py createsuperuser
```

## PostgreSQL and containers

For the deployment-shaped local environment, use Docker Compose:

```console
docker compose up --build
docker compose exec web python manage.py migrate
```

This starts Tanu at <http://127.0.0.1:8000> and PostgreSQL 18 in a persistent named volume. The
credentials in `compose.yaml` are deliberately development-only.

VS Code and compatible editors can instead reopen the repository in its development container.

## Common checks

```console
uv run ruff check .
uv run ruff format --check .
uv run coverage run manage.py test
uv run coverage report
uv run python manage.py check
uv run pip-audit
```

GitHub Actions runs the same checks, verifies migrations, and evaluates Django's deployment checks.

## Configuration

Development needs no configuration. Deployed instances use environment variables; `.env.example`
documents the supported values. Important production requirements include:

- set `DJANGO_DEBUG=false`;
- provide a long, unique `DJANGO_SECRET_KEY`;
- set `DJANGO_ALLOWED_HOSTS` and `DJANGO_CSRF_TRUSTED_ORIGINS` to the public site;
- provide `POSTGRES_HOST` and PostgreSQL credentials;
- enable HTTPS and cookie settings appropriate to the reverse proxy;
- run `python manage.py check --deploy` against the real production environment.

Django does not automatically read `.env` files. Your process manager or hosting platform should
provide these values as environment variables.

## Repository map

| Path | Purpose |
| --- | --- |
| `tanu/` | Project settings, URLs, and server entry points |
| `core/` | Public pages and health checks |
| `users/` | The swappable user model and account foundation |
| `templates/` | Server-rendered HTML templates |
| `static/` | Styles and public visual assets |
| `docs/adr/` | Decisions with their context and trade-offs |
| `docs/roadmap.md` | Directional product phases and deliberate deferrals |
| `docs/technical-debt.md` | Prioritised engineering risks and remediation phases |
| `docs/releases.md` | Commit, version, changelog, and release policy |
| `CHANGELOG.md` | Release Please's generated user-facing history |

## Product direction

The intended product includes libraries with their own memberships, chaptered stories, durable
revisions, accessible reading, and portable editions. Data modelling and conversion work are not
stubbed out prematurely. See the [roadmap](docs/roadmap.md) for the planned order.

## Contributing and security

Contributions are welcome. Please read the [contribution guide](.github/CONTRIBUTING.md) and
[Code of Conduct](.github/CODE_OF_CONDUCT.md). Report suspected vulnerabilities privately as
described in the [security policy](SECURITY.md). Tanu uses Conventional Commit pull request titles,
Semantic Versioning, and an [automated release process](docs/releases.md).

## Licence

Tanu is free software released under the [GNU General Public License v3.0](LICENSE).
