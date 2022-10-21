install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C,W1203,W0702 constants.py
	pylint --disable=R,C,W1203,W0702 combinedfloodproc.py
	pylint --disable=R,C,W1203,W0702 droughtproc.py
	pylint --disable=R,C,W1203,W0702 hailproc.py
	pylint --disable=R,C,W1203,W0702 heatproc.py
	pylint --disable=R,C,W1203,W0702 precipproc.py
	pylint --disable=R,C,W1203,W0702 windproc.py
	pylint --disable=R,C,W1203,W0702 fireproc.py
	pylint --disable=R,C,W1203,W0702 app.py

test:
	python -m pytest -vv --cov=app test_app.py

all: install lint test