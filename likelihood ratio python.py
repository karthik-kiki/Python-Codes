from random import randint
print("Let's calculate likelihood ratio of tossing 2 dice")
rolls=[]
choice=int(input("How many times you want to roll?:"))
for i in range(choice):
    d=(randint(1,6),randint(1,6))
    rolls.append(d)
print(rolls)
s=len(rolls)
print("Total outcomes of rolling 2 dice {} times are {}".format(choice,s))
print("Let A and B be the event of addition of number greater or Lesser")
aval,bval=map(int,input("Enter event conditions for A and B:").split())
print("We have to check for addition of numbers greater than {} and lesser than {}".format(aval,bval))
a=[x for x in rolls if sum(x)>=aval]
b=[x for x in rolls if sum(x)<=bval]
print(sorted(a))
print(sorted(b))
proba,probb=(len(a)/s),(len(b)/s)
print("The probability of A is {} and probability of B is {}".format(round(proba,3),round(probb,3)))
proband=len(list(set(a)&set(b)))
print("Probability of A intersection B is",round((proband/s),3))
print("Probability of (A/B) is {} and (B/A) is {}".format(round((proband/probb),3),round((proband/proba),3)))
lratio=((proband/probb)/(proband/proba))
print("Likelihood ratio is",round((lratio),3))
