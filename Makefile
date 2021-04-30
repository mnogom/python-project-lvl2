install:
	poetry install

gen-diff:
	poetry run gendiff

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall

lint:
	poetry run flake8 gendiff
	poetry run flake8 tests

test:
	poetry run pytest tests/test_diff.py -vv

coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests

local-coverage:
	poetry run pytest --cov=gendiff tests
