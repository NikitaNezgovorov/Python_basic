import datetime as dt
import time


def time_log(funk):
    def wrapper(*args, **kwargs):
        print(f'{dt.datetime.now()} : {funk.__name__} start')
        start = time.time()
        result = funk(*args, **kwargs)
        print(f'{dt.datetime.now()} : {funk.__name__} end {time.time() - start}')
        return result

    return wrapper


@time_log
def while_tic(n):
    while n:
        n -= 1

@time_log
@time_log
def for_tic(n):
    for _ in range(n):
        pass


for_tic(10**5)
# while_tic(10**5)
