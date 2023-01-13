test = input("Enter a string: ")
print("Original string : " + str(test))
o = '$'
res = test.replace(test[0], o).replace(o, test[0], 1)
print("Replaced string : " + str(res))