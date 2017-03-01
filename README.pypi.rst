============
GA4GH Client
============

This is a client library for using the Global Alliance for Genomics and Health (GA4GH) API. This library provides an easy Python programming interface to access GA4GH compliant servers such as 1kgenome.ga4gh.org.

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

For more examples of using the GA4GH client visit this iPython_ notebook.

.. _iPython: https://github.com/BD2KGenomics/bioapi-examples/blob/master/python_notebooks/1kg.ipynb

For more information about GA4GH see the GA4GH_ website.

.. _GA4GH: http://www.genomicsandhealth.org
