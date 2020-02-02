'''
Generator expressions are lighter than list comprehensions
'''

import sys
list_comp = sys.getsizeof([x * 10 for x in range(1000)])
gen_exp = sys.getsizeof(x * 10 for x in range(1000))

print(f'List comprehension: {list_comp} bytes')
print(f'Generator expression: {gen_exp} bytes')
