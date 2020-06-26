# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 National Institute of Informatics.
#
# WEKO-Indextree-Journal is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Module of weko-indextree-journal."""

import os

from setuptools import find_packages, setup

readme = open('README.rst').read()
history = open('CHANGES.rst').read()

tests_require = [
    'coverage>=4.5.3,<5.0.0',
    'mock>=3.0.0,<4.0.0',
    'pytest>=4.6.4,<5.0.0',
    'pytest-cache',
    'pytest-cov',
    'pytest-pep8',
    'pytest-invenio',
    'responses',
]

extras_require = {
    'celery': [
        # Needed for building the documentation until v4.2 is released.
        'celery>=3.1.0,<4.0',
    ],
    'docs': [
        'Sphinx>=1.5.1',
    ],
    'tests': tests_require,
}

extras_require['all'] = []
for reqs in extras_require.values():
    extras_require['all'].extend(reqs)

setup_requires = [
    'Babel>=1.3',
    'pytest-runner>=3.0.0,<5',
]

install_requires = [
    'Flask-BabelEx>=0.9.3',
    'invenio-logging>=1.0.0b3',
]

packages = find_packages()


# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join('weko_indextree_journal', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='weko-indextree-journal',
    version=version,
    description=__doc__,
    long_description=readme + '\n\n' + history,
    keywords='invenio TODO',
    license='MIT',
    author='National Institute of Informatics',
    author_email='wekosoftware@nii.ac.jp',
    url='https://github.com/RCOSDP/weko-indextree-journal',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'invenio_base.apps': [
            'weko_indextree_journal = weko_indextree_journal:WekoIndextreeJournal',
        ],
        'invenio_base.api_apps': [
            'weko_indextree_journal_rest = weko_indextree_journal:WekoIndextreeJournalREST',
        ],
        'invenio_base.blueprints': [
            'weko_indextree_journal = weko_indextree_journal.views:blueprint',
        ],
        'invenio_i18n.translations': [
            'messages = weko_indextree_journal',
        ],
        'invenio_db.models': [
            'weko_indextree_journal = weko_indextree_journal.models',
        ],
        'invenio_access.actions': [
            'indextree_journal_access = '
            'weko_indextree_journal.permissions:action_indextree_journal_access',
        ],
        'invenio_assets.bundles': [
            'weko_indextree_journal_css = weko_indextree_journal.bundles:style',
            'weko_indextree_journal_view = weko_indextree_journal.bundles:js_treeview',
            'weko_indextree_journal_js = weko_indextree_journal.bundles:js',
        ],
        'invenio_celery.tasks': [
            'weko_indextree_journal = weko_indextree_journal.tasks',
        ],
        'invenio_admin.views': [
            'weko_indextree_journal = weko_indextree_journal.admin:index_journal_adminview',
        ],
        # TODO: Edit these entry points to fit your needs.
        # 'invenio_access.actions': [],
        # 'invenio_admin.actions': [],
        # 'invenio_assets.bundles': [],
        # 'invenio_base.api_apps': [],
        # 'invenio_base.api_blueprints': [],
        # 'invenio_base.blueprints': [],
        # 'invenio_celery.tasks': [],
        # 'invenio_db.models': [],
        # 'invenio_pidstore.minters': [],
        # 'invenio_records.jsonresolver': [],
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Development Status :: 1 - Planning',
    ],
)
