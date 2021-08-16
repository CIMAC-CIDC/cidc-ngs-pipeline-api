## What

Describe very concisely what this Pull Request does.

## Why

Describe what motivated this Pull Request and why this was necessary. Use closing keywords to link to the relevant Issue. Ex. Closes #666

## Remarks

Add notes on possible known quirks/drawbacks of this.

## Mentions

Person responsible for reviewing proposed changes.

## Checklist

Please include and complete the following checklist. Your Pull Request is (in most cases) not ready for review until the following have been completed. You can create a draft PR while you are still completing the checklist. You can mark an item as complete with the `- [x]` prefix

- [ ] Formatting & Linting - `black` and `flake8` have been used to ensure styling guidelines are met
- [ ] Type Annotations - New code has been type annotated in the function signatures using type hints
- [ ] Documentation - Short and long descriptions of files which have been updated in the schema. Docstrings have been provided for functions
- [ ] Tests - Added unit tests for new code
- [ ] Package version - Manually bumped the package version in [cidc_ngs_pipeline_api/__init__.py](https://github.com/CIMAC-CIDC/cidc-ngs-pipeline-api/blob/master/cidc_ngs_pipeline_api/__init__.py#L9)
