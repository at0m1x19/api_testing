BASE_URL = 'https://dog.ceo/api'

LIST_ALL_BREEDS = '/breeds/list/all'
RANDOM_IMAGE = '/breeds/image/random'


def get_by_breed_endpoint(breed):
    return f'/breed/{breed}/images'


def get_list_sub_breed_endpoint(breed):
    return f'/breed/{breed}/list'
