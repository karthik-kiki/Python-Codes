print("Bank Transaction")
use=int(input("How many account holder do we have?:"))
start=0
while start<use:
    def user_name():
        name=input("Enter card holder name :").upper()
        for i in name:
            if (i.isalpha()or i.isspace())==True:
                print("Hello {}".format(name))
                break
            else:
                print("Invalid name")
                user_name()
    def bank_name():
        user_name()
        print("Total Banks available are:")
        print("1.SBI")
        print("2.ICICI")
        print("3.HDFC")
        print("4.BOI")
        global user
        user=int(input("In which bank among the above do u have the account?:"))
    def bank_select():
        bank_name()
        if(user==1):
            print("You have account in SBI")
            sbi=int(input("Enter your 11 digit account number:"))
            if(len(str(sbi))==11):
                print("Your 11 digit account number is",sbi)
            else:
                print("Invalid account number")
                bank_select()
        elif(user==2):
            print("You have account in ICICI")
            icici=int(input("Enter your 12 digit account number:"))
            if(len(str(icici))==12):
                print("Your 12 digit account number is",icici)
            else:
                print("Invalid account number")
                bank_select()
        elif(user==3):
            print("You have account in HDFC")
            hdfc=int(input("Enter your 13 or 14 digit account number:"))
            if(len(str(hdfc))==13)or(len(str(hdfc))==14):
                print("Your 13 or 14 digit account number is",hdfc)
            else:
                print("Invalid account number")
                bank_select()
        elif(user==4):
            print("You have account in BOI")
            boi=int(input("Enter your 15 digit account number:"))
            if(len(str(boi))==15):
                print("Your 15 digit account number is",boi)
            else:
                print("Invalid account number")
                bank_select()
        else:
            print("Sorry!! This bank doesnt exist")
    def bank_bal():
        bank_select()
        bal=int(input("Enter your amount balance in the account:"))
        print("Your account balance is",bal)
    def expend():
        bank_bal()
        expe=int(input("Enter your average monthly expenditure:"))
        print("Your monthly expenditure is",expe)
    def salary():
        expend()
        global sal
        sal=int(input("Enter your monthly salary:"))
        print("Your monthly salary is",sal)
    def loan():
        salary()
        if sal>=15000:
            print("As your salary is {},you are eligible for loan".format(sal))
        else:
            print("As your salary is {},you are not eligible for loan".format(sal))
    loan()
    print("\n")
    start+=1
