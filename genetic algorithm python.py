from statistics import mean
import random
def fitness(x1,x2,x3,x4,x5,x6,x7,x8):
    x=(x1+x2)-(x3+x4)+(x5+x6)-(x7+x8)
    return x
li1=[]
li2=[]
li3=[]
li4=[]
for i in range(8):
    li1.append(random.randint(0,9))
    li2.append(random.randint(0,9))
    li3.append(random.randint(0,9))
    li4.append(random.randint(0,9))
a=fitness(li1[0],li1[1],li1[2],li1[3],li1[4],li1[5],li1[6],li1[7])
b=fitness(li2[0],li2[1],li2[2],li2[3],li2[4],li2[5],li2[6],li2[7])
c=fitness(li3[0],li3[1],li3[2],li3[3],li3[4],li3[5],li3[6],li3[7])
d=fitness(li4[0],li4[1],li4[2],li4[3],li4[4],li4[5],li4[6],li4[7])
print("the 1st sequence is",li1)
print("the 2nd sequence is",li2)
print("the 3rd sequence is",li3)
print("the 4th sequence is",li4)
e=[a,b,c,d]
a=0
while a<3:
    print("fitness values are",e)
    mx=max(e)
    print("max fittest value is",mx)
    smx=sorted(e)[-2]
    print("second fittest value is",smx)
    tmx=sorted(e)[-3]
    print("Third fittest value is",tmx)
    print("\n")
    if (mx==e[3]):
        mlist=li4[:]
    elif(mx==e[2]):
        mlist=li3[:]
    elif(mx==e[1]):
        mlist=li2[:]
    else:
        mlist=li1[:]
        
    if (smx==e[3]):
        smlist=li4[:]
    elif(smx==e[2]):
        smlist=li3[:]
    elif(smx==e[1]):
        smlist=li2[:]
    else:
        smlist=li1[:]

    if (tmx==e[3]):
        tmlist=li4[:]
    elif(tmx==e[2]):
        tmlist=li3[:]
    elif(tmx==e[1]):
        tmlist=li2[:]
    else:
        tmlist=li1[:]
    print("max fittest row is",mlist)
    print("2nd max fittest row is",smlist)
    print("3rd max fittest row is",tmlist)
    print("\n")
    print("One point crossover of max 2 lists")
    os1=mlist[0:4]+smlist[4:8]
    print("offspring 1 is",os1)
    os2=smlist[0:4]+mlist[4:8]
    print("offspring 2 is",os2)
    print("\n")
    print("Two point crossover of 1st and 3rd max lists")
    os3=mlist[0:2]+tmlist[2:6]+mlist[6:8]
    os4=tmlist[0:2]+mlist[2:6]+tmlist[6:8]
    print("offspring 3 is",os3)
    print("offspring 4 is",os4)
    print("\n")
    u=fitness(os1[0],os1[1],os1[2],os1[3],os1[4],os1[5],os1[6],os1[7])
    v=fitness(os2[0],os2[1],os2[2],os2[3],os2[4],os2[5],os2[6],os2[7])
    w=fitness(os3[0],os3[1],os3[2],os3[3],os3[4],os3[5],os3[6],os3[7])
    x=fitness(os4[0],os4[1],os4[2],os4[3],os4[4],os4[5],os4[6],os4[7])
    final=[u,v,w,x]
    print("The fitness values of offsprings",final)
    av=mean(final)
    print("The average value of offspring",av)
    print("\n")
    print("Optimal solution is improved and the final max fitness value is",max(final))
    print("\n")
    e.clear()
    e.append(u)
    e.append(v)
    e.append(w)
    e.append(x)
    a+=1
    
