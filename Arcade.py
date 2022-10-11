import csv
import random
#Game1
def TicTacToe():
    pname.append(gamezone[g])
    #TicTacToe
    print('Welcome to Tic Tac Toe!!')
    print('In this game you place X and computer places 0')
    print('You win when X occupies 3 consecutive places')
    print('Computer wins when 0 occupies 3 consecutive places')
    print('Here we go!\n')
    key={1:'   ',2:'   ',3:'   ',4:'   ',5:'   ',6:'   ',7:'   ',8:'   ',9:'   '}
    l=[1,2,3,4,5,6,7,8,9]
    #Board for the game
    def board():
        print(key[7],key[8],key[9],sep='|')
        print('-+-+-')
        print(key[4],key[5],key[6],sep='|')
        print('-+-+-')
        print(key[1],key[2],key[3],sep='|')
    print('Positions are given by:')
    print('7|8|9')
    print('-+-+-')
    print('4|5|6')
    print('-+-+-')
    print('1|2|3')
    #Conditions for winning and losing
    global win,lose,points
    win=lose=0
    def winlosecheck():
        global win,lose
        if key[7]==key[8]==key[9]=='X' or key[4]==key[5]==key[6]=='X' or key[1]==key[2]==key[3]=='X':
            print('You have won!')
            win+=1
        elif key[7]==key[5]==key[3]=='X' or key[9]==key[5]==key[1]=='X':
            print('You have won!')
            win+=1
        elif key[7]==key[4]==key[1]=='X' or key[8]==key[5]==key[2]=='X' or key[9]==key[6]==key[3]=='X':
            print('You have won!')
            win+=1
        elif key[7]==key[8]==key[9]=='0' or key[4]==key[5]==key[6]=='0' or key[1]==key[2]==key[3]=='0':
            print('Computer wins!\nGame over')
            lose+=1
        elif key[7]==key[5]==key[3]=='0' or key[9]==key[5]==key[1]=='0':
            print('Computer wins!\nGame over')
            lose+=1
        elif key[7]==key[4]==key[1]=='0' or key[8]==key[5]==key[2]=='0' or key[9]==key[6]==key[3]=='0':
            print('Computer wins!\nGame over')
            lose+=1
    while True:
        if win==1 or lose==1:
            if win==1:
                points+=5
                print('Points:',points)
            break
        user=int(input('\nEnter position to put X: '))
        if user not in key:
            print('Invalid position try again')
            continue
        elif key[user]=='   ':
            key[user]='X'
            l.remove(user)
            board()
            winlosecheck()
            if l !=[]:
                comp=random.randint(1,9)
                while comp not in l:
                    comp=random.randint(1,9)
                else:
                    l.remove(comp)
            elif l==[] and win!=1 and lose!=1:
                print('Tie!')
                break
            if win!=1:
                print('\nComputer plays:')
                key[comp]='0'
                board()
                winlosecheck()
        elif key[user]!='   ':
            print('Invalid position try again')

#Game2
def StonePaperScissor():
    global points
    pname.append(gamezone[g])
    #StonePaperScissor
    opt=['STONE','PAPER','SCISSOR']
    plyr=com=0
    print("\nWelcome to STONE-PAPER-SCISSOR")
    #PermutAndCombiForTheResult
    while plyr<5 and com<5:
        choice=input("\nEnter your choice from STONE, PAPER, or SCISSOR: ")
        p=choice.upper()
        c=opt[random.randint(0,2)]
        print('You put ',p)
        print("Computer's move: ",c)
        if p==c:
            print("\nDraw")
        elif p=='STONE' and c=='PAPER':
            print('\nComputer wins this round')
            com+=1
        elif p=='STONE' and c=='SCISSOR':
            print('\nYou win this round')
            plyr+=1
        elif p=='PAPER' and c=='STONE':
            print('\nYou win this round')
            plyr+=1
        elif p=='PAPER' and c=='SCISSOR':
            print("\nComputer wins this round")
            com+=1
        elif p=='SCISSOR' and c=='PAPER':
            print("\nYou win this round")
            plyr+=1
        elif p=='SCISSOR' and c=='STONE':
            print("\nComputer wins this round")
            com+=1
        else:
            print("\nWrong Input")
        #Result
        print('\nPoints:')
        print("You: ",plyr,"\nComputer: ",com)
        if plyr==5:
            print("YOU WON THIS GAME !")
            points+=5
            print('Points awarded: ',points)
        elif com==5:
            print("YOU HAVE LOST THIS GAME !")
#Game3
def Hangman():
    global points
    #Hangman
    pname.append(gamezone[g])
    print("Hello Venz. Welcome to Hangman. You have 5 turns to guess the word. You will get 3 words to guess. All the best")
    hangcount=3
    while hangcount>0:
        print("\n")
        #ListOfWordsInThisGame
        words=['FACEMASK','BUILDING','THAILAND','FORMULA','EMIRATES','VARANDAH','SKYWALK','ALPHABET','QUALITY','CARPOOL','ESCALATOR','SCENT','SHELF','DOCTOR','TEAL','MEAT','FOLDER','UNCOPYWRITEABLE','BINOCULARS']
        t=len(words)
        op='True'
        rand=random.randint(0,t)
        while op=='True':
            i=words[rand]
            count=0
            n=len(i)
            print ("The word is ",n," letters long.")
            w=[]
            for j in range(n):
                w.append(' _ ')
                if i[j]=='A' or i[j]=='E' or i[j]=='I' or i[j]=='O' or i[j]=='U':
                    w[j]=i[j]
            def word():
                nord=''
                for k in w:
                    nord+=k
                return nord
            print(word())
            while count<=5:
                    y=input("Enter your letter (in capitals) : ")
                    if y in i:
                        print("CORRECT")
                        a=i.find(y)
                        w[a]=i[a]
                        word()
                        check=word()
                        print(check)
                        if check==i:
                            print("YOU HAVE GUESSED THE CORRECT WORD!")
                            points+=5
                            op='False'
                            break
                    else:
                        print("WRONG")
                        count+=1
                        if count==5:
                            print("ALL YOUR TURNS ARE DONE")
                            print ("THE CORRECT WORD IS: ",i)
                            op='False'
                            break
        hangcount-=1
#Game4
def QuizMaster():
    global points
    #QuizMaster
    score=0
    reward=0
    print("Welcome to KBC! You will be asked 10 questions. If you answer each of these correctly, it proves that you're smart. \nEnjoy the game!!")
    ask=input("Are you ready to play? ")
    if ask=='YES' or ask=='yes':
        print("OK. Lets start.")
        print("Enter the correct option (in capitals) or Type the exact option")
    else:
        print(" Give it a try, lets go! ")
        print(" Enter the correct option (in CAPITALS) or Type the exact option")
    answer1=input("\n1. Who is the current chairman of ISRO? \n\nA.Sathish Dhawan \nB.K.Sivan \nC.APJ Abdul Kalam \nD.U R Rao \nAnswer:  ")
    if answer1=="B" or answer1=="K.Sivan":
        score+=1
        reward+= 1000
        print("CORRECT!")
        print("SCORE:  ",score)
        print("REWARD:  ", reward)
    else:
        print("INCORRECT :( , correct answer is 'B'")
        print("SCORE:  ",score)
        print("REWARD:  ", reward)
    answer2=input("\n2.Which is the parent company of royal enfield? \n\nA.Eicher Motors \nB.Ashok Leyland \nC.Tata \nD.Mahindra \nAnswer:  ")
    if answer2=="A" or answer2=="Eicher Motors":
        score+=1
        reward+=1000
        print("CORRECT!")
        print("SCORE:  ",score)
        print("REWARD:  ", reward)
    else:
        print("INCORRECT :( !, correct answer is 'A'")
        print("SCORE:  ",score)
        print("REWARD:  ", reward)
    answer3=input("\n3.Who is known as the father of indian share market? \n\nA.Ratan Tata \nB.Mukesh Ambani \nC.Rakesh Jhunjunwala \nD.Adhithya Birla \nAnswer:  ")
    if answer3=="C" or answer3=="Rakesh Jhunjhunwala":
        score+=1
        reward+=1000
        print("CORRECT!")
        print("SCORE:  ",score)
        print("REWARD:  ", reward)
    else:
        print("INCORRECT :( !, correct answer is 'C'")
        print("SCORE:  ",score)
        print("REWARD:  ", reward)
    answer4=input("\n4.Who was the first indian actor who made his/her appearance in the mission impossible series?\n\nA.Akshay Kumar \nB.Rajnikanth \nC.Sharukh Khan \nD.Anil Kapoor \nAnswer:  ")
    if answer4=="D" or answer4=="Anil Kapoor":
        score+=1
        reward+=1000
        print("CORRECT!")
        print("SCORE:  ",score)
        print("REWARD:  ", reward)
    else:
        print("INCORRECT :( !, correct answer is 'D'")
        print("SCORE:  ",score)
        print("REWARD:  ", reward)
    answer5=input("\n5.How many compartments are there in a standard indian goods train? \n\nA.26 \nB.60 \nC.10 \nD.100 \nAnswer:  ")
    if answer5=="A" or answer5=="26":
        score+=1
        reward+=1000
        print("CORRECT!")
        print("SCORE:  ",score)
        print("REWARD:  ", reward)
    else:
        print("INCORRECT :( !, correct answer is 'A'")
        print("SCORE:  ",score)
        print("REWARD:  ", reward)
    answer6=input("\n6.What is the name of Ambani's residence in Mumbai \n\nA.One100 \nB.Antilia \nC.Kingfishers \nD.Orchid Springs \nAnswer:  ")
    if answer6=="B"or answer6=="Antilia":
        score+=1
        reward+=1000
        print("CORRECT!")
        print("SCORE:  ",score)
        print("REWARD:  ", reward)
    else:
        print("INCORRECT :( !, correct answer is 'B'")
        print("SCORE:  ",score)
        print("REWARD:  ", reward)
    answer7=input("\n7.What is the name of the train that runs between India and Pakisthan? \n\nA.Vivek Exp \nB.Lalbagh Exp \nC.Samjhautha Exp \nD.Intercity Exp \nAnswer:  ")
    if answer7=="C" or answer7=="Samjhautha Exp":
        score+=1
        reward+=1000
        print("CORRECT!")
        print("SCORE:  ",score)
        print("REWARD:  ", reward)
    else:
        print("INCORRECT :( !, correct answer is 'C'")
        print("SCORE:  ",score)
        print("REWARD:  ", reward)
    answer8=input("\n8.Which place is known as the needle tip of india? \n\nA.Kanyakumari \nB.Allepey \nC.Rameswaram \nD.Dhanushkodi \nAnswer:  ")
    if answer8=="D" or answer8=="Dhanushkodi":
        score+=1
        reward+=1000
        print("CORRECT!")
        print("SCORE:  ",score)
        print("REWARD:  ", reward)
    else:
        print("INCORRECT :( !, correct answer is 'C'")
        print("SCORE:  ",score)
        print("REWARD:  ", reward)
    answer9=input("\n9.Which indian food item is regarded as the national food of india? \n\nA.Khichidi \nB.Idli \nC.Chapathi \nD.Pani puri \nAnswer:  ")
    if answer9=="A" or answer9=="Khichidi":
        score+=1
        reward+=1000
        print("CORRECT!")
        print("SCORE:  ",score)
        print("REWARD:  ", reward)
    else:
        print("INCORRECT :( !, correct answer is 'A'")
        print("SCORE:  ",score)
        print("REWARD:  ", reward)
    answer10=input("\n10.When is engineer's day celebrated in India? \n\nA.Dec 5th \nB.Oct 26th \nC.Nov 12th \nD.Sept 15th \nAnswer:  ")
    if answer10=="D" or answer10=="sept 15th":
        score+=1
        reward+=1000
        print("CORRECT!")
        print("SCORE:  ",score)
        print("REWARD:  ", reward)
    else:
        print("INCORRECT :( !, correct answer is 'D'")
        print("SCORE:  ",score)
        print("REWARD:  ", reward)
    points=score
    print("TOTAL SCORE:  ",score)
    print("NET REWARD:  ",reward)
    print("Thank you for playing :) !!")

#Game5
def Mastermind():
    global points
    #MastermindV2.1
    pname.append(gamezone[g])
    print('\nWelcome to Mastermind!!!')
    print('In this game, you will have to find out a random number.')
    print('After each guess, the number of exact numbers used and the number of correct positions will be shown.')
    print('Your guess must be a 4 digit number without any digit repeated.')
    print('You have 12 tries to guess the number correctly.')
    print('All the best!')
    no=1
    r=1
    found=e=p=0
    while True:
        rep=0
        fix=random.randint(1000,9999)
        sfix=str(fix)
        for i in sfix:
            if sfix.count(i)>1:
                rep=1
        if rep==0:
            break
    while found==0 and no<=12:
        p=e=0
        r=1
        n=int(input('\nGuess :'))
        s=str(n)
        for i in s:
            if s.count(i)>1:
                print('No number should be repeated')
                r=0
                break
            continue
        if n==fix:
            print('Correct!')
            print('You have won the game in',no,'tries!!')
            points+=5
            found=1
        elif len(s)!=4:
            print('Invalid guess: Guess must be a 4 digit number')
            continue
        elif no==12:
            print('\nNumber of Chances over')
            print('The answer is :',fix)
            break
        elif found==0 and r==1:
            for i in range(0,4):
                if sfix[i]==s[i]:
                    p+=1
            print('Correct positions: ',p)
            for i in s:
                if i in sfix:
                    e+=1
            print('Exact numbers used: ',e)
            no+=1

#MainMenu
entry=0
mem=input("\nAre you a member of Game Zone? Answer using Y or N: ")
if mem=='N':
    print("To join Game Zone, enter your username and PIN code below.")
    username=str(input("Username in CAPITALS: "))
    pin=int(input("Enter a 2-digit PIN code: "))
    print("Succesfully registered")
    with open('Members.csv','a+') as f:
        w=csv.writer(f)
        w.writerow([username,pin])
else:
    print("Welcome to Gamezone")
while entry==0:
    a=input("\nEnter username in CAPITALS: ")
    b=int(input("Enter 2-digit PIN code: "))
    with open('Members.csv','r') as f:
        r=csv.reader(f)
        for row in r:
            if row !=[]:
                if row==[a,str(b)]:
                    print('You have logged in successfully')
                    entry=1
                    break
        if a not in row:
            print('Wrong username or pin. Please enter again')  
while entry==1:
    print("\nWelcome to Game Zone")
    print("We have 5 games available currently")
    rec=[]
    gamezone={1:'Tic Tac Toe',2:'Stone Paper Scissor',3:'Hangman',4:'Quiz Master',5:'Mastermind'}
    while True:
        print("\nMENU:")
        print("1. PLAY GAMES")
        print("2. CREDITS")
        print("3. RECORDS")
        print("4. EXIT Game Zone")
        plan=int(input("Enter the OPTION NUMBER of what would you like to do: "))
        if plan==1:
            name=a
            pname=[]
            print("If you succeed in a game, you'll get 5 points. You can view your points in the RECORDS section.")
            points=0
            while True:
                print("\nChoose your Game:")
                print("1. Tic Tac Toe")
                print("2. Stone Paper Scissor")
                print("3. Hangman")
                print("4. Quiz Master")
                print("5. Mastermind")
                print('6.Save and Return to Main Menu')
                print("7. Quit without playing")
                g=int(input("Enter the game no. : "))
                if g==1:
                    TicTacToe()
                elif g==2:
                    StonePaperScissor()
                elif g==3:
                    Hangman()
                elif g==4:
                    QuizMaster()
                elif g==5:
                    Mastermind()
                elif g==6:
                    if n!=0:
                        n=len(pname)
                        avg=points//n
                        rec=[name,points,avg]
                        with open('Records.csv','a+') as f:
                            w=csv.writer(f)
                            w.writerow(rec)
                        print("\nGO CHECK OUT YOUR SCORES IN THE RECORDS SECTION")
                        break
                else:
                    print("Back to Main Menu")
                    break
        if plan==2:
            print("\nThis program has been designed by: ")
            print("Charan Raja (12 B - Roll 12)")
            print("Soham S. Raut (12 B - Roll 35)")
            print("Yash H. Barve (12 B - Roll 40)")
        if plan==3:
            with open('Records.csv','r') as f:
                r=csv.reader(f)
                for i in r:
                    if i !=[]:
                        print('\nName:',i[0])
                        print('Score:',i[1])
                        print('Average Score:',i[2])
        if plan==4:
            print("Thank you for visiting Game Zone! Hope to see you soon :)")
            break
    break

