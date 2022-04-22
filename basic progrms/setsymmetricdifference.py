A = {'red', 'green', 'blue'}
B = {'yellow', 'red', 'orange'}

# by operator
print(A ^ B)
# Prints {'orange', 'blue', 'green', 'yellow'}

# by method
print(A.symmetric_difference(B))
# Prints {'orange', 'blue', 'green', 'yellow'}

