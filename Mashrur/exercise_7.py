class Fibonacci:

    def __init__(self, max_number):
        self.max_number = max_number
        self.previous = 0
        self.current = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.previous, self.current = self.current, self.current + self.previous
        if self.previous >= self.max_number:
            raise StopIteration
        return self.previous


def fib(max_number):
        previous, current = 0, 1
        while previous < max_number:
            yield previous
            previous, current = current, current + previous



for num in fib(100):
    print(num, end=' ')