grades = []
passed = 0

print("Enter grades for the students")

while True:
    grade_input = input("Enter grade: ")

    if grade_input == "done":
     break
    elif (int(grade_input) > 30) and (int(grade_input) < 101):
        grades.append(int(grade_input))
        if int(grade_input) > 74:
            passed +=1
    else: break


for num in grades:
    total = 0
    total += num

if len(grades) != 0:
    pass_percentage = (passed / len(grades)) * 100
    print("Class average grade:", round(total/len(grades)))
    print ("Percentage of students who passed:", round(pass_percentage, 2) , "%")
    print("Passed: ", passed)      