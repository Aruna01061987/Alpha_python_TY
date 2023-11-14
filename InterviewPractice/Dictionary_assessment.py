from collections import defaultdict

""" Write a program to get the indexes of each item in the below list
names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'google', 'gmail', 'gmail', 'gmail']
output should be -  {'apple': [0, 2], 'google': [1, 5], 'yahoo': [3, 4], 'gmail': [6, 7, 8]}
"""

names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'google', 'gmail', 'gmail', 'gmail']
names_dict = defaultdict(list)

for index, item in enumerate(names):
    names_dict[item] += [index]
print(names_dict)

""" Reverse the values in the dictionary if the value is of type String"""
d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}

for key, value in d.items():
    if isinstance(value, str):
        d[key] = value[::-1]
    else:
        d[key] = value
print(d)

"""Write a program to get all the duplicate items and the number of times the item is repeated in the list."""
names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'facebook', 'apple', 'gmail', 'gmail', 'gmail', 'gmail']
dd = {}
for name in names:
    if names.count(name) > 1:
        dd[name] = names.count(name)
print(dd)


"""Creating Dictionary of city and population pairs using Dict Comprehension"""
cities = ['Tokyo',  'Delhi',  'Shanghai',   'Sao Paulo',  'Mumbai']
population = ['38,001,000',  '25,703,168',  '23,740,778',   '21,066,245',  '21,042,538']

city_pop = zip(cities, population)
dd = dict(city_pop)
print(type(city_pop))
print(dict(dd))
city = {key: value for key, value in city_pop}
print(type(city))
print(city)

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)

print(d)








