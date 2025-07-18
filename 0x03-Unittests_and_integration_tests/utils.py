#!/usr/bin/env python3
import requests


def access_nested_map(nested_map, path):
    """Traverse nested dictionary using a list of keys"""
    for key in path:
        nested_map = nested_map[key]
    return nested_map


def get_json(url):
    """Get JSON from the provided URL"""
    return requests.get(url).json()


def memoize(fn):
    """Decorator to cache the result of a property method"""
    attr_name = "_{}".format(fn.__name__)

    @property
    def wrapper(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)

    return wrapper
