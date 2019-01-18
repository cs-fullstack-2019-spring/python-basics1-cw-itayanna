def main():
    #problem1()
    #problem2()
    #problem3()
    problem4()


#this function prints my name is and the users name entered

def problem1():
    myName= "My name is "
    name= "I'Tayanna"
    print(myName,name)

#this function determins if the extra credit is too much or not enough based on its value compared to 20


def problem2():
    xtraCredit= int(input("how much extra credit did you learn?"))
    if (xtraCredit<5):
        print("thats not enough exctra credit")
    elif(xtraCredit>20):
        print("thats too much extra credit!")


#this function prints password is set if the passwords they enter match, if they dont it tells them

def problem3():
    pswd= input("enter a password")
    pswd2=input("re-enter password")
    if(pswd==pswd2):
        print("Password set")
    else:
        print("Passwords don't match")

#this function is a blackJack game kind of watered down becasue there is no option for face cards

def problem4():
    card1= int(input("Pick a card"))
    card2= int(input("Pick another card"))
    if(card1+card2==21):
        print("BLACKJACK!!")
    elif(card1+card2>21):
        print("BUST!!")
    elif(card1+card2<21):
        print("total",card2+card1)





if __name__ == '__main__':
    main()
