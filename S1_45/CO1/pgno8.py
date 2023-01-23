test='onion'
print("The original string is:" +str(test))
o='$'
res=test.replace(test[0],o).replace(0,test[0],1)
print("replaced string is:" + str(res))
