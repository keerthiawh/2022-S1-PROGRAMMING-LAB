str =input("Enter the text")
c = dict()
txt = str.split(" ")
for t in txt:
	if t in c:
		c[t] += 1
	else:
		c[t] = 1
print(c)
