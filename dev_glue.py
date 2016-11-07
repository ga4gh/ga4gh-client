"""
Glue for running client code during development

Import this module before using any other module that imports ga4gh.client.
Otherwise, python will look for client in the installed ga4gh package.

See __path__ documentation at:
    https://docs.python.org/2/tutorial/modules.html
"""
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import ga4gh
ga4gh.__path__.insert(0, 'ga4gh')
