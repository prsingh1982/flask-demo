install:
	python -m pip install --upgrade pip &&\
		python -m pip install -r requirements.txt
	python -m pip install tf-keras

test:
	python -m pytest -vv test_app.py

format:
	black *.py

lint:
	python -m pylint --disable=R,C app.py

all: install lint test format