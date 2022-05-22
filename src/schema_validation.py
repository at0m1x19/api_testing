def assert_schema(response, schema, validator):
    if isinstance(response, list):
        for item in response:
            assert validator.validate(item, schema)
    elif isinstance(response, dict):
        assert validator.validate(response, schema)
    else:
        raise AssertionError(f'Unexpected response type: {response}')
