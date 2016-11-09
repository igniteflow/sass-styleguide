build:
	python setup.py sdist bdist bdist_wheel

release:
	python setup.py sdist bdist bdist_wheel upload -r pypi

clean:
	rm -rf build dist sass_styleguide.egg-info MANIFEST .cache
