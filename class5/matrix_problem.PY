
import math
r = int(input("Enter the row number: "))
c = int(input("Enter the column number: "))

matrixx = []
print("Enter the elements")


# i = row ; j = column
for i in range(r):
    a = []
    for j in range(c):
        a.append(int(input()))
    matrixx.append(a)

print("\nInput: ")
for i in range(r):
    for j in range(c):
        print(matrixx[i][j],end=" ")
    print()

# Initialize empty matrices for output
output1 = []
output2 = []
output3 = []
output4 = []

for row in matrixx:
    row1 = []
    row2 = []
    
    for number in row:
        #Calculate matrix for output1
        row1.append(number % 10)

        #Calculate matrix for output2
        if number % 2 == 0:
            row2.append("Even")
        else:
            row2.append("Odd")
     
    output1.append(row1)
    output2.append(row2)
    
    #Calculate matrix for output3
    for i in range(len(output1)):
        row_sum = sum(output1[i])

    #Calculate matrix for output4
    if row_sum % 2 == 0:
        output4.append("Even")
    else:
        output4.append("Odd")
    
    output3.append(row_sum)
    
    
def matrix_print(matrix_lst):
    for i in range(len(matrix_lst)):
        for j in range(len(matrix_lst[i])):
            print(matrix_lst[i][j], end=" ")
        print()

# Print the output matrix using the matrix_print function
print("\nOutput 1: ")
matrix_print(output1)

print("\nOutput 2: ")
matrix_print(output2)


print("\nOutput 3: ")
for num in output3:
    print(num, end=" ")

print("\n\nOutput 4: ")
for value in output4:
    print(value, end=" ")