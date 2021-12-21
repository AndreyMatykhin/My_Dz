import sys
from time import perf_counter

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
start = perf_counter()
result = [src[i] for i in range(1, len(src)) if src[i] > src[i - 1]]
print(f'{type(result)}, {sys.getsizeof(result)}, {result}, {perf_counter() - start}')
start = perf_counter()
gen_result = (src[i] for i in range(1, len(src)) if src[i] > src[i - 1])
print(f'{type(gen_result)}, {sys.getsizeof(gen_result)}, {list(gen_result)}, {perf_counter() - start}')
