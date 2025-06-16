format:
	@ruff check . --fix && ruff format .

test:
	@poetry run pytest -vv