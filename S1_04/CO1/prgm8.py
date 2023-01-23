test = input("enter a string")
print("The original string is : " + str(test))
o = '$'
res = test.replace(test[0], o).replace(o, test[0], 1)
print("Replaced String : " + str(res))
