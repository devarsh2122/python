D = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
     'emp2': {'name': 'Kim', 'job': 'Dev'},
     'emp3': {'name': 'Sam', 'job': 'Dev'}}

print(D['emp1']['name'])
# Prints Bob
print(D['emp1']['job'])
# Prints Mgr

print(D['emp2']['name'])
# Prints Kim
print(D['emp2']['job'])
# Prints Dev

print(D['emp3']['name'])
# Prints Sam
print(D['emp3']['job'])
# Prints Dev

print(D['emp1'].get('salary'))
# Triggers KeyError: 'salary'

print(D['emp1'].get('name'))