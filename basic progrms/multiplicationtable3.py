# Python program to print multiplication table

# take inputs
num = int(input('Display multiplication table of: '))

# print multiplication table
i = 1
while i <= 10:
    print ("%d * %d = %d" %(num, i, num * i))
    i = i+1