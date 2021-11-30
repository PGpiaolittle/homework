import logging
import random
import time
from functools import wraps

def handle_error(re_raise=True, log_traceback=True, exc_type=Exception, tries=1, delay=0.0, backoff=1):
    def handler(func):
        @wraps(func)
        def wrapper():
            _tries = tries
            _delay = delay
            try:
                return func()
            except exc_type as e:
                while _tries > 0:
                    _tries -= 1
                    time.sleep(delay)
                    _delay = _delay * backoff
                    try:
                        return func()
                    except BaseException:
                        _tries -= 1
        return wrapper
    return handler
@handle_error( re_raise =True , tries =3 , delay =0.5 , backoff =2 )
def some_function():
    x = 1 / 0
if __name__ == '__main__':
    some_function()
    print(1)  #
    some_function()
    print(1)  #
