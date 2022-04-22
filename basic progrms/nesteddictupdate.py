D = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
     'emp2': {'name': 'Kim', 'job': 'Dev'},
     'emp3': {'name': 'Sam', 'job': 'Dev'}}

D['emp3']['name'] = 'Max'
D['emp3']['job'] = 'Administrtor'

print(D['emp3'])
# Prints {'name': 'Max', 'job': 'Admiistrator'}

print(D)


D = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
     'emp2': {'name': 'Kim', 'job': 'Dev'},
     'emp3': {'name': 'Sam', 'job': 'Dev'}}

D['emp3'] = {'name': 'Max', 'job': 'Janitor'}

print(D)

D = {'emp1': {'name': 'harsh', 'job': 'student'},
     'emp2': {'name': 'Ural', 'job': 'Developer'},
     'emp3': {'name': 'Yash', 'job': 'Mnager'}}
print(D)

D['emp4'] = {'name': 'Yash Patel', 'job': 'Student'}
print(D)