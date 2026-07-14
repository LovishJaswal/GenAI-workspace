print("\nHi, Welcome to the salary calculator.\n")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age<18:
    print("Invalid age for you to get salary!")
    exit()
salary = int(input("Enter your salary(in Rs.): "))
if salary<1:
    print("Enter a valid salary!")
    exit()
print(f"\nHi {name}, here are your insights-\n")
if age<=60:
    print(f"{60-age} years until you turn 60")
else:
    print("You are passed 60")
print(f"Your annual salary is: Rs. {salary*12:.2f}")
print(f"Your monthly salary after 30% tax deduction is: Rs. {(70/100)*salary:.2f}")
