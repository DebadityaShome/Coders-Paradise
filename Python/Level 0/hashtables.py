items1 = dict({"key1" : 1, "key2" : 2, "key3" : "three"})
print(items1)

print(items1["key2"])

items1["key2"] = "two"
print(items1)

# Iterating the keys and values in the dictionary
for key, value in items1.items():
    print("Key: ", key, " value: ", value)
