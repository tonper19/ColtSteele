'''
returns a sorted list of a passed collection
'''
numbers = [4,6,2,78,11,9,0,1]
# by default sorted returns a list sorted in ascending order
sorted_numbers = sorted(numbers)
print('*** Sorted numbers in ascending order')
print(sorted_numbers)
print('')

# the collection can be sorted in descending order
reversed_sorted = sorted(numbers, reverse = True)
print('*** Sorted numbers in descending order')
print(reversed_sorted)
print('')

# passing a tuple of strings
names = ('Tony', 'Ana', 'Annabelle', 'Miguel')
sorted_names = sorted(names)
print('*** Sorted strings in ascending order')
print(sorted_names)