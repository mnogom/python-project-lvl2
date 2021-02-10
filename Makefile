install:
	poetry install

gen-diff:
	poetry run gendiff

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff
	poetry run flake8 tests

test:
	poetry run pytest tests/test_diff.py -vv

coverage:
	poetry run coverage run --source=gendiff -m pytest tests
	poetry run coverage xml

run-plain-stylish:
	poetry run gendiff tests/fixtures/inputs/plain_json/file1.json tests/fixtures/inputs/plain_json/file2.json -f stylish

run-recur-stylish:
	poetry run gendiff tests/fixtures/inputs/recursive_json/file1.json tests/fixtures/inputs/recursive_json/file2.json -f stylish

run-plain-plain:
	poetry run gendiff tests/fixtures/inputs/plain_json/file1.json tests/fixtures/inputs/plain_json/file2.json -f plain

run-recur-plain:
	poetry run gendiff tests/fixtures/inputs/recursive_json/file1.json tests/fixtures/inputs/recursive_json/file2.json -f plain

run-plain-json:
	poetry run gendiff tests/fixtures/inputs/plain_json/file1.json tests/fixtures/inputs/plain_json/file2.json -f json

run-recur-json:
	poetry run gendiff tests/fixtures/inputs/recursive_json/file1.json tests/fixtures/inputs/recursive_json/file2.json -f json