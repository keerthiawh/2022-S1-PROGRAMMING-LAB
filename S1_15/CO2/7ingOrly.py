#Add ‘ing’ at the end of a given string. If it already ends with ‘ing’, then add ‘ly’

str1 = input("Enter the string : ")
for i in str1:
    if str1[-3:] == 'ing':
        print(str1+"ly")
        break
    else:
        print(str1+"ing")
        break