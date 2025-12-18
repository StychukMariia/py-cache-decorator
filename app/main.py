from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}
    def wrapper(*args, **kwargs):
        if (tuple(args), tuple(sorted(kwargs.items()))) in cache_dict:
            print("Getting from cache")
        else:
            cache_dict[(tuple(args), tuple(sorted(kwargs.items())))] = func(*args, **kwargs)
            print("Calculating new result")
        return cache_dict[(tuple(args), tuple(sorted(kwargs.items())))]
    return wrapper
