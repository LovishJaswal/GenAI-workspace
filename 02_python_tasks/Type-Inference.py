print("\nWelcome to a type Inference program\n")
val = input("Please enter any value: ")

try:
    val = int(val)
except:
    pass

if val == "True":
    val = True
elif val == "False":
    val = False

if type(val) == int:
    print("\nEntered value is an integer\n")
    print(f"{val} in float is {float(val):.2f}")
    print(f"{val} in boolean is {bool(val)}")
    print(f"{val} in string is {str(val)}")
elif type(val) == float:
    print("\nEntered value is a floating point number\n")
    print(f"{val} in integer is {int(val)}")
    print(f"{val} in boolean is {bool(val)}")
    print(f"{val} in string is {str(val)}")
elif type(val) == str:
    print("\nEntered value is a string\n")
    print(f"{val} in boolean is {bool(val)}")
    print("String is inconvertible to integer or float")
elif type(val) == bool:
    print("\nEntered value is a boolean\n")
    print(f"{val} in integer is {int(val)}")
    print(f"{val} in float is {float(val):.2f}")
    print(f"{val} in string is {str(val)}")
    