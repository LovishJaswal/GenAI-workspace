string = input("\nEnter your string: ")
Frequency_Counter = {}
for x in string:
    if x == ' ':
        continue
    Frequency_Counter[x] = 0

i = 0
while i < len(string):
    if string[i] == ' ':
        i+=1
        continue
    Frequency_Counter[string[i]]+=1
    i+=1

for key in Frequency_Counter:
    print(key, "*"*Frequency_Counter[key])