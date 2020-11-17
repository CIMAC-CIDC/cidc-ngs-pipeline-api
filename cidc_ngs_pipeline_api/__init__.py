# -*- coding: utf-8 -*-

import os
from json import load


__author__ = """Stephen C van Nostrand"""
__email__ = "vannost@ds.dfci.harvard.edu"
__version__ = "0.1.5"


_API_ENDING = "_output_API.json"
_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
_SCHEMA_PATH = os.path.join(_BASE_DIR, "output_API.schema.json")


try:
    with open(_SCHEMA_PATH, "r") as f:
        METASCHEMA = load(f)
except Exception as e:
    raise Exception(f"Failed loading json {_SCHEMA_PATH}") from e

OUTPUT_APIS = {}
for dname, _, files in os.walk(_BASE_DIR):
    for fname in files:
        if fname.endswith(_API_ENDING):
            analysis = dname.split("/")[-1]
            with open(os.path.join(dname, fname), "rb") as f:
                OUTPUT_APIS[analysis] = load(f)
