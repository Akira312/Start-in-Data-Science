import time as t
def benchmark(func):
    start=t.time()
    func()
    stop=t.time()
    print(stop-start)

@benchmark
def function():
    s=0
    for i in range(10000000):
        s+=i
    return s
