import time as t
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

s=0
def counter(func):
    def calls(*args, **kwargs):
        func(*args, **kwargs)
        s+=1
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
