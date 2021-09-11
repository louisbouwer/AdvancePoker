install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=game --cov=deck --cov=card ./app/test_adv_poker.py

format:
	black *.py

lint:
	pylint --disable=R,C,W1203,E1101 game deck card
	
all: install lint test