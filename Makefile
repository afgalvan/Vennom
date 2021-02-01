init: main.py
	pip3 install pipenv
	pipenv shell
	pipenv install --ignore-pipfile

run: main.py
	pipenv run python3 main.py