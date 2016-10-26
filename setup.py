# Don't import __future__ packages here; they make setup fail

import ga4gh_common.setup as setup

packageDict = {
    "name": "ga4gh_client",
    "description": "A client for the GA4GH reference server",
    "packages": ["ga4gh_client"],
    "url": "https://github.com/ga4gh/ga4gh-client",
    "use_scm_version": {"write_to": "ga4gh_client/_version.py"},
    "entry_points": {
        'console_scripts': [
            'ga4gh_client=ga4gh_client.cli:client_main',
        ]
    },
}
setup.doSetup(packageDict)
