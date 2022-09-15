import time
from numba import njit

@njit
def fibonacci_loop(n):
    a, b = 1, 0
    for _ in range(n):
        a, b = b, a + b

def main():
    start = time.time()
    fibonacci_loop(1000000)
    print(f'{time.time() - start}s')

if __name__ == '__main__':
    main()
