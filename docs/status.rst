.. _status:

+++++++++++++
Release Notes
+++++++++++++

********
0.6.0a10
********

Features:

- Added **support for BigWig files** in a new Continuous Data object (#63)  New endpoints and message types include:
 - `POST /continuoussets/search`
 - `GET /continuoussets/{id}`
 - `POST /continuous/search`
 - Continuous (new)
 - ContinuousSet (new)
 
- Add **ability to list and join peer server networks** (#60)  New endpoints and message types include:
 - `POST /peers/list`
 - `POST /peers/announce`
 - `GET /info`
 - ListPeersResponse (new)
 - Peer (new)
 - AnnouncePeerResponse (new)
 - GetInfoResponse (new)

- Remove feature_id from ExpressionLevel and add ability to search by the Name field (#67)  Impacts
 - 'POST /expressionlevels/search'
 - `GET /expressionlevels/{id}`

- Replaced info fields with rich type Attributes fields (#46)  Impacts the following message types:
 - TranscriptEffect
 - VariantAnnotation
 - Individual
 - Biosample
 - Experiment (new)
 - Analysis (new)
 - Dataset
 - ReadGroup
 - ReadGroupSet
 - ReadAlignment
 - Reference
 - ReferenceSet
 - RnaQuantificationSet
 - RnaQuantification
 - ExpressionLevel
 - Feature
 - VariantSetMetadata
 - CallSet
 - Call
 - Variant

- Replace NCBI taxon ID integer with ontology term.  Impacts the following message types:
 - Reference
 - ReferenceSet

- Changed ontology term “id” to “term_id” (#48)  Impacts the following message types:
 - OntologyTerm

Documentation:

* Created a basic Info page for the Pypi repository (#68)

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
