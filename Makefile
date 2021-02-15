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

test:
	poetry run pytest tests/test_diff.py -vv

coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests

run-plain-stylish:
	poetry run gendiff tests/fixtures/inputs/plain_json/file1.json tests/fixtures/inputs/plain_json/file2.json -f stylish