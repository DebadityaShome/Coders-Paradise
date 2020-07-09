items = ["apple", "pear", "orange", "banana", "apple","apple", "pear", "orange", "banana", "apple","apple", "pear", "orange", "banana", "apple", "orange"]

counter = dict()

for item in items:
    if (item in counter.keys()):
        counter[item] += 1
    else:
        counter[item] = 1

print(counter)