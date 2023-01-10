evenlist=[11,6,9,2,13,26,49,39]
print("list items=",evenlist)

for ev in evenlist:
    if(ev%2==0):
        evenlist.remove(ev)
print("list items after removing even numbers=",evenlist)
