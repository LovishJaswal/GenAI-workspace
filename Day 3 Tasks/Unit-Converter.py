print("\nHi, Welcome to the Unit converter")
op = int(input("\nChoose the number corresponding to the type of conversion you want:\n1- Km to Miles. \n" \
"2- Kg to lbs. \n3- Celsius to Fahrenheit. \n4- USD to INR. \nEnter your choice here: "))
num = int(input("\nEnter the value: "))
if op == 1:
    print(f"{num} Km is {0.62*num} miles")
elif op == 2:
    print(f"{num} Kg is {2.20*num} lbs")
elif op == 3:
    print(f"{num} degrees celsius is {(num*9/5)+32} degree Fahrenheit")
elif op == 4:
    print(f"${num} is Rs. {num*95.39}")
else:
    print("Enter a valid number!")