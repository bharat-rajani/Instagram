import time


def bench(func):

    def wrapper(*args, **kwargs):

        _start = time.time()
        value = func(*args, **kwargs)
        _end = time.time()
        _elapsed = _end - _start
        now = time.strftime("%H:%M:%S %d-%m-%Y")
        print(f'[{now}]- Function \'{func.__name__}\' took {_elapsed} seconds.')

        return value

    return wrapper

