# Guelph API

RESTful API service for the [University of Guelph][1] written in Python and Django.

## Documentation

You can find API documentation and well as REST methods in the docs/ directory.

## Status

This is a work in progress and will only support a subset of services to start.

## Dependencies

* Python 2.5+ (tested with Python 2.7.2)
* virtualenv
* pip
* Django 1.4
* [django-tastypie][2] 0.9.11

See requirements.txt for more details.

### To Install

* Install easy\_install: `sudo apt-get install python-setuptools python-dev build-essential`
* Install virtualenv: `sudo easy_install -U virtualenv`
* Create a virtual environment in our source directory: `virtualenv --distribute venv`
* Get into your virtual environment: `source nenv/bin/active`
* To leave this virtualenv: `deactivate`
* Install packages: `pip install -r requirements.txt`
* Your packages have been installed. Verify with yolk: `yolk -l`

**NOTE:** You may need to install `libxml2-dev` and `libxslt-dev` in your package manager to resolve lxml dependencies.


  [1]: http://uoguelph.ca "University of Guelph"
  [2]: http://django-tastypie.readthedocs.org/en/v0.9.11/ "django-tastypie"
