'''
reverse iterables: put the last item of an iterable as the first, 
the second to last item as the second, and so on.

Not to be confused with sort descending.
'''

nums = [3, 1, 8, 3, 2, 7, 5]
reversed_object = reversed(nums) # this returns a reversed iterator object!
print(f'Original list: {nums}')
print(f'Reversed list: {list(reversed_object)}')

# reverse strings:
reversed_string = list(reversed('Hello World!'))
print(reversed_string)
# but... slicing works as well
reversed_string2 = 'Hello World!'[::-1]
print(reversed_string2)