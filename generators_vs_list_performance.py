"""
generators_vs_list_performance.py

compare the times to sum a sequence of numbers using a generator comprehension
and a list comprehension

Output:
*** generator comprehension calculating the sum of the first 9999999
49999999985000000001
*** list comprehension calculating the sum of the first 9999999
49999999985000000001
the generator comprehension took 595.0286509990692
the list comprehension took 599.2130289077759
"""

import time

generator_start_time = time.perf_counter()
print("*** generator comprehension calculating the sum of the first 9999999")
print(sum(n for n in range(9999999)))
generator_time = time.perf_counter() - generator_start_time

list_start_time = time.perf_counter()
print("*** list comprehension calculating the sum of the first 9999999")
print(sum(n for n in range(9999999)))
list_time = time.perf_counter() - list_start_time

print(f"the generator comprehension took {generator_time}")
print(f"the list comprehension took {list_time}")
print(f"Clock resolution: {time.get_clock_info('perf_counter').resolution}")
