#Merge two dictionaries
dict1 = {'a': 100, 'b': 200}
dict2 = {'x': 300, 'y': 200}

dict3 = {**dict1, **dict2}
print("dictinary 1 :",dict1)
print("dictinary 2 :",dict2)
print("Merged dictionary :",dict3)