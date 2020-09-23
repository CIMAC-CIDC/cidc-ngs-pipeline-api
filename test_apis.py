#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests each output API against the output API schema"""

import jsonschema
import os
import pytest
from json import load


API_ENDING = "_output_API.json"
SCHEMA_FILE_NAME = "output_API.schema.json"


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCHEMA_PATH = os.path.join(BASE_DIR, SCHEMA_FILE_NAME)

with open(SCHEMA_PATH, "r") as f:
    try:
        schema = load(f)
    except Exception as e:
        raise Exception(f"Failed loading json {SCHEMA_PATH}") from e


def test_schema():
    """Ensure the output_API.schema.json conforms to JSON Schema Draft 7"""
    jsonschema.Draft7Validator.check_schema(schema)




validator = jsonschema.Draft7Validator(schema)

def api_paths():
    """Get the path to every output_API.json in the schemas directory"""
    return (
        os.path.join(dname, fname)
        for dname, _, files  in os.walk(BASE_DIR)
            for fname in files
                if fname.endswith(API_ENDING)
    )


@pytest.mark.parametrize("api_path", api_paths(), ids=lambda x: x.split("/")[-1])
def test_api(api_path):
    """Ensure the output_API.json file conforms to schema"""
    with open(api_path, "r") as f:
        try:
            validator.validate(load(f))
        except Exception as e:
            raise Exception(f"Failed loading json {SCHEMA_PATH}") from e
