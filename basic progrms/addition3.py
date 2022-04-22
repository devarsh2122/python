# Python program to add two numbers using function

def add_num(a,b):   #user-defined function
    sum = a + b   #adding numbers
    return sum   #return value

#taking input from the user
num1 = float(input('Enter first number : '))
num2 = float(input('Enter second number : '))

#function call
sum = add_num(num1, num2)
print('The sum of numbers {0} and {1} is {2}'.format(
              num1, num2, sum))
