# Add up all odd numbers between 10 and 20
# Store the result in x:
sum_of_odd_numbers = 0
sum_of_even_numbers = 0

# YOUR CODE GOES HERE:

for number in range(1, 10):
    if number % 2 == 1:
        sum_of_odd_numbers = sum_of_odd_numbers + number
    else:
        sum_of_even_numbers = sum_of_even_numbers + number

print(f'the sum of odd numbers is {sum_of_odd_numbers}')
print(f'the sum of even numbers is {sum_of_even_numbers}')
