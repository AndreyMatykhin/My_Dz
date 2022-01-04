from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} ({', '.join(f'{str(i)}: {type(i)}' for i in args)}"
              f"{', '.join(f'{str(j)}: {type(j)}' for j in kwargs)})")
        return func(*args)

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


print(calc_cube(5))
