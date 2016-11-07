"""
Simple shim for running the client program during development.
"""
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import dev_glue  # NOQA
import ga4gh.client.cli as cli

if __name__ == "__main__":
    cli.client_main()
