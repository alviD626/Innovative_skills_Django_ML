import sys
 
# sample lists
list1 = [1, 2, 3, 5 , 'a']
list2 = ["ML", "based", "web"]
 
# print the sizes of sample lists
print("Size of list1 index0: " + str(sys.getsizeof(list1[0])) + "bytes")
print("Size of list1 index1: " + str(sys.getsizeof(list1[1])) + "bytes")
print("Size of list1 index2: " + str(sys.getsizeof(list1[2])) + "bytes")
print("Size of list1 index3: " + str(sys.getsizeof(list1[3])) + "bytes")
print("Size of list1 index4: " + str(sys.getsizeof(list1[4])) + "bytes\n\n")


print("Size of list2 index0: " + str(sys.getsizeof(list2[0])) + "bytes")
print("Size of list2 index1: " + str(sys.getsizeof(list2[1])) + "bytes")
print("Size of list2 index2: " + str(sys.getsizeof(list2[2])) + "bytes")