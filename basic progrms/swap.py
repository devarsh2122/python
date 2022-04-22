# Python program to swap two numbers 
# without using temporary variable

# take inputs
a = input('Enter the value of a: ')
b = input('Enter the value of b: ')

print('Values Before Swapping')
print('a = ',a, 'and b = ',b)

# swap the value
a, b = b, a

# display swapping values
print('Values After Swapping')
print('a = ',a, 'and b = ',b)