# Create a dictionary to store employee record
D = {'name': 'Bob',
     'age': 25,
     'job': 'Dev',
     'city': 'New York',
     'email': 'bob@web.com'}
print(D)

# Create a dictionary with a list of two-item tuples
L = [('name', 'Bob'),
     ('age', 25),
     ('job', 'Dev')]

D = dict(L)
print(D)
# Prints {'name': 'Bob', 'age': 25, 'job': 'Dev'}


# Create a dictionary with a tuple of two-item lists
T = (['name', 'Bob'],
     ['age', 25],
     ['job', 'Dev'])

D = dict(T)
print(D)
# Prints {'name': 'Bob', 'age': 25, 'job': 'Dev'}

#When the keys are simple strings, it is sometimes easier to specify key:value pairs using keyword arguments.
D = dict(name = 'Bob',
         age = 25,
         job = 'Dev')

print(D)
# Prints {'name': 'Bob', 'age': 25, 'job': 'Dev'}
