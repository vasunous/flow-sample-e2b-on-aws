# E2B SDK Test Suite

This repository contains a test suite for verifying compatibility and functionality of the [E2B on AWS](https://github.com/aws-samples/sample-e2b-on-aws). The tests are designed to validate core functionality and identify compatibility issues across different SDK versions.

## Overview

These tests verify the E2B SDK's capabilities for sandbox environments, ensuring that critical features function as expected. The test suite is forward-compatible and designed to work with future SDK versions that fully implement the documented functionality.

## Current Test Status

### Passing Tests
- Commands execution
- Environment variables management
- Filesystem operations
- Internet access (inbound portion)
- Sandbox lifecycle operations
- Basic sandbox metadata operations

### Known Compatibility Issues
- `Sandbox.list()` method fails with a "'state'" error when attempting to list sandboxes
- Both `test_sandbox_listing` and `test_sandbox_metadata` encounter issues related to this incompatibility
- Full internet access testing requires an external HTTP client for verification

## Usage

To run the tests:

```bash
python -m pytest test_e2b_sdk.py -v
```

Tests that are incompatible with the current SDK version will be gracefully skipped with detailed error information.