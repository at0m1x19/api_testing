list_all_breeds_schema = {
    'message': {'type': 'dict', 'required': True},
    'status': {'type': 'string', 'required': True}

}

random_image_schema = {
    'message': {'type': 'string', 'required': True},
    'status': {'type': 'string', 'required': True}
}

by_breed_schema = {
    'message': {'type': 'list', 'required': True},
    'status': {'type': 'string', 'required': True}
}

list_all_sub_breed_schema = {
    'message': {'type': 'list', 'required': True},
    'status': {'type': 'string', 'required': True}
}
