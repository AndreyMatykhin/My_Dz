def val_checker(verbosity=None):
    def _val_checker(func):
        def wrapper(*args):
            try:
                if len(list(filter(verbosity, args))):
                    return func(*filter(verbosity, args))
                else:
                    raise ValueError(f"wrong val {''.join(str(*args))}")
            except ValueError as e:
                print(f'ValueError: {e}')

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(-7))
print(calc_cube(7))
