.DEFAULT_GOAL := all

all: install test run deploy

install:
	@echo -e "*****************************************"
	@echo -e "* Installing pipenv and dependencies... *"
	@echo -e "*****************************************\n"
	@pip install pipenv
	@pipenv --python 3.7
	@pipenv install requests
	@pipenv install pytest

test:
	@echo -e "\n\n"
	@echo -e "*****************************************"
	@echo -e "*            Starting tests...          *"
	@echo -e "*****************************************\n"
	@pipenv run pytest tests/tests.py | tee results.txt

run:
	@echo -e "\n\n"
	@echo -e "***************************************"
	@echo -e "*        Running Python app...        *"
	@echo -e "***************************************\n"
	@pipenv run python app.py | tee -a results.txt
	
deploy:
	@echo -e "\n\n"
	@echo -e "***********************************************"
	@echo -e "* Adding and Committing results.txt to git... *"
	@echo -e "***********************************************\n"
	@git add results.txt
	@git commit -m "Pushing results.txt"
	@git push origin master
