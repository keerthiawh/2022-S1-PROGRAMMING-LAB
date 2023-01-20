test='onion'
print("the original string is:"+str(test))
o='$'
res=test.replace(test[0],o).replace(o,test[0],1)
print("replaced string:"+str(res))
