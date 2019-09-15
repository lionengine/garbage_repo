.DEFAULT_GOAL := all

all: install test run deploy

install:
	@echo "Installing pipenv and dependencies."
	@pip install pipenv
	@pipenv --python 3.7
	@pipenv install requests
	@pipenv install pytest

test:
	@echo -e "Starting tests...\n"
	@pytest tests/tests.py | tee results.txt

run:
	@echo "Run Python app."
	@python app.py | tee -a results.txt

deploy:
	@echo "Adding and Committing results.txt to git."
	@git add results.txt
	@git commit -m "Pushing results.txt"
	@git push origin master
