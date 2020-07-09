
items = ["apple", "pear", "orange", "banana", "apple","apple", "pear", "orange", "banana", "apple","apple", "pear", "orange", "banana", "apple", "orange"]


filter = dict()

for key in items:
    filter[key] = 0

result = set(filter.keys())
print(result)