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


def memoize(fn):
    """Memoization decorator"""
    attr_name = "_{}".format(fn.__name__)

    @property
    def wrapper(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)

    return wrapper


