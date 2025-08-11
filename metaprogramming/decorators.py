"""
Decorators are functions that modify the behavior of other functions or classes.
They wrap the target function or class and provide additional functionlity
"""

def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper


@uppercase_decorator
def greet(name: str) -> str:
    return f'Hello, {name}!'


if __name__ == '__main__':
    print(greet('nick'))
