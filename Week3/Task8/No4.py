student = {}
student_name = input("Enter your name: ")
age = int(input("Enter your age: "))
student["Student Name"]=student_name
student["Student Age"]= age

# score = int(input("Input your score: "))
list_of_score = [60, 65, 70, 75, 80]
student["Scores"]= list_of_score

average_score = sum(list_of_score)/len(list_of_score)
passed = average_score >= 50
student["Passed"] = passed

teenager = (age >= 13) and (age <= 19)
print(f"     Student Details:\nName: {student["Student Name"]}\nAge: {student["Student Age"]}\nPassed: {student["Passed"]}\nTeenager: {teenager}")