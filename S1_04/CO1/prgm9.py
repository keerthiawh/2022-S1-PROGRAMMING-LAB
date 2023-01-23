Create a string from input string where first and last word exchanged ??
str = input("input a string")
print(str)
str = str[-1]+str[1:-1]+str[0]
print(str)
