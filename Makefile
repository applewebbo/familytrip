.PHONY: server

server:
	python manage.py runserver

requirements-dev:
	pip install --upgrade pip pip-tools
	pip install -r requirements-dev.txt -r requirements.txt

requirements:
	pip install --upgrade pip pip-tools
	pip-compile --resolver=backtracking
	pip install -r requirements-dev.txt -r requirements.txt

checkmigrations:
	python manage.py makemigrations --check --no-input --dry-run

# coverage:
# 	pytest --cov --migrations -n 2 --dist loadfile

# fcov:
# 	@echo "Running fast coverage check"
# 	@pytest --cov -n 4 --dist loadfile -q