# Tanu roadmap

Tanu is in a foundation reboot. This roadmap is directional rather than a promise of dates.

## Phase 1: dependable foundation — current

- Maintain a supported LTS application stack and reproducible dependency lock.
- Keep local setup simple while making the production configuration explicit.
- Run automated style, test, migration, deployment, and dependency checks.
- Document architectural choices and keep the public project status honest.

## Phase 2: stories and libraries

- Design library tenancy, account ownership, roles, and invitations.
- Design books, chapters, stable identifiers, revisions, drafts, and publications.
- Build the smallest complete authoring-to-reading path.
- Establish accessibility, content warning, privacy, moderation, and backup policies.

## Phase 3: portable editions

- Define supported source formats and a safe conversion boundary.
- Export valid EPUB editions with accessible navigation and metadata.
- Provide source archives and documented migration paths.
- Test round trips and long-term preservation workflows.

## Phase 4: community features

- Add bookmarks, follows, tags, and comments only after the ownership model is stable.
- Give library operators clear moderation tools and audit trails.
- Research federation and discovery without coupling the core publishing path to them.

## Deferred on purpose

- Rich client-side editing
- Federation
- Recommendations or ranking
- Multi-format TeX execution on the web process
- A plugin marketplace

These may be worthwhile later. Adding them before the core domain and threat model are understood
would create more architecture than product.
