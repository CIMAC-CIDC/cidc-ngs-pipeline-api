#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests each output API against the output API schema"""

import jsonschema
import pytest

from cidc_ngs_pipeline_api import METASCHEMA, OUTPUT_APIS


def test_schema():
    """Ensure the output_API.schema.json conforms to JSON Schema Draft 7"""
    jsonschema.Draft7Validator.check_schema(METASCHEMA)


validator = jsonschema.Draft7Validator(METASCHEMA)


@pytest.mark.parametrize(
    "schema", [pytest.param(v, id=k) for k, v in OUTPUT_APIS.items()]
)
def test_api(schema):
    """Ensure the output_API.json file conforms to schema"""
    errors = list(validator.iter_errors(schema))  # Iterable[ValidationError]

    # check that long_description isn't just short_description repeated
    if "run id" not in schema:  # exclude wes
        for k, v in schema.items():
            for n, d in enumerate(v):
                if (
                    not d["long_description"]
                    .replace(d["short_description"], "")
                    .strip()
                ):
                    errors.append(
                        f"/{k}/{n} {d['file_path_template']} needs a long_description"
                    )

    assert len(errors) == 0, "\n".join([str(e) for e in errors])
