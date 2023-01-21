#Enter 2 lists of integers. Check(a) Whether list are of same length(b) whether list sums to same value(c) whether any value occur in both

#Enter 2 lists of integers. Check 

list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [11,12,13,14,15,16,17,18,19,20]

# (a) Whether list are of same length
if len(list1) == len(list2):
    print("List 1 and List 2 are of same length")
else:
    print("List 1 and List 2 are not of same length")
print("List 1 ", len(list1))
print("List 2 ", len(list2))

# (b) whether list sums to same value
if sum(list1) == sum(list2):
    print("List 1 and List 2 sums to same value")
else:
    print("List 1 and List 2 sums to different value")
print("List 1 sum ", sum(list1))
print("List 2 sum ", sum(list2))

# (c) whether any value occur in both
if list1 == list2:
    print("List 1 and List 2 are same")
else:
    print("List 1 and List 2 are not same")
print("List 1 ", list1)
print("List 2 ", list2)
