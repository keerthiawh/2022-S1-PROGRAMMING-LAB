names=['David','Daniel','Christa','Jack','Emily']
count=0
for i in names:
    for j in i:
        if j == "a":
            count=count+1
print("occurrence of a in:",count)
