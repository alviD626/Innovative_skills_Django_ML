import math

list1 = []
n = int(input("Enter the length of the list: "))
for i in range(n):
    i+=1
    element = int(input(f"element no. {i}: "))
    list1.append(element)
print("Elements: ",list1)
print(type(list1))


# using sample standard deviation formula

mean = sum(list1)/len(list1)
sqrt_func = ((x - mean)**2 for x in list1)
difference = len(list1)-1
summation = sum(sqrt_func) / difference
sample_standard_deviation= math.sqrt(summation)

print(f"Output: {float(round(sample_standard_deviation))}")


