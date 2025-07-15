import requests
def access_nested_map(nested_map, path):
    for key in path:
        try:
            nested_map = nested_map[key]
        except (KeyError, TypeError):
            raise KeyError(key)
    return nested_map




def get_json(url):
    return requests.get(url).json()

