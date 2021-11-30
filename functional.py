from abc import ABCMeta


class BoundedMeta(type):
    _counter = {}
    _max_instance_count = None

    def __new__(mcs, name, bases, dict, max_instance_count):
        mcs._counter[name] = 0
        mcs._max_instance_count = max_instance_count
        return super().__new__(mcs, name, bases, dict)

    def __call__(cls):
        cls._counter[cls.__name__] += 1
        if cls._max_instance_count is not None and cls._counter[cls.__name__] > cls._max_instance_count:
            raise TypeError
        else:
            return super().__call__()

#
def smart_function():
    pass


class C(metaclass=BoundedMeta, max_instance_count=2):
    pass

if __name__ == '__main__':
    c1 = C()
    c2 = C()
    try:
        c3 = C()
    except TypeError:
        print('everything works fine !')
    else:
        print('something goes wrong !')





