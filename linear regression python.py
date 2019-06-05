print("The value of x is")
x=[int(i) for i in input().split(',')]
print("The value of y is")
y=[int(i) for i in input().split(',')]
meanx=0;meany=0
for i in x:
    meanx=meanx+i
    mx=meanx/len(x)
for i in y:
    meany=meany+i
    my=meany/len(y)
xnew=[];ynew=[]
xw=0;yw=0;xs=0
xdeno=[]
for i in x:
    xw=i-mx
    xs=(i-mx)*(i-mx)
    xnew.append(xw)
    xdeno.append(xs)
for i in y:
    yw=i-my
    ynew.append(yw)
xy=[xnew[i]*ynew[i] for i in range(len(xnew))]
xysum=0
xyadd=[]
for i in xy:
    xysum+=i
    xyadd.append(xysum)
xdenoadd=[]
xdenosum=0
for i in xdeno:
    xdenosum+=i
    xdenoadd.append(xdenosum)
w1=xyadd[-1]/xdenoadd[-1]
w0=my-(w1*mx)
exp=int(input("Experience in years:?"))
res=w0+w1*exp
print("salary is",res)
