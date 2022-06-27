brewery_schema = {
    'id': {'type': 'string', 'required': True},
    'name': {'type': 'string', 'required': True},
    'brewery_type': {'type': 'string', 'required': True},
    'street': {'type': 'string', 'required': True, 'nullable': True},
    'address_2': {'type': 'string', 'required': True, 'nullable': True},
    'address_3': {'type': 'string', 'required': True, 'nullable': True},
    'city': {'type': 'string', 'required': True},
    'state': {'type': 'string', 'required': True, 'nullable': True},
    'county_province': {'type': 'string', 'required': True, 'nullable': True},
    'postal_code': {'type': 'string', 'required': True, 'nullable': True},
    'country': {'type': 'string', 'required': True},
    'longitude': {'type': 'string', 'required': True, 'nullable': True},
    'latitude': {'type': 'string', 'required': True, 'nullable': True},
    'phone': {'type': 'string', 'required': True, 'nullable': True},
    'website_url': {'type': 'string', 'required': True, 'nullable': True},
    'updated_at': {'type': 'string', 'required': True},
    'created_at': {'type': 'string', 'required': True}
}

autocomplete_schema = {
    'id': {'type': 'string', 'required': True},
    'name': {'type': 'string', 'required': True}
}
