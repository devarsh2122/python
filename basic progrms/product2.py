# Python program to multiply three numbers using function

def product_num(num1, num2, num3):  #user-defind function
    num = num1 * num2 * num3   #calculate product
    return num   #return value

# take inputs
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))
num3 = float(input('Enter third number: '))

# function call
product = product_num(num1, num2, num3)

# print multiplication value
print("The product of number: %0.2f" %product)