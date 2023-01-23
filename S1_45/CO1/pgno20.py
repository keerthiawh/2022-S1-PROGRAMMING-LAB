evenlist=[1,2,3,4,5,6,7,8,9]
print("list item=",evenlist)
for ev in evenlist:
    if(ev%2==0):
        evenlist.remove(ev)
print("List after removing even numbers=",evenlist)        
        
