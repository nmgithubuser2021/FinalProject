#Nicholas Mueller 00292391 CIS 153-O1Z Final Project
#Final Project
#This program demonstrates concepts learned during
#The class

def Ch1():
    print("Ch1 Introduction")
    print("In the first chapter some of the basics of Python and programming in general is what I learned")
    print("Starting out simple, with code that prints out what is entered into the program")
    print("I learned to use print in the Python code which is how I'm structuring this very line")
    print("Certain words are part of Pythons built in language such as else or try \n These are used to accomplish things when outside of a print statement")
    anykey=input ("Enter anything to return to the menu")
    MainMenu()

def Ch2():
    print("Ch2 Variables Expressions and Statements")
    print("In chapter 2 I learned how to create Variables with the Python syntax")
    print("Python like every programming language I've used has mathematical implementations and uses")
    print("Try entering values as prompted (numbers only or the program ends), the program will perform calculations for the user, making it a useful tool")

    A = input("Enter a number: ")
    B = input("Enter another number: ")
    try:
        x = float(A)
        y = float(B)
    except:
       print("Numerical input only please")

       quit()
    xp = (x**y)
    try:
        ival = int(A)
    except:
        ival = 0

    if ival > 0 :
        print("The result of " + str(x) + " ^ " + str(y) + " is " + str(xp))
    else:
        print('This calculation is not supported')

    anykey=input ("Enter anything to return to the menu")
    MainMenu()
def Ch3():
    print("Ch3 Conditional Execution and Boolean expressions")
    print("During Chapter 3 I learned how Python code can make choices for the user, based on predefined criteria or conditions")
    print("Follow the instructions to see an example of the program making a choice based on a condition predefined in the code")
    print("What will happen given proper input is the word hello is printed along side whatever the user enters as a name variable")
    print("Additionally when prompted for age a message will display conditionally based on input (numerical input only please) ")

    name = input("Please enter your name ")
    print("Hello " + name)
    rawstr = input('Enter your age:')
    try:
        ival = int(rawstr)
    except:
        ival = -1

    if ival >= 18 :
        print('Be sure to register to vote')
    else:
        print('Good Work')

    anykey=input ("Enter anything to return to the menu")
    MainMenu()
def Ch4():
    print("Ch4 Functions")
    print("Python has both the functionality to use built in functions such as the max function which returns the maximum value from a list of values")
    print("User defined functions are very useful also in fact every number option in the menu of this program")
    print("and even the menu itself used to print this line is really a user defined function")
    anykey=input ("Enter anything to return to the menu")
    MainMenu()

def Ch5():
    print("Chapter 5 Iteration")
    print("Iteration involves going back through and analysing the same data multiple times")
    print("Try the following program enter numbers or letters when finished type in done the data will be iterated through")
    print("After you are done the data will be displayed this is possible because of the use of a counter variable and iterating it multiple times")
    min = 10000000
    max = 0
    count = 0
    number = 0
    sum = 0.0
    while True :
        count = count + 1
        sval = input('Please enter a number: ')
        if sval == 'done' :
            break
        try:
            fval = float(sval)
        except:
            print('Bad Data')
            print('Invalid Input')
            continue

        number = number + 1
        sum = sum + fval
        sval=int(sval)
        if sval != 'done' and sval > max : max = sval
        sval=int(sval)
        if sval != 'done' and sval < min : min = sval

    print('Numbers entered ' +str(number))
    print('Sum ' + str(sum))
    print('Average ' + str(sum/number))
    print('Count of total entries  ' + str(count))
    print('Max value ' + str(max))
    print('Min value ' + str(min))

    anykey=input ("Enter anything to return to the menu")
    MainMenu()

def Ch6():
    print("Chapter 6 stuff")
    anykey=input ("Enter anything to return to the menu")
    MainMenu()

def Ch7():
    print("Chapter 7 stuff")
    anykey=input ("Enter anything to return to the menu")
    MainMenu()

def Exit():
    quit()

def MainMenu():
    print("0. Exit the program")
    print("1. Chapter 1 Material")
    print("2. Chapter 2 Material")
    print("3. Chapter 3 Material")
    print("4. Chapter 4 Material")
    print("5. Chapter 5 Material")
    print("6. Chapter 6 Material")
    print("7. Chapter 7 Material")
    while True:
        try:
            selection=int (input ("Enter a number choice: "))

            if selection==1:
                Ch1()
                break
            elif selection==2:
                Ch2()
                break
            elif selection==3:
                Ch3()
                break
            elif selection==4:
                Ch4()
                break
            elif selection==5:
                Ch5()
                break
            elif selection==6:
                Ch6()
                break
            elif selection==7:
                Ch7()
                break
            elif selection==0:
                Exit()
                break
            else:
                print("Error please choose a valid number")
                MainMenu()
        except ValueError:
             print("Invalid input choose a correct number")

MainMenu()
