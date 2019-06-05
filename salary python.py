office=["manager","supervisor","worker"]
print("total staff:")
staff=int(input())
print("enter basic sal:")
basicsal=float(input())
if(basicsal>50000):
    da=(70*basicsal)/100
    print("da is :",da)
elif(50000>basicsal>2500):
    da=(50*basicsal)/100
    print("da is :",da)
elif(basicsal<2500):
    da = (40 * basicsal) / 100
    print("da is :",da)
else:
    print("wrong salary")
print("enter post:")
post=input().lower()
if post in office:
        if(post=="manager"):
            hra=(25*basicsal)/100
            print("hra is :",hra)
        elif(post=="supervisor"):
            hra=(20*basicsal)/100
            print("hra is :", hra)
        elif(post=="worker"):
            hra=(15*basicsal)/100
            print("hra is :", hra)
        else:
            print("invalid post")
else:
    print("invalid choice")
print("netsal is :",basicsal+hra+da)

