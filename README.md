# Common Provenance Model (CPM)

This repository contains the semantic definition and validation rules for the **Common Provenance Model (CPM)**. The model is built as an extension of the W3C PROV-O standard and serves to ensure strict bidirectional traceability in distributed systems.

## Repository Structure

* **`cpm.ttl`**
  The main definition file of the ontology in Turtle format. It contains the complete CPM vocabulary (classes, connectors, agents, and data properties) extending the `prov:` standard.

* **`cpm-shapes.ttl`**
  The normative SHACL (Shapes Constraint Language) validator. It contains strict rules (closed shapes, cardinalities, and data types) designed to prevent the creation of inconsistent data and ensure 100% compliance with the CPF specification.

  * **`example.ttl`**
  A fully functional, multi-hop demonstration scenario (Hospital -> Biobank -> Research Lab) written in Turtle. It illustrates how forward and backward connectors securely link across different distributed nodes. This dataset is guaranteed to validate perfectly against the provided SHACL shapes.

* **`cpm/`**
  A directory containing the interactive and fully interlinked HTML documentation of the entire ontology, generated using the WIDOCO tool. The main entry point for the documentation is `cpm/index-en.html`.

* **`LICENSE`**
  This repository is licensed under the open MIT license.

## How to Use This Repository

### Viewing the Documentation
For local viewing of the HTML documentation (including graph visualization), we recommend opening the `cpm` directory via a local web server (e.g., using the *Live Server* extension in VS Code or via Python `python -m http.server`) to prevent browser script blocking (CORS).

### Data Validation
To verify whether your PROV data meets the requirements of this model, run the `cpm-shapes.ttl` file against your data graph using any standard SHACL validator (e.g., the `pyshacl` library or the online [SHACL Playground](https://shacl.org/playground/)). You can safely use `example.ttl` as a sample data graph to test the validator's strictness and functionality.
