marks = list(map(int, input("Enter marks in Physics, Chemistry, Biology, Mathematics and Computer: ").split()))
percentage = 0
for i in marks:
    if i < 0 or i > 100:
        print("Invalid marks entered")
        exit(-1)
    else:
        percentage += i
percentage = percentage/len(marks)
if percentage >= 90:
    print("Grade A")
elif 80 <= percentage < 90:
    print("Grade B")
elif 70 <= percentage < 80:
    print("Grade C")
elif 60 <= percentage < 70:
    print("Grade D")
elif 40 <= percentage < 60:
    print("Grade E")
else:
    print("Grade F")
