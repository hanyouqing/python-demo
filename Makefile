# @reference:
#	https://www.gnu.org/software/make/manual/html_node/Introduction.html
#	https://www.gnu.org/software/make/manual/html_node/Complex-Makefile.html
#
PATH  := .:$(PATH)
SHELL := /bin/bash

PROJECT = demo
OPTS = help example preinstall build install upload clean docker

help:
	$(info ************    HELP    ************)
	@for opt in $(OPTS); do echo -e "\t"$$opt; done

example:
	@echo "examples:"
	@echo "	xxxx:"

all: preinstall build install clean

preinstall:
	pip install -U setuptools
	pip install -U wheel
	pip install -U twine

check:
	twine check dist/*

build:
	python setup.py sdist
	tree ./dist/

install:
	@#python setup.py install
	pip install .

upload:
	twine upload dist/*

test:
	$(info test)

clean:
	rm -rf __pycache__  
	rm -rf build 
	rm -rf $(PROJECT).egg-info 
	rm -rf $(PROJECT)_python.egg-info 
	rm -rf dist

docker:
	docker-compose build || docker build -t tt .

docker-start:
	docker-compose up 

docker-remove:
	docker-compose down

.PHONY: clean
