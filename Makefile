all: default

clean: 

deps:
	pip install -r requirements.txt

dev_deps:
	pip install -r requirements-dev.txt

check-format: dev_deps
	yapf -rd src

format: dev_deps
	yapf -ri src

lint: check-format
	pylint -r n src

lint-no-error: 
	pylint --exit-zero -r n src

test: build dev_deps
	python3 -m pytest -v

build: clean deps
