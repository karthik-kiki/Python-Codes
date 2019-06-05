fname=open("stud.txt","r")
words=0
lines=0
chars=0
my_word=input("enter the word to be searched:")
count=0
for i in fname:
    word=i.split()
    lines+=1
    words+=len(word)
    chars+=len(i)
    for j in word:
        if j==my_word:
            count+=1 
print("total lines are:",lines)
print("total words are:",words)
print("total letters are:",chars)
print(my_word,"is {} times".format(count))
    
