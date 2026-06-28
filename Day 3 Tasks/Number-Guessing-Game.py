import random
print("\nWelcome to the number guessing game\n")
num = random.randrange(1, 101)
print("Computer has generated a random number(Between 1-100)")
guess = None
cnt = 0
while guess != num:
    guess = int(input("Try guessing it here: "))
    diff = abs(guess - num)
    cnt+=1
    if diff < 10 and guess < num:
        print("You're almost there! Go a bit higher")
    elif diff < 10 and guess > num:
        print("You're almost there! Go a bit lower")
    elif diff < 50 and guess < num:
        print("Close, but still low")
    elif diff < 50 and guess > num:
        print("Close, but still high")
    elif diff < 100 and guess < num:
        print("Way too low")
    elif diff < 100 and guess > num:
        print("Way too high")
    else:
        print("\nCongratulations!, you're spot on")
        print("You have guessed the number correctly")
        print(f"Number of tries: {cnt}")