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

test:
	poetry run pytest tests/tests.py -vv

run-plain:
	poetry run gendiff tests/fixtures/plain_json/file1.json tests/fixtures/plain_json/file2.json -f stylish

run-recur:
	poetry run gendiff tests/fixtures/recursive_json/file1.json tests/fixtures/recursive_json/file2.json -f stylish