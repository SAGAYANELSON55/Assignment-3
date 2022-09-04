import random
def playA():
        pg=input("\n\ndo you want to play the game(y/n)")
        if pg=='y' or pg =='n':
            return pg
        else:
            playA()
def guessGame():
    playagain='y'
    score=0
    while playagain=='y':
        
        
        Actualnum=random.randint(1,50)
        givennum=int(input("\nEnter the number between 1 to 50="))

        diff=Actualnum-givennum
        if diff==0:
            print("Its the same number, you get 50 points")
            score=score+50
            print("your updated score is",score)

        elif diff >=-5 and diff <=5:
            print("This number is very close to the real number")
            print("givennum=",givennum)
            print("Actualnum=",Actualnum)
            score=score+25
            print("Your updated score is ",score)
        elif diff>=-10 and diff<=10:
            print("This number is close to the real number")
            print("Actualnum=",Actualnum)
            print("givennum=",givennum)
            score=score+10
            print("Your updated score is",score)
        else :
            print("sorry your number didn't match")
            print("Actualnum=",Actualnum)
            print("givennum=",givennum)
        playagain=playA()
    else:
        print("final score is",score)
        

    
