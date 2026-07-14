print("\nWelcome to the string checker\n")
string = input("Enter your string here: ")

cnt_ch = 0
cnt_vowels = 0
cnt_words = 0

for x in string:

    cnt_ch+=1

    if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' or \
    x == 'A' or x == 'E' or x == 'I' or x == 'O' or x == 'U':
        cnt_vowels+=1
    
    if x == " ":
        cnt_words+=1
print(f"\nThe entered string has {cnt_ch} characters, {cnt_words+1} words and {cnt_vowels} vowels")

rev_str = ""
x = len(string) - 1

while x>=0:
    rev_str+=string[x]
    x-=1

print(f"The reversed string is: '{rev_str}'")