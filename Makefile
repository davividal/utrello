.PHONY: build upload

build:
	python -m build

upload:
	python3 -m twine upload --repository testpypi dist/* --verbose