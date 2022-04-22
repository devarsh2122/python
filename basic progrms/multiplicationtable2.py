# Python program to print multiplication table in range

# take inputs
print('Display multiplication table')
start = int(input('Start: '))
end = int(input('End: '))

# print multiplication table
for i in range (start, end+1):
    print('\n\nMultiplication table of %d\n' %(i))
    for j in range(1, 11 ):
        print('%d * %d = %d\t' %(i, j, i*j))