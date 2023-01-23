#Accept an integer n and compute n+nn+nnn.
n = int(input("Enter a number: "))
nn = int(str(n) + str(n))
nnn = int(str(n) + str(n) + str(n))
print(n + nn + nnn)

