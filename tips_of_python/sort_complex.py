data = [3,6,8,1,5,9]

sorted_data = sorted(data, reverse = True)

print(sorted_data)

data = [{'name': 'Max', 'age': 8},
        {'name': 'Lisa', 'age': 5},
        {'name': 'Tom', 'age': 11}]

sorted_data = sorted(data, key=lambda x : x['age'])

print(sorted_data)

data = [{'nick': 'agi1','id': 1},
        {'nick': 'agi1','id': 12},
        {'nick': 'agi1','id': 5}]

sorted_data = sorted(data, key=lambda x : x["id"])

print(sorted_data)