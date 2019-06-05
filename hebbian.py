x1=[float(i) for i in input().split() ]
x2=[float(i) for i in input().split() ]
x3=[float(i) for i in input().split() ]
w=[float(i) for i in input().split()]
user=int(input("how many cycles do you need?:"))
c=1;l=1
w1=[];w2=[];w3=[]
wnew=[];wnew1=[];wnew2=[]
def sgn(p):
    if p>0:
        return 1;
    else:
        return -1;
for m in range(user):
    net1=sum([i*j for i,j in zip(x1,w) ])
    print("net value is :",net1 )
    o=sgn(net1)
    print("objective value is",o)
    for i in x1:
        delw=c*o*i
        w1.append(delw)
    for j,k in zip(w,w1):
        wnew.append(j+k)
    print("new weight values are",wnew)
    print("\n")
    net2=sum([i*j for i,j in zip(x2,wnew) ])
    print("net value is :",net2 )
    o1=sgn(net2)
    print("objective value is",o1)
    for i in x2:
        delw1=c*o1*i
        w2.append(delw1)
    for j,k in zip(wnew,w2):
        wnew1.append(j+k)
    print("new weight values are",wnew1)
    print("\n")
    net3=sum([i*j for i,j in zip(x3,wnew1) ])
    print("net value is :",net3 )
    o2=sgn(net3)
    print("objective value is",o2)
    wnew2.clear()
    for i in x3:
        delw2=c*o2*i
        w3.append(delw2)
    for j,k in zip(wnew1,w3):
        wnew2.append(j+k)
    print("new weight values are",wnew2)
    w.clear();w1.clear();w2.clear();w2.clear();wnew.clear();wnew1.clear()
    w.extend(wnew2)
    print("\n")
