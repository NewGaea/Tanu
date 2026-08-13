# Technical-debt register

This register begins after the 2026 foundation reboot. Scores use
`(impact + risk) × (6 − effort)`, where each input is rated from 1 to 5. Higher scores should be
addressed sooner, but dependencies and product discovery still determine implementation order.

| Priority | Item | Type | Impact | Risk | Effort | Score | Why it matters |
| ---: | --- | --- | ---: | ---: | ---: | ---: | --- |
| 1 | Define identity, library tenancy, and author ownership | Architecture | 5 | 5 | 3 | 30 | Almost every permission and data boundary depends on it. |
| 2 | Add end-to-end accessibility and browser checks to CI | Test | 3 | 4 | 2 | The manual baseline is good, but future visual changes need regression coverage. |
| 3 | Build and smoke-test the production container in CI | Infrastructure | 3 | 3 | 2 | Compose parses and Gunicorn runs locally; automated image proof closes the packaging gap. |
| 4 | Threat-model and isolate document conversion | Security | 5 | 5 | 4 | Markdown and especially TeX-like inputs cannot safely execute in the web process. |
| 5 | Define backups, media storage, and restore drills | Operations | 5 | 5 | 4 | A publishing home is only trustworthy if source work can be recovered. |
| 6 | Decide background-job semantics and failure handling | Architecture | 4 | 4 | 4 | Ebook generation and imports will outgrow request-response processing. |
| 7 | Establish stable-release and migration policy | Documentation | 3 | 4 | 3 | Self-hosters need predictable upgrades before Tanu calls itself production-ready. |

## Remediation phases

### Before domain implementation

1. Resolve identity, tenancy, ownership, and role boundaries in an ADR.
2. Add a container-build job to CI.
3. Add repeatable browser and accessibility smoke tests for the current public page.

### Before accepting author content

1. Threat-model upload, preview, conversion, and export paths.
2. Isolate resource-intensive or executable conversion tools from the web process.
3. Define source-file storage, validation, quotas, retention, and backup restoration.

### Before the first stable release

1. Test PostgreSQL backup and restore procedures with realistic libraries.
2. Document supported versions, data migrations, rollback limits, and release cadence.
3. Exercise an upgrade from the previous release using a copy of production-shaped data.
