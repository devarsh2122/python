A = {'red', 'green', 'blue'}
B = {'yellow', 'red', 'orange'}

# by operator
print(A - B)
# Prints {'blue', 'green'}

# by method
print(A.difference(B))
# Prints {'blue', 'green'}

# by operator
print(B - A)
# Prints {yellow, orange}

# by method
print(B.difference(A))
# Prints {yellow, orange}
