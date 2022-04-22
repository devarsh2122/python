# Python program to find the factorial of a number

# take input
num = int(input("Enter number: "))

# check number is positive, negative, or zero
if num < 0:
   print('Factorial does not exist for negative numbers')
elif num == 0:
   print('The factorial of 0 is 1')
else:
    # find factorial of a number
   fact = 1
   for i in range(1,num + 1):
       fact = fact*i
   print('The factorial of',num,'is',fact)