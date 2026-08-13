## Outcome

<!-- What becomes better for a reader, writer, operator, or contributor? -->

## What changed

<!-- Keep this focused. Link an issue with "Closes #123" when one exists. -->

-

## Verification

<!-- List the checks you ran and any important manual scenarios. -->

- [ ] `uv run ruff check .`
- [ ] `uv run ruff format --check .`
- [ ] `uv run python manage.py makemigrations --check --dry-run`
- [ ] `uv run coverage run manage.py test && uv run coverage report`
- [ ] `uv run python manage.py check`
- [ ] `uv run pip-audit`

## Visual and accessibility evidence

<!-- For interface changes, include narrow and wide screenshots with useful alt text. Describe keyboard,
screen-reader, contrast, zoom, and reduced-motion checks that apply. Write "Not applicable" otherwise. -->

## Risk and release notes

<!-- Note migrations, configuration changes, compatibility breaks, privacy/security effects, rollback
needs, or follow-up work. Write "None" when there are none. -->

## Checklist

- [ ] The pull request title follows `type(optional-scope): concise outcome`.
- [ ] This change is focused and the documentation matches the implemented behaviour.
- [ ] Behaviour changes have tests, or I have explained why a test is not practical.
- [ ] No secrets, personal data, or unpublished story content are included.
- [ ] Third-party material is identified and compatible with the GPL-3.0-only licence.
