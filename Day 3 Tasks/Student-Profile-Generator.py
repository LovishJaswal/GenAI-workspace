print("\nWelcome to the Student Profile Generator\n")
name = input("Please enter your name here: ")
age = int(input("Kindly enter your age: "))
grade = int(input("Enter your percentage(%): "))
while grade <= 0 or grade >= 100:
    print("Enter a valid percentage!")
    grade = input("Enter your percentage(%): ")

print(f"\nHi {name}, here's your insights- ")
if grade >= 33:
    print("\nResult status: Pass")
else:
    print("\nResult status: Fail")

if grade >= 90 and grade <= 100:
    print("Grade: A")
    print("Outstanding! Keep shining and aim even higher.")
elif grade >= 75 and grade < 90:
    print("Grade: B")
    print("Great job! A little more effort can take you to the top.")
elif grade >= 60 and grade < 75:
    print("Grade: C")
    print("Good work! Stay consistent and keep improving.")
elif grade >= 45 and grade < 60:
    print("Grade: D")
    print("You are getting there. Don't give up and keep practicing.")
elif grade >= 33 and grade < 45:
    print("Grade: E")
    print("You passed! Work harder and you'll do much better next time.")
elif grade < 33:
    print("Grade: F")
    print("Failure is not the end. Learn from mistakes and try again.")