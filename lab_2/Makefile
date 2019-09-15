.DEFAULT_GOAL := all

all: install test run deploy

install:
	@echo "Installing pipenv and dependencies."
	sudo pip install pipenv
	pipenv --python 3.7
	pipenv install requests
	pipenv install pytests
test:
	@echo "Start tests."
	pytest tests/tests.py > results.txt
	cat results.txt
run:
	@echo "Run Python app."
	python app.py >> results.txt
	cat results.txt
deploy:
	@echo "Adding and Committing results.txt to git."
	git add results.txt
	git commit -m "Pushing results.txt"
	git push origin master
