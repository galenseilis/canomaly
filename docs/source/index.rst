.. canomaly documentation master file, created by
   sphinx-quickstart on Sat May 13 18:03:38 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to canomaly's documentation!
====================================

Project Description
-------------------

This package detects specific types of anomalies with an emphasis in
looking for cumulative changes.

Installation
------------

This package can be installed through
`PyPi <https://pypi.org/project/canomaly/>`__ using

::

   pip install canomaly

or

::

   pip3 install canomaly

Example Usage
-------------

.. code:: python

   >>> import pandas as pd
   >>> from canomaly.searchtools import cumrexpy
   >>> # Get some data
   >>> data = {
               'date': [
                   '2018-11-20',
                   '2018-11-21',
                   '2018-11-22',
                   '2018-11-22',
                   '2018-11-23',
                   '2018-11-24'],
               'email': [
                   'john.doe@example.com',
                   'jane.smith@example.com',
                   'bob-johnson_123@example.com',
                   'sarah@mydomain.co.uk',
                   'frank@mydomain.com',
                   'jessica_lee@mydomain.com'
                       ]
               }
   >>> df = pd.DataFrame(data)
   >>> df['date'] = pd.to_datetime(df['date'])
   >>> # Take a peek at the data
   >>> df
           date                        email
   0 2018-11-20         john.doe@example.com
   1 2018-11-21       jane.smith@example.com
   2 2018-11-22  bob-johnson_123@example.com
   3 2018-11-22         sarah@mydomain.co.uk
   4 2018-11-23           frank@mydomain.com
   5 2018-11-24     jessica_lee@mydomain.com
   >>> # Extract regular expressions
   >>> cumrexpy(df, 'email', 'date')
   date
   2018-11-20                           [^john\.doe@example\.com$]
   2018-11-21                [^[a-z]{4}\.[a-z]{3,5}@example\.com$]
   2018-11-22    [^[a-z]{4,5}[.@][a-z]+[.@][a-z]+\.[a-z]{2,3}$,...
   2018-11-23    [^frank@mydomain\.com$, ^[a-z]{4,5}[.@][a-z]+[...
   2018-11-24    [^frank@mydomain\.com$, ^[a-z]+[.@_][a-z]+[.@]...
   Name: email_grouped, dtype: object


Build Documentation Locally
---------------------------

.. code:: bash

   cd /path/to/canomaly/docs
   make html

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   searchtools

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
