print("\nWelcome to the Bill Splitter\n")
amt = float(input("Enter your total bill amount(in Rs.): "))
tax = float(input("Enter the tax percentage(in %): "))
tip = float(input("Enter the tip percentage(in %): "))
people = int(input("Enter the number of people to split the bill among: "))

if amt<1 or tax<=0 or tip<=0 or people<1:
    print("Invalid data!")
    exit()


tax = (tax/100)*amt
tip = (tip/100)*amt
individual_bill = (amt + tax + tip)/people

print(f"\nTotal bill amount: Rs. {amt:.2f}")
print(f"\nTax applied: Rs. {tax:.2f}")
print(f"\nTotal tip paid: Rs. {tip:.2f}")
print(f"\nNumber of people: {people}")
print(f"\nIndividual bill: Rs. {individual_bill:.2f}")