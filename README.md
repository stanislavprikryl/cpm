# Common Provenance Model (CPM)

This repository contains the semantic definition and validation rules for the **Common Provenance Model (CPM)**. The model is built as an extension of the W3C PROV-O standard and serves to ensure strict bidirectional traceability in distributed systems.

## Repository Structure

* **`cpm.ttl`**
  The main definition file of the ontology in Turtle format. It contains the complete CPM vocabulary (classes, connectors, agents, and data properties) extending the `prov:` standard.

* **`cpm-shapes.ttl`**
  The normative SHACL (Shapes Constraint Language) validator. It contains strict rules (closed shapes, cardinalities, data types, and PROV topology constraints) designed to prevent the creation of inconsistent data and ensure compliance with the CPF specification. Each shape includes inline references to the corresponding sections of the CPF Supplementary document that justify its constraints.

  * **`example.trig`**
  A fully functional, multi-hop demonstration scenario (Hospital → Biobank → Research Lab) written in TriG format. Each Finalized Provenance Component (FPC) is encapsulated in its own named graph (`prov:Bundle`), per CPF Supplementary §1.1. The example demonstrates the complete CPM topology including main activities, forward and backward connectors, specialized forward connectors, current/sender/receiver agents, and the full set of PROV relations (`prov:wasGeneratedBy`, `prov:used`, `prov:wasAssociatedWith`, `prov:specializationOf`, `prov:wasDerivedFrom`). All three bundles validate cleanly against `cpm-shapes.ttl`.

* **`validate.py`**
  A Python validation script that performs per-bundle SHACL validation of `example.trig` against `cpm-shapes.ttl`, using `cpm.ttl` as the OWL ontology for RDFS subclass inference. Requires `rdflib` and `pyshacl` (`pip install rdflib pyshacl`).


* **`cpm/`**
  A directory containing the interactive and fully interlinked HTML documentation of the entire ontology, generated using the WIDOCO tool. The main entry point for the documentation is `cpm/index-en.html`.

* **`LICENSE`**
  This repository is licensed under the open MIT license.

## How to Use This Repository

### Viewing the Documentation
For local viewing of the HTML documentation (including graph visualization), we recommend opening the `cpm` directory via a local web server (e.g., using the *Live Server* extension in VS Code or via Python `python -m http.server`) to prevent browser script blocking (CORS).

### Data Validation

The repository includes a ready-to-run validation script. From the repository root:

```bash
pip install rdflib pyshacl
python validate.py
```

Expected output:

```bash
=== Per-bundle SHACL validation of CPM-conformant FPCs ===

Bundle <http://example.org/cpf-scenario/LabBundle>: 37 triples -- PASS
Bundle <http://example.org/cpf-scenario/HospitalBundle>: 31 triples -- PASS
Bundle <http://example.org/cpf-scenario/BiobankBundle>: 51 triples -- PASS

=== OVERALL: PASS ===

```

### Validating Your Own Data
To verify whether your own PROV data meets the requirements of this model, run `cpm-shapes.ttl` against your data graph using any standard SHACL validator (e.g., the `pyshacl` library, Apache Jena `shacl` command, or the online [SHACL Playground](https://shacl.org/playground/)). For TriG-formatted data with multiple `prov:Bundle` graphs, validate each bundle independently — the `validate.py` script demonstrates this pattern.

### Note on Hash Values
The `cpm:referencedBundleHashValue` literals in `example.trig` are illustrative placeholders. In production deployments, these would be computed via RDF Dataset Canonicalization (RDFC-1.0) over the referenced bundle's contents.
