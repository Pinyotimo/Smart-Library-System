# utils.py
import functools
import datetime

def track_access(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] Called {func.__name__} with args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper


def permission_check(required_role):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            if getattr(self, "role", None) == required_role:
                return func(self, *args, **kwargs)
            else:
                raise PermissionError(f"Access denied. {required_role} role required.")
        return wrapper
    return decorator


def borrow_item(item):
    if hasattr(item, "title"):
        print(f"{item.title} borrowed successfully!")
    else:
        raise TypeError("Item must have a title attribute.")