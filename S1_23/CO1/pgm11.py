list_num=(input("enter list of integer"));
list_num2=list_num.split()
print(list_num2)
list_num2=int(list_num2)
k=100
ch="over"
res=[ch if ele > k else ele for ele in list_num2]
print(res)
