D = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
     'emp2': {'name': 'Kim', 'job': 'Dev'},
     'emp3': {'name': 'Sam', 'job': 'Dev'}}

for id,info in D.items():
    print("\nEmployee ID:", id)
    for key in info:
        print(key + ':', info[key])

