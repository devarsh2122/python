D = {'name': 'Bob',
     'age': 25,
     'job': 'Dev'}

# get all keys
#print(list(D.keys()))
Lkey=list(D.keys())
print(Lkey)
# Prints ['name', 'age', 'job']

# get all values
#print(list(D.values()))
Lvalue=list(D.values())
print(Lvalue)
# Prints ['Bob', 25, 'Dev']

# get all pairs
Litems=list(D.items())
print(Litems)
#print(list(D.items()))
# Prints [('name', 'Bob'), ('age', 25), ('job', 'Dev')]
