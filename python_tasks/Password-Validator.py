print("\nWelcome to the password validator\n")
password = input("Enter your password here: ")
found_int = False
found_upper = False
found_spclch = False

if len(password) < 8:
    print("Error: Password must be 8 characters long!")

for x in password:
    try:
        x = int(x)
        found_int = True
        break
    except:
        pass
if found_int == False:
    print("Error: Password must contain a digit!")

for x in password:
    if x.isupper() == True:
        found_upper = True
        break
if found_upper == False:
    print("Error: Password must contain atleast one uppercase letter!")

for x in password:
    if x.isalnum() == False:
        found_spclch = True
        break
if found_spclch == False:
    print("Error: Password must contain atleast one special character!")

if found_int == True and found_spclch == True and found_upper == True and len(password) >= 8:
    print("\nEntered password is a valid password")