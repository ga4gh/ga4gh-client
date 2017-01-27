.. _status:

+++++++++++++
Release Notes
+++++++++++++

*************
0.6.0a9.post2
*************

Bugfix release which uses the new release process.

*************
0.6.0a9.post1
*************

Bugfix release which fixes the following issues:

* wrong attributes on RnaQuantification (#53)
* wrong attributes on ExpressionLevels (#51)

*******
0.6.0a9
*******

A new versioning scheme has been introduced that will make it easy to tell
which version of the client to use against a protocol version!

* Calls are now returned as ListValues and can be int32, empty, or strings
    to cover the case when a VCF call states no call was made.
* Refactor "BioSample" to "Biosample".
* Switch to stable protobuf version (3.1).
* Improve generated documentation.
* Add authorization via headers.

*****
0.0.4
*****


*****
0.0.3
*****

Add hierachical namespace

*****
0.0.2
*****

Release using new ga4gh packages, ga4gh-common and ga4gh-schemas

*****
0.0.1
*****

Initial release
