mark = int(input('enter the marks: '))

m_percentage = (mark/100)*100

if mark >= 80:
    grade = "A+"
    point = 5.00
    range = "80% - 100%"
elif mark>=70 and mark<=79:
    grade = "A"
    point = 4.00
    range = "70% - 79%"
elif mark>=60 and mark<=69:
    grade = "A-"
    point = 3.50
    range = "60% - 69%"
elif mark>=50 and mark<=59:
    grade = "B"
    point = 3.00
    range = "50% - 59%"
elif mark>=40 and mark<=49:
    grade = "C"
    point = 2.00
    range = "40% - 49%"
elif mark>=33 and mark<=39:
    grade = "D"
    point = 1.00
    range = "33% - 39%"
else:
    grade = "F"
    point = 0.00
    range = "0% - 32%"
    
print(f"Mark in percentage: {m_percentage}% \nGrade: {grade} \nPoint: {point} \nRange: {range}")