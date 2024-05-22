import time as t
def benchmark(func):
    def time():
        start=t.time()
        print(func())
        stop=t.time()
        print(stop-start)
    return time

def logging(func):
    def log():
        pass
    return log

@logging
@benchmark
def function():
    s=0
    for i in range(9999999):
        s+=i
    return s
function()
