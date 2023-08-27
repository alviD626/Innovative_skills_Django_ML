mark = int(input('enter the marks: '))

if mark >= 80:
    print("A+")
elif mark>=75 and mark<=79:
    print("A")
elif mark>=70 and mark<=74:
    print("A-")
elif mark>=65 and mark<=69:
    print("B+")
elif mark>=60 and mark<=64:
    print("B")
elif mark>=55 and mark<=59:
    print("B-")
elif mark>=50 and mark<=54:
    print("C+")
elif mark>=45 and mark<=49:
    print("C")
elif mark>=40 and mark<=44:
    print("D")
else:
    print("F")