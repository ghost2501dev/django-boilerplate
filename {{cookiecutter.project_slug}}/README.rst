{% for _ in cookiecutter.project_name %}*{% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}*{% endfor %}

{{ cookiecutter.project_description }}

Getting Started
===============

Prerequisites
-------------

* Python >= 3.6.0 <https://docs.python.org/3/index.html>
* Postgres >= 10.0 <https://www.postgresql.org/docs/>

Installing
----------

1. Create the database and the virtual environment. We recommend using
   `virtualenvwrapper <http://virtualenvwrapper.readthedocs.io/en/latest/index.html>`_.

2. Create an .env file and set variables. Examples can be found in :code:`.env.example`.

3. Setup the environment:

   .. code-block:: bash

      $ pip install -r requirements.txt
      $ python manage.py migrate

4. Start the server:

   .. code-block:: bash

      $ python manage.py runserver

The site will be available on <http://localhost:8000> or <http://127.0.0.1:8000>.

You can create a custom settings in `project/settings/custom.py`.
Set DJANGO_SETTINGS_MODULE to your settings file and import all from
`project/settings/common.py`.

Deploy
======

Put your deploy instructions here, otherwise, pass instructions to the administrator.

Translations
============

Example of how to make messages for spanish (es):

   .. code-block:: bash

      $ django-admin makemessages --locale=es

Django translations should be compiled automatically during the deployment.
If you want to compile messages, use the compilemessages command:

   .. code-block:: bash

      $ django-admin compilemessages --locale=es

Requirements
============

We use constraints.

Add dependencies to requirements.txt:

   .. code-block:: text

      # requirements.txt
      -c constraints.txt
      Django
      anotherdependency

Then run:

   .. code-block:: bash

      $ pip install -r requirements.txt
      $ pip freeze > constraints.txt


Tests
=====

For postgres, the user must have permissions to create the database.
So in psql, you must do the following. See <https://stackoverflow.com/a/14186439>.

   .. code-block:: bash

      =# ALTER USER dbuser CREATEDB;

The tests should live in a directory inside the same directory of the code being tested.
The test file must start with test_*. For example, the tests for foo/bar.py
lives in foo/tests/test_bar.py.

Basic commands
--------------

   .. code-block:: bash

      # Run all tests
      $ pytest

      # Run wip tests
      # See <http://doc.pytest.org/en/latest/example/markers.html> and `pytest.ini`
      $ pytest -m wip

Coverage
--------

   .. code-block:: bash

      $ pytest --cov=.

**Notes:**

- Use `Factory Boy <https://factoryboy.readthedocs.io/en/latest/index.html>`_ for mock models
- We use `Splinter <https://splinter.readthedocs.io/en/latest/index.html>`_ to test templates
- We recommend use `snapshottest <https://github.com/syrusakbary/snapshottest>`_ for complex outputs
- We do not use sqlite because the results may vary between different engines

This project was created with `Django Boilerplate <https://gitlab.com/ghost2501/django-boilerplate>`_.
