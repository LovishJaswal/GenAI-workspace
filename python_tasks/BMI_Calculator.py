print("\nHi, Welcome to the BMI calculator\n")

weight = float(input("Enter your weight(in Kgs): "))
if weight < 2:
    print("Enter a valid weight!")
    exit()
height = float(input("Enter your height(in cms): "))
if(height < 20):
    print("Enter a valid height: ")
    exit()

height = height/100 #converted cms to m
bmi = weight/(height*height)

print(f"Your BMI is {bmi:.1f}")
if bmi<18.5:
    print("You are curretly underweight. Consult a good nutritionist")
elif bmi >= 18.5 and bmi < 25:
    print("You are at normal weight range")
elif bmi >= 25 and bmi < 30:
    print("You are overweight! Watch out for health risks")
elif bmi >= 30:
    print("You are Obese! Try consulting a good doctor")