# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 National Institute of Informatics.
#
# weko-gridlayout is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Minimal Flask application example.

SPHINX-START

First install weko-gridlayout, setup the application and load
fixture data by running:

.. code-block:: console

   $ pip install -e .[all]
   $ cd examples
   $ ./app-setup.sh
   $ ./app-fixtures.sh

Next, start the development server:

.. code-block:: console

   $ export FLASK_APP=app.py FLASK_DEBUG=1
   $ flask run

and open the example application in your browser:

.. code-block:: console

    $ open http://127.0.0.1:5000/

To reset the example application run:

.. code-block:: console

    $ ./app-teardown.sh

SPHINX-END
"""

from __future__ import absolute_import, print_function

from flask import Flask
from flask_babelex import Babel

from weko_gridlayout import WekoGridLayout
from weko_gridlayout.views import blueprint

# Create Flask application
app = Flask(__name__)
Babel(app)
WekoGridLayout(app)
app.register_blueprint(blueprint)
