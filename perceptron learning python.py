x1=[float(i) for i in input().split() ]
x2=[float(i) for i in input().split() ]
x3=[float(i) for i in input().split() ]
w=[float(i) for i in input().split()]
d=[float(i) for i in input().split()]
c=0.1
user=int(input("how many cycles required?:"))
wnew=[];wnew1=[];wnew2=[]
w1=[];w2=[];w3=[]
for i in range(user):
    print("x1 values are :",x1)
    print("x2 values are :",x2)
    print("x3 values are :",x3)
    print("w values are :",w)
    print("d values are :",d)
    net1=sum([i*j for i,j in zip(x1,w) ])
    print("net value is :",net1 )
    def sgn(p):
        if p>0:
            return 1;
        else:
            return -1;
    o=sgn(net1)
    print("objective value is",o)
    for i in x1:
        if (d[0]==o):
            print("no correction required")
            wnew.extend(w)
            print("old weight values are",[round(i,3)for i in wnew])
        else:
            for j in x1:
                delw=c*(d[0]-o)*j
                w1.append(delw)
            for i,j in zip(w,w1):
                wnew.append(i+j)
        break
    print("new weight values are ",[round(i,3)for i in wnew])
    print("\n")
    net2=sum([i*j for i,j in zip(x2,wnew) ])
    print("net value is :",net2 )
    o1=sgn(net2)
    print("objective value is",o1)
    for i in x2:
        if(d[1]==o1):
            print("no correction required")
            wnew1.extend(wnew)
            print("old weight values are",[round(i,3)for i in wnew1])
            break
        else:
            for j in x2:
                delw1=c*(d[1]-o1)*j
                w2.append(delw1)
            for i,j in zip(wnew,w2):
                wnew1.append(i+j)
        break
    print("new weight values are ",[round(i,3)for i in wnew1])
    print("\n")
    net3=sum([i*j for i,j in zip(x3,wnew1) ])
    print("net value is :",net3 )
    o2=sgn(net3)
    print("objective value is",o2)
    for i in x3:
        if(d[2]==o2):
            print("no correction required")
            wnew2.clear()
            wnew2.extend(wnew1)
            print("old weight values are",[round(i,3)for i in wnew2])
        else:
            wnew2.clear()
            for j in x3:
                delw2=c*(d[2]-o2)*j
                w3.append(delw2)
            for i,j in zip(wnew1,w3):
                wnew2.append(i+j)
        break
    print("new weight values are ",[round(i,3)for i in wnew2])
    w.clear();w1.clear();w2.clear();w3.clear();wnew.clear();wnew1.clear()
    w.extend(wnew2)
    print("\n")
