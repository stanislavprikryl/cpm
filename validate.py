#!/usr/bin/env python3
"""
SHACL validation script for the CPM artifact suite.
Validates each PROV bundle in example.trig per-bundle against cpm-shapes.ttl,
loading cpm.ttl as the OWL ontology for RDFS subclass inference.

Usage:
    pip install rdflib pyshacl
    python3 validate.py

Expects in current directory:
    cpm.ttl
    cpm-shapes.ttl
    example.trig
"""
from rdflib import Dataset, Graph
from pyshacl import validate
import sys


def main():
    ds = Dataset()
    ds.parse('example.trig', format='trig')

    shapes_g = Graph()
    shapes_g.parse('cpm-shapes.ttl', format='turtle')
    onto_g = Graph()
    onto_g.parse('cpm.ttl', format='turtle')

    print("=== Per-bundle SHACL validation of CPM-conformant FPCs ===\n")
    all_pass = True
    for ctx in ds.graphs():
        name = ctx.identifier
        if str(name) == 'urn:x-rdflib:default':
            continue
        bundle_g = Graph()
        for s, p, o in ctx:
            bundle_g.add((s, p, o))
        if len(bundle_g) == 0:
            continue

        conforms, _, txt = validate(
            data_graph=bundle_g, shacl_graph=shapes_g, ont_graph=onto_g,
            inference='rdfs', advanced=True,
        )
        status = "PASS ✓" if conforms else "FAIL ✗"
        print(f"Bundle <{name}>: {len(bundle_g)} triples — {status}")
        if not conforms:
            all_pass = False
            print(txt)
            print()

    print(f"\n=== OVERALL: {'PASS ✓' if all_pass else 'FAIL ✗'} ===")
    sys.exit(0 if all_pass else 1)


if __name__ == '__main__':
    main()
