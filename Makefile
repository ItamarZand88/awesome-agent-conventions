PYTHON ?= python3
PIP ?= pip

.PHONY: install validate build extract check-links check-examples verify-generated verify open-source-check license-report clean

install:
	$(PIP) install -r scripts/requirements.txt

validate:
	$(PYTHON) scripts/validate_targets.py

build:
	$(PYTHON) scripts/build_readme.py
	$(PYTHON) scripts/extract.py --index-only

extract:
	$(PYTHON) scripts/extract.py
	$(PYTHON) scripts/build_readme.py

check-links:
	$(PYTHON) scripts/check_links.py

check-examples:
	$(PYTHON) scripts/check_example_licenses.py --offline

verify-generated:
	$(PYTHON) scripts/check_generated.py

verify: validate verify-generated check-examples check-links

open-source-check: verify
	test -f LICENSE
	test -f CONTRIBUTING.md
	test -f CODE_OF_CONDUCT.md
	test -f SECURITY.md
	test -f THIRD_PARTY_EXAMPLES.md
	test -f WATCHLIST.md
	test -f ROADMAP.md

license-report:
	$(PYTHON) scripts/check_example_licenses.py --markdown

clean:
	find . -name __pycache__ -type d -prune -exec rm -rf {} +
	find . -name '*.pyc' -delete
