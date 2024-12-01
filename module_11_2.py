import sys


def introspection_info(obj):
    info = {}
    info.update({f'type': type(obj).__name__})
    all_attrs = dir(obj)

    info['attributes'] = [attr for attr in all_attrs if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    info['methods'] = [method for method in all_attrs if callable(getattr(obj, method)) and not method.startswith("__")]
    if hasattr(obj, '__module__'):
        info['module'] = sys.modules[obj.__module__].__name__
    else:
        info['module'] = None
    return info


class Proba:
    def method_one(self):
        pass

    def method_two(self):
        pass

    attribute_one = 42
    attribute_two = "Hello"


obj = Proba()
print(introspection_info(obj))

print(introspection_info(42))