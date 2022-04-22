# Python program to print fibonacci series up to n-th term

# take input
num = int(input('Enter number of terms: '))

# print fibonacci series
a, b = 0, 1
   
# check if the number of terms is valid
if num <= 0:
    print('Please enter a positive integer.')

elif num == 1:
    print('The Fibonacci series: ')
    print(a)

else:
    print('The Fibonacci series: ')
    for i in range (1, num+1):
        print(a, end=' ')
        c = a + b
        a = b
        b = c