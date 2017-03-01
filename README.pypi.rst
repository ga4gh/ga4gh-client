.. image:: http://genomicsandhealth.org/files/logo_ga.png

============
GA4GH Client
============

This is a client library for using the Global Alliance for Genomics and Health (GA4GH) API. This library provides an easy Python programming interface to access GA4GH compliant servers such as the 1kgenomes.ga4gh.org_ server.

.. _1kgenomes: http://1kgenomes.ga4gh.org

**Installation**

::

  pip install ga4gh-client

**To install the latest alpha release use**

::

  pip install --pre ga4gh_client

This installs both the client command line utility and the GA4GH client programming library.

**To demonstrate the CLI try:**

::

  ga4gh_client datasets-search http://1kgenomes.ga4gh.org

**To access the programming API you can use a Python console:**

::

  >>> from ga4gh.client import client
  >>> client.HttpClient
  <class 'ga4gh_client.client.HttpClient'>

==========
REFERENCES
==========

- For more examples of using the GA4GH client visit this `iPython <https://github.com/BD2KGenomics/bioapi-examples/blob/master/python_notebooks/1kg.ipynb>`_ notebook.
- For more information about GA4GH see the `GA4GH <http://www.genomicsandhealth.org>`_ website.
- Full documentation is available at `read-the-docs.org <http://ga4gh-reference-implementation.readthedocs.org/en/stable>`_.
- For a quick start with the GA4GH API, please see our `demo <http://ga4gh-reference-implementation.readthedocs.org/en/stable/demo.html>`_.
- To configure and deploy the GA4GH server in production please see the
  `installation <http://ga4gh-reference-implementation.readthedocs.org/en/stable/installation.html>`_ page.
- If you would like to contribute to the project, please see the
  `development <http://ga4gh-reference-implementation.readthedocs.org/en/stable/development.html>`_ page.
