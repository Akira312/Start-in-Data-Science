import time as t
import functools
def benchmark(func):
    def time(*args, **kwargs):
        start=t.time()
        func(*args, **kwargs)
        stop=t.time()
        print(f'Время выполнения функции составило {stop-start} секунд')
    return time

def logging(func):
    def log(*args, **kwargs):
        print(f'количество полученных элементов функцией составило: {len(args)}')
        func(*args, **kwargs)
    return log

def counter(func):
    def calls(*args, **kwargs):
        func(*args, **kwargs)
        if 
        print(f'количество итераций заданной функции составило {s} раз')
    return calls

@benchmark
@logging
@counter
def function(k): # logging(benchmark(function))
    s=0
    for i in range(k):
        s+=i
    return s
function(3923823)
