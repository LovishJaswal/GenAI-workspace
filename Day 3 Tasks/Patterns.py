num = int(input("\nKindly enter the value of n(n must be odd): "))


#Diamond pattern without using nested loops

print("\nDiamond pattern without using nested loops\n")
i = num
j = 1

while i >=1:
    i-=1
    print(i*" " + j*"*" + i*" ")
    j+=2

i+=1
j-=2

while i < num:
    j-=2
    print(i*" " + j*"*" + i*" ")
    i+=1


#Diamond pattern using nested loops

print("\nDiamond pattern using nested loops\n")
for x in range(1, 2):
    for y in range(num-1, -1, -1):
        print(y*" " + x*"*" + y*" ")
        x+=2

for x in range(num+(num-1), num+(num-1)+1):
    for y in range(1, num):
        x-=2
        print(y*" " + x*"*" + y*" ")


#Star pattern using nested loops

print("\nStar pattern using nested loops\n")
for x in range(1, 2):
    for y in range(1, num+1):
        if y%5 == 0:
            print("***")
        elif y%2 == 0:
            print("**")
        elif y%2 != 0:
            print("*")

#Inverted star pattern using nested loops

print("\nInverted star pattern using nested loops\n")
for x in range(1, 2):
    for y in range(num, 0, -1):
        if y%5 == 0:
            print("***")
        elif y%2 == 0:
            print("**")
        elif y%2 != 0:
            print("*")