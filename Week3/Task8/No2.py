# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# score = int(input("Enter your test score: "))

# eligibility = (age < 18) and (score > 70)
# print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")

'''The code is trying to get the name, age and score of students that are eligible'''

# Adapt the code to the case below
citizenship = input("Your citizenship status: ").lower()
enrollement = input("Are you an undergraduate in a well known university: ").lower()
scholarships = input("Any other scholarship in the oil and gas industry: ").lower()
academic_qualification = input("Do you have five distinctions: ").lower()

eligibility = (citizenship == "nigeria") and (enrollement == "yes") and (scholarships == "no") and (academic_qualification == "yes")

print(f"Citizenship: {citizenship}\nEnrollement: {enrollement}\nScholarship: {scholarships}\nAcademic Qualification: {academic_qualification}\nEligible: {eligibility}")

