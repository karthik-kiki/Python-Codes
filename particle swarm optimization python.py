from random import randint
inp=[-9.6,-6,-2.6,-1.1,0.6,2.3,2.8,8.3,10]
v=[0,0,0,0,0,0,0,0,0]
func1=[]
func2=[]
pbest=[-9.6,-6,-2.6,-1.1,0.6,2.3,2.8,8.3,10]
newpb=[]
start=0
c1=1.0
c2=1.0
def fx(a):
    return[-(i*i)+(5*i)+20 for i in a]
def velocity():
    crts1=[]
    crts2=[]
    pmi=[pbest-inp for pbest,inp in zip(pbest,inp)]
    gmi=[gb-i for i in inp]
    for i in pmi:
        crt1=c1*r1*i
        crts1.append(crt1)
    for i in gmi:
        crt2=c2*r2*i
        crts2.append(crt2)
    global vi
    vi=[i+j+k for i,j,k in zip(v,crts1,crts2)]
    return vi
def newval():
    global xnew
    xnew=[i+j for i,j in zip(inp,vi)]
    return xnew
while(start<3):
    print("the initail input vector is",[round(i,3)for i in inp])
    print("initial velocity is",[round(i,3)for i in v])
    c=fx(inp)
    func1.extend(c)
    print("objective function values is",[round(i,3)for i in func1])
    print("best values are",[round(i,3)for i in pbest])
    pb=max(c)
    print("max value from function",pb)
    gb=inp[c.index(pb)]
    print("global max value is",gb)
    r1=randint(100,999)/1000
    print("1st random value is",r1)
    r2=randint(100,999)/1000
    print("2nd random value is",r2)
    print("new velocity value is",[round(i,3)for i in velocity()])
    print("new input value is",[round(i,3)for i in newval()])
    d=fx(xnew)
    func2.extend(d)
    print("new objective function values is",[round(i,3)for i in func2])
    inp.clear()
    inp.extend(xnew)
    newpb.clear()
    for i in range(len(func1)):
        if(func2[i]<=func1[i]):
            newpb.append(str(pbest[i]))
        else:
            newpb.append(str(inp[i]))
    newpb=[float(i)for i in newpb]
    print("New best values are",[round(i,3)for i in newpb])
    pbest.clear()
    pbest.extend(newpb)
    func1.clear()
    func2.clear()
    v.clear()
    v.extend(vi)
    print("\n")
    start+=1
