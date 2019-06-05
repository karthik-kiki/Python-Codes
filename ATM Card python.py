from random import randint
print("ATM CARD")
user=int(input("How many users exist?:"))
start=0
while start<user:
    def cardname():
        cname=[]
        name=input("Enter card holder name :").upper()
        for i in name:
            if (i.isalpha()or i.isspace())==True:
                cname.append(name)
                break
            else:
                print("Invalid name")
                cardname()
        print(cname)
    def cardnum():
        cardname()
        global num
        num=int(input("Enter the 16 digit card number:"))
        if(len(str(num))==16):
            print("Your card number is",num)
        else:
            print("Invalid card number")
            cardnum()
    def cardtype():
        cardnum()
        nums=str(num)
        cnums1=[nums[0:2]]
        res1=[int(i)for i in cnums1]
        cnums2=[nums[0]]
        res2=[int(i)for i in cnums2]
        check1=[51,52,53,54,55]
        check2=[4]
        for i in res1:
            if i in check1:
                print("Your card is mastercard")
            else:
                for i in res2:
                    if i in check2:
                        print("Your card is visa")
                    else:
                        print("Invalid card number")
                        cardnum()

    def expiry():
        cardtype()
        print("Your expiry date is",randint(1,12),randint(20,50),sep='/')
    def cvv():
        expiry()
        print("Your cvv number is",randint(100,999))
    def phno():
        cvv()
        ph=[]
        global pnum
        pnum=int(input("Enter 10 digit phone number:"))
        if len(str(pnum))==10:
            print("Phone number is valid")
            ph.append(pnum)
        else:
            print("Invalid Phone number")
    def otp():
        phno()
        print("otp generated is",randint(100000,999999))
    otp()
    print("\n")
    start+=1
