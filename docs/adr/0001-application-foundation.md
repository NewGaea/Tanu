# ADR-0001: Use a Django modular monolith with PostgreSQL

- **Status:** Accepted
- **Date:** 2026-08-13
- **Amended:** 2026-08-13 (Python 3.14 production baseline)
- **Deciders:** Tanu maintainers

## Context

Tanu intends to be a self-hostable publishing library for independent authors. Its planned domain
includes libraries, members, roles, stories, chapters, revisions, tags, comments, bookmarks,
subscriptions, and ebook exports. The 2023 repository contained only the unmodified Next.js starter;
there was no application or data to migrate.

The new foundation should be approachable for a small project, friendly to self-hosters, secure by
default, and useful without requiring a client-side JavaScript application.

## Decision

Use a server-rendered Django 5.2 LTS modular monolith on Python 3.14, backed by PostgreSQL in deployed
environments. Keep Python 3.12 as the minimum supported interpreter and test both ends of the
supported range. Use Django templates for the initial interface, add small amounts of progressive
enhancement only where they earn their maintenance cost, and manage dependencies with uv.

SQLite is supported for the zero-configuration development path. PostgreSQL is the deployment
target and the database used by the container setup.

## Options considered

| Option | Complexity | Domain fit | Self-hosting | Main trade-off |
| --- | --- | --- | --- | --- |
| Django + PostgreSQL | Low–medium | Excellent | Strong | Less client-side ecosystem reach |
| Next.js + PostgreSQL | Medium | Good | Good | Authentication, administration, and backend composition require more choices |
| Rails + PostgreSQL | Low–medium | Excellent | Strong | Ruby was a larger tooling shift for this repository's likely contributors |
| Headless CMS + custom reader | Medium–high | Mixed | Mixed | Fast content editing, but awkward ownership of Tanu's bespoke publishing domain |

MongoDB was not retained. Tanu's central concepts and permissions are relational, and transactional
integrity matters for publication, revision, and membership workflows. PostgreSQL can still store
flexible metadata in JSON fields where appropriate without making the full domain document-based.

## Consequences

- Authentication, permissions, forms, migrations, security middleware, and an administration site
  are available without assembling a collection of services.
- Server-rendered pages establish a fast, accessible baseline with very little browser JavaScript.
- Python provides a mature ecosystem for Markdown, TeX, document conversion, and EPUB work.
- A separate frontend can still be added later through Django views or an API, but it must solve a
  demonstrated interaction need.
- A minimal custom user model exists from the first migration so account fields can evolve safely.
- Background jobs and object storage remain undecided until publishing pipeline requirements are
  known.

## Follow-up decisions

1. Model library tenancy and ownership boundaries.
2. Define story source, revision, and publication semantics.
3. Choose a safe document-conversion boundary for untrusted author input.
4. Choose storage and backup policies for source files and generated editions.
5. Threat-model membership, comments, moderation, and export workflows before implementation.
