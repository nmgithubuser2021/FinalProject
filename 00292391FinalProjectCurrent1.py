#Nicholas Mueller 00292391 CIS 153-O1Z Final Project
#Final Project
#This program demonstrates concepts learned during
#The class

import re

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

def Ch6to10():
    print("Chapter 6 to Chapter 10")
    print("Chapter 6-10 Strings to Tuples **Note chapters 6-10 have no examples just text explaining the concepts. As the material was demonstrated as the topic of two mini projects, so I'm focusing on material that is important but not part of any problem set or mini project. \n  A string in python is a sequence of characters the text in this print statement would be considered a String")
    print("Strings are immutable parts of a string can be extracted selectively using brackets and index positions, such as an individual character or the second half of a string")
    print("Chapter 7 Files")
    print("Python has useful capabilites for creating a file, or searching through an existing file such as analysing a system log, a file that would not be possible to read with human eyes alone.")
    print("The section on chapter 11 will demo searching through files, using regular expressions.")
    print("Chapter 8 Lists")
    print("Like strings Lists are a sequence of values, differences include lists can have multiple elements and include multiple data types such as numbers and words or even another list.")
    print("Chapter 9 Dictionaries")
    print(" A dictionary in Python is similar to a list in some ways, differences include the way a dictionary uses curly brackets {} and matches indices called keys to a value such a combination is called a key-value pair or an item")
    print("Chapter 10 Tuples")
    print(" A tuple is a value sequence similar to a list structure, tuples however are immutable, these tuples can also be compared and hashed. This makes lists of tuples sortable and usable as key values in a dictionary")
    anykey=input ("Enter anything to return to the menu")
    MainMenu()

def Ch11():
    print("Chapter 11 Regex part 1")
    print("Regular Expressions have their origins in the 1960s they are old and still very powerful expressions when used in a programming language")
    print("Regex is supported by Python with the import re module other languages that support regex includes Perl, PHP, and Java.")
    print("Regular Expressions are also very complex in terms of syntax and are nearly a whole programming language in themselves.")
    print("In the following example I will be demonstating how regex can be used similar to the grep command in Unix" )
    print("")
    print(" ^ Matches the beginning of a line \n $ Matches the end of a line \n . Matches any character \n \s matches whitespace \n \S matches any non-whitespace \n * repeats a character zero or more times")
    print(" *? repeats a character zero or more times non-greedy \n + repeats a character one or more times \n +? repeats a chatacter one or more times non-greedy")
    print(" [aeiou] matches a single character in the listed set \n [^XYZ] matches a single character not in the listed set \n [a-z0-9] The set of characters can include a range")
    print(" ( indicates where string selection is to start \n ) indicates where string selection is to end")
    regex = input("Enter a regular expression.")
    counter = 0
    hand = open('mbox.txt')
    for line in hand:
        line = line.rstrip()
        if re.search(regex, line):
            counter += 1
            print(counter, regex, line)
            print("Note that only a few lines are displayed in this menu version of the regex search")
            print("With regex in this example the user can just enter any combination of letters or numbers and a line that matches that pattern will be returned More of the complex syntax for Regex will be explored in the next example")
            anykey=input ("Enter anything to return to the menu")
            MainMenu()

def ChRegex():
    print("Ch11 Regex part 2. Continuing to look at regex due to it's complexity and importance")
    print("two main regular expressions functions that are useful are re.search shown in the previous example which is similar to the find() string method it maches a string with a regular expression")
    print("Also there is re.findall which like re.search uses its own special syntax")
    print(" As an example of the syntax try entering New\sRevision:\s\d+")
    print (" With that syntax the function will search for literally New Revision the \s denotes a space, the last part of the expression is the \d+ which means a digit the + indicates we are searching for at least one digit")
    regex1 = input("Enter a regular expression.")
    counter = 0
    hand = open('mbox-short.txt')
    for line in hand:
        line = line.rstrip()
        if re.findall(regex1, line):
            counter += 1
            print(counter, regex1, line)
            print("Note that only a few lines are displayed in this menu version of the regex search")
            print("With this function the user is working with the function re.findall with the file mbox-short prevoiusly it was re.search with mbox.txt")
            print("Some additional important syntax with regex includes ^ this symbol matches the beginning of a line $ matches the end of a line and a . will match any character.")
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
    print("6. Chapter 6-10 Material")
    print("11. Chapter 11 Material")
    print("12. Chapter 11 Material part 2")
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
                Ch6to10()
                break
            elif selection==11:
                Ch11()
                break
            elif selection==12:
                ChRegex()
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
