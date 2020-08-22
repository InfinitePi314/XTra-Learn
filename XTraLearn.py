import pickle
import random

def begin():
    print("Welcome to XTra Learn")
    startChoice=str(input("Type 0 to quit \nType 1 to learn capitals \nType 2 to learn math\n"))
    if startChoice=="0":
        quit()
    elif startChoice=="1":
        geography()
    elif startChoice=="2":
        mathMain()
    else:
        print("Invalid")
        begin()


def mathMain(): 
    print('Welcome to our math course!\n')


    #Variables
    checker2b = ""
    userchoiceb = ""
    #Functions
    def addcheck2b(x, y):
            num1b = random.randint(x, y)
            num2b = random.randint(x, y)
            global checker2b
            checker2b = "n"
            while checker2b == "n":
                    print("What is " + str(num1b) + " + " + str(num2b) + "?")
                    answer = input("Enter the answer: ")
                    if int(answer) == num1b + num2b:
                            print('\nCorrect!\n')
                            checker2b = "y"
                    else: 
                            print('\nIncorrect. Try Again.')
                            checker2b = "n"

    def subcheck2b(x, y):
            num1b = random.randint(x, y)
            num2b = random.randint(x, y)
            global checker2b
            checker2b = "n"
            while checker2b == "n":
                    if num1b > num2b:
                            print("What is " + str(num1b) + " - " + str(num2b) + "?")
                            answer = input("Enter the answer: ")
                            if int(answer) == (num1b - num2b):
                                    print('\nCorrect!\n')
                                    checker2b = "y"
                            else: 
                                    print('\nIncorrect. Try Again.')
                                    checker2b = "n"
                    else:
                            print("What is " + str(num2b) + " - " + str(num1b) + "?")
                            answer = input("Enter the answer: ")
                            if int(answer) == num2b - num1b:
                                    print('\nCorrect!\n')
                                    checker2b = "y"
                            else: 
                                    print('\nIncorrect. Try Again.')
                                    checker2b = "n"

    def mulcheck2b(x, y):
            num1b = random.randint(x, y)
            num2b = random.randint(x, y)
            global checker2b
            checker2b = "n"
            while checker2b == "n":
                    print("What is " + str(num1b) + " x " + str(num2b) + "?")
                    answer = input("Enter the answer: ")
                    if int(answer) == num1b * num2b:
                            print('\nCorrect!\n')
                            checker2b = "y"
                    else: 
                            print('\nIncorrect. Try Again.')
                            checker2b = "n"

    def divcheck2b(w, x, y, z):
            num1b = random.randint(w, x)
            num2b = random.randint(y, z)
            global checker2b
            checker2b = "n"
            while checker2b == "n":
                    if num1b > num2b:
                            print("What is " + str(num1b) + " ÷ " + str(num2b) + "?")
                            answer = input("Enter the answer: ")
                            if int(answer) == num1b // num2b:
                                    print('\nCorrect!\n')
                                    checker2b = "y"
                            else: 
                                    print('\nIncorrect. Try Again.')
                                    checker2b = "n"
                    else:
                            print("What is " + str(num2b) + " ÷ " + str(num1b) + "?")
                            answer = input("Enter the answer: ")
                            if int(answer) == num2b // num1b:
                                    print('\nCorrect!\n')
                                    checker2b = "y"
                            else: 
                                    print('\nIncorrect. Try Again.')
                                    checker2b = "n"

    def additionb():
            print("\nAddition is defined as the process or skill of calculating the total of\ntwo or more numbers or amount.\n")
            print("Adding single digit numbers is simple.\n")
            print('Here are some examples:\n1 + 2 = 3\n5 + 7 = 12\n8 + 3 = 11\n')
            print("\nYour turn!\n")
            for x in range (4):
                    addcheck2b(1, 9)
            print('Congratulations for getting all of the single-digit problems correct.\n')
            print('Now on to double digit addition.\n')
            print('Adding double digit numbers is a little more complex.\n')
            print('Here are some examples:\n13 + 15 = 28\n24 + 37 = 61\n48 + 41 = 89')
            print("\nYour turn!\n")
            for x in range (4):
                    addcheck2b(10, 99)
            print('Congratulations for getting all of the double-digit problems correct.\n')
            print('Now on to mixed practice 1.\n')
            print("\nMixed Practice 1:\n")
            for x in range (5):
                    addcheck2b(1, 99)
            print('Congratulations for getting all of the mixed practice 1 problems correct.\n')
            print('Now on to three-digit problems.\n')
            print("Here it gets even more complex.\n")
            print("Here are some examples: \n105 + 269 = 374\n341 + 525 = 896\n800 + 100 = 900")
            print("\nYour turn!\n")
            for x in range(4): 
                    addcheck2b(100, 999)
            print('Congratulations for getting all of the triple-digit problems correct.\n')
            print("Now for some more mixed practice.")
            print("\nMixed Practice 2:\n")
            for x in range(5):
                    addcheck2b(1,999)
            print("Congratulations. You have completed the addition part of this course!\n")
            teach()

    def subtractb():
            print("\nSubtraction is defined as the process or skill of taking one number or amount away from another.\n")
            print("Subtracting single digit numbers is simple.\n")
            print('Here are some examples:\n2 - 1 = 1\n7 - 5 = 2\n8 - 3 = 5')
            print("\nYour turn!\n")
            for x in range (4):
                    subcheck2b(1, 9)
            print('Congratulations for getting all of the single-digit problems correct.\n')
            print('Now on to double digit subtraction.\n')
            print('Subtracting double digit numbers is a little more complex.\n')
            print('Here are some examples:\n15 - 13 = 2\n37 - 24 = 13\n48 - 41 = 7')
            print("\nYour turn!\n")
            for x in range (4):
                    subcheck2b(10, 99)
            print('Congratulations for getting all of the double-digit problems correct.\n')
            print('Now on to mixed practice 1.\n')
            print("\nMixed Practice 1:\n")
            for x in range (5):
                    subcheck2b(1, 99)
            print('Congratulations for getting all of the mixed practice 1 problems correct.\n')
            print('Now on to three-digit problems.\n')
            print("Here it gets even more complex.\n")
            print("Here are some examples: \n269 - 105 = 164\n525 - 371 = 154\n800 - 100 = 700")
            print("\nYour turn!\n")
            for x in range(4): 
                    subcheck2b(100, 999)
            print('Congratulations for getting all of the triple-digit problems correct.\n')
            print("Now for some more mixed practice.")
            print("\nMixed Practice 2:\n")
            for x in range(5):
                    subcheck2b(1,999)
            print("Congratulations. You have completed the subtraction part of this course!\n")
            teach()

    def multiplyb():
            print("\nMultiplication is defined as the process or skill of dividing one number by another.\n")
            print("Multiplying single digit numbers is simple.\n")
            print('Here are some examples:\n2 x 1 = 2\n6 x 3 = 18\n8 x 3 = 24\n')
            print("\nYour turn!\n")
            for x in range (4):
                    mulcheck2b(1, 9)
            print('Congratulations for getting all of the single-digit problems correct.\n')
            print('Now on to double digit multiplication.\n')
            print('Multiplying double digit numbers is a little more complex.\n')
            print('Here are some examples:\n45 x 15 = 675\n34 x 17 = 578\n97 x 10 = 970')
            print("\nYour turn!\n")
            for x in range (4):
                    mulcheck2b(10, 99)
            print('Congratulations for getting all of the double-digit problems correct.\n')
            print('Now on to mixed practice 1.\n')
            print("\nMixed Practice 1:\n")
            for x in range (5):
                    mulcheck2b(1, 99)
            print('Now on to three-digit problems.\n')
            print("Here it gets even more complex.\n")
            print("Here are some examples: \n269 x 15 = 17\n525 x 37 = 14 \n800 x 80 = 10")
            print("\nYour turn!\n")
            for x in range(4): 
                    mulcheck2b(100, 999)
            print('Congratulations for getting all of the triple-digit problems correct.\n')
            print("Now for some more mixed practice.")
            print("\nMixed Practice 2:\n")
            for x in range(5):
                    mulcheck2b(1,999)
            print("Congratulations. You have completed the multiplication part of this course!\n")
            teach()

    def divideb():
            print("\nDivision is defined as the process or skill of dividing one number by another.\n")
            print("Dividing single digit numbers is simple.\n")
            print('Here are some examples:\n2 ÷ 1 = 2\n6 ÷ 3 = 2\n8 ÷ 3 = 2\n')
            print("\nYour turn!\nUse floor division: in other words, calculate the answer and leave out any remainder.\n")
            for x in range (4):
                    divcheck2b(1, 9, 1, 9)
            print('Congratulations for getting all of the single-digit problems correct.\n')
            print('Now on to double digit division.\n')
            print('Dividing double digit numbers is a little more complex.\n')
            print('Here are some examples:\n45 ÷ 15 = 3\n34 ÷ 17 = 2\n97 ÷ 10 = 9')
            print("\nYour turn!\n")
            for x in range (4):
                    divcheck2b(1, 9, 10, 99)
            print('Congratulations for getting all of the double-digit problems correct.\n')
            print('Now on to three-digit problems.\n')
            print("Here it gets even more complex.\n")
            print("Here are some examples: \n269 ÷ 15 = 17\n525 ÷ 37 = 14 \n800 ÷ 80 = 10")
            print("\nYour turn!\n")
            for x in range(4): 
                    divcheck2b(10, 99, 100, 999)
            print('Congratulations for getting all of the triple-digit problems correct and completing the division part of this course.\n')
            teach()

    def teach():
            userchoiceb = str(input("Press 1 for Addition Problems\nPress 2 for Subtraction Problems\nPress 3 for Multiplication Problems\nPress 4 for Division Problems\n Or type exit to return to main menu \nEnter your choice: "))
            if userchoiceb == "1":
                    additionb()
            elif userchoiceb == "2":
                    subtractb()
            elif userchoiceb == "3":
                    multiplyb()
            elif userchoiceb == "4":
                    divideb()
            elif userchoiceb.lower() == "exit":
                begin()
            else:
                    print("Error. Try again.")
                    teach()
    teach()

def geography():
    def beginGeography():
        print("Welcome to GeoLearner!")
        geographyChoice=str(input("Type 0 to return to main screen \nType 1 to search up world capitals \nType 2 to take a quiz on world capitals\n"))
        if geographyChoice=="0":
            begin()
        elif geographyChoice=="1":
            geoDatabase()
        elif geographyChoice=="2":
            geoQuiz()
        else:
            print("Invalid")
            beginGeography()

    def geoDatabase():
        capitals = pickle.load(open("capitals.p", "rb"))
        databaseChoice=str(input("Type a capital name or type exit to go back. Be sure to capitalize and spell properly"))
        if databaseChoice.lower() == "exit":
            beginGeography()
        elif databaseChoice not in capitals.keys():
            print("I do not know the capital of that country")
            capitalOfInput=str(input("Please enter the name of the capital of the country or type exit to go back, please capitalize and spell properly: \n"))
            if capitalOfInput.lower()=="exit":
                geoDatabase()
            else: 
                capitals[databaseChoice]=capitalOfInput
                pickle.dump(capitals, open("capitals.p", "wb"))
                geoDatabase()
        else:
            print("The capital of "+databaseChoice+" is "+capitals[databaseChoice])
            geoDatabase()

    def geoQuiz():
        capitals = pickle.load(open("capitals.p", "rb"))
        geoAnswer=" "
        score=[0,0]
        while geoAnswer.lower()!="exit":
            country=str(random.choice(list(capitals.keys())))
            answerGeo=input(str(("What is the capital of "+country+"? Or type exit to go back to the main screen. Be sure to spell correctly and capitalize! ")))
            print(" ")
            if answerGeo.lower()=="exit":
                print("You got "+str(score[0])+" right and "+str(score[1])+" wrong")
                if score[0]==0:
                    print('oof')
                elif score[1]==0:
                    print('Great Job!')
                elif score[1]>score[0]: 
                    print('Keep studying')
                elif score[1]<score[0]:
                    print('More right than wrong! ')
                beginGeography()
            elif answerGeo==capitals[country]:
                print("Correct!")
                score[0]=score[0]+1
            else:
                print("Incorrect! Better luck next time!")
                score[1]=score[1]+1
    beginGeography()

begin()

    
