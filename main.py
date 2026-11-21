
print("STUDENT RESULT ANALYZER")

name = input("Enter your name: ")

subjects = ["Python", "Physics", "Mathematics", "English"]
marks = []

for subject in subjects:
    print(f"Enter marks for {subject}")
    mark = int(input("Enter marks: "))
    marks.append(mark)

total = sum(marks)
percentage = total / 4

print("\n----- STUDENT RESULT -----")

print("Name:", name)

for i in range(len(subjects)):
    print(subjects[i], ":", marks[i])

print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 90:
    print("Grade: A")
elif percentage >= 75:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
elif percentage >= 40:
    print("Grade: D")
else:
    print("Grade: F")

print("--------------------------")

