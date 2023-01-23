test='onion'
print("the orginal string is:"+ str(test))
o='$'
res=test.replace(test[0],o).replace(o,test[o],1)
print("replaced string:"+ str(res))
