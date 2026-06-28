sentence = input("\nEnter the sentence: ")
word = input("Enter the word: ")

x = 0
cnt = 0
new_sentence = ""
while(x<len(sentence)):
    if sentence[x] == word[0]:
        i = 0
        while i< len(word) and x<len(sentence):
            if word[i] != sentence[x]:
                break
            x+=1
            i+=1
            if i == len(word):
                cnt+=1
                while i>=1:
                    i-=1
                    new_sentence+=("*")
                i+=len(word)
            if cnt == 1 and i == len(word):
                print(f"\nThe character position at which the word firstly appear is: {x-i}")
    if x<len(sentence):
        new_sentence+=(sentence[x])
    x+=1
print(f"\n'{word}' appears {cnt} times in the given sentence")
print(f"\nYour new sentence is: {new_sentence}")