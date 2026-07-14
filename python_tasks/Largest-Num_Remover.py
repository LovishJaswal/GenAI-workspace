print("\nWelcome to the largest number remover from a list\n")
data = []
data= input("Enter the values of list separated by a comma: ").split(",")
data = [int(x) for x in data]

while(len(data)) != 0:
    max = 0
    for i in data:
        if i>max:
            max = i
    data.remove(max)
    print(data)