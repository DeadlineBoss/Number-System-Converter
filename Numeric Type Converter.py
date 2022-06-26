# Program To Convert Any Number System To Another System
# By me not you and not him cuz i can never be him :'(
# Took me lot of time bruh i wrote something then thought what this way is better then just rewrote the whole thing :/
# Idk if i should be pround or sad this is not much pretty basic :') but then again I'm just in 11th


# IMPORTANT TO UNDERSTAND BEFORE READING THIS CODE
# I will be using the word the subpower to the denote the base of a number system that is in decimal to move to the next
# place we mutliply by 10 likewise in binary we do by 2. This 10 for decimal and 2 for binary, I will be calling that subpower
#
# One might say there is no need for some if statements but some of them are for the program to stop from running useless text
# When they are not need this helps in saving time and help in faster processing



# Defining Function To Convert Numbers from one system to another
def numberSystemConverter(inputNumber,inputNumberSystem,outputNumberSystem):
    # inputNumber is the number inputed by the user
    # inputNumberSystem represents the subpower of the number entered by the user
    # otputNumberSystem represents the subpower of the number we want to convert into
            
    # Declaring a global variable to use in both if statements
    tempInputNumber = inputNumber

    # Checking if the inputNumberType is hexa or not if not then turn input into int else keep in string
    if(inputNumberSystem != 16):
        inputNumber = int(inputNumber)
        tempInputNumber = inputNumber

    # Number system into decimal
    if(outputNumberSystem == 10) or (inputNumberSystem != 10 and outputNumberSystem != 10):
        # Declaring Global Variable
        listTemp = []

        # Checking if the number is non-hexadecimal if yes then leave it
        # If not convert into int then into list
        if(inputNumberSystem != 16):
            # Creating a list of the number to easily deal with each number seperatly
            listTemp = [int(x) for x in str(inputNumber)]

        else:
            listTemp = list(inputNumber)

        # Declare Variables
        decimalValue = 0
        placeInfo = len(listTemp)

        # Converting each number into respective number system by multipying by thier subpower and adding them
        # like 2 * 100 + 3 * 10 + 5 = 235
        for x in listTemp:
            # placeInfo stores the ones, tens , hundreds place
            placeInfo -= 1

            # Checking if the inputNumberSystem is 16
            # If no then convert as usual
            # If Yes then check if its a digit then convert if its not a digit convert into value then do the calculation
            if(inputNumberSystem != 16):
                tempVari = x * inputNumberSystem ** placeInfo

            else:
                # Checking is the number is a numerical or a character here
                if x.isdigit():
                    x = int(x)
                    tempVari = x * inputNumberSystem ** placeInfo

                elif(x == 'A'):
                    tempVari = 10 * inputNumberSystem ** placeInfo

                elif(x == 'B'):
                    tempVari = 11 * inputNumberSystem ** placeInfo
            
                elif(x == 'C'):
                    tempVari = 12 * inputNumberSystem ** placeInfo
            
                elif(x == 'D'):
                    tempVari = 13 * inputNumberSystem ** placeInfo
            
                elif(x == 'E'):
                    tempVari = 14 * inputNumberSystem ** placeInfo

                elif(x == 'F'):
                    tempVari = 15 * inputNumberSystem ** placeInfo
            
                else:
                    print("Number entered is incorrect")
     
            decimalValue += tempVari

        # Printing the value only when the operation ends here
        if(outputNumberSystem == 10):
            # Printing The Result
            print(decimalValue)
        
        # Else copying the value into another temp variable for further use
        else:
            tempInputNumber = decimalValue


    # Decimal To Another System
    if(inputNumberSystem == 10) or (inputNumberSystem != 10 and outputNumberSystem != 10):
        # Empty Str To Store The Remainders
        val = ""

        # Checking If The Work Is Done Or Not If Not Run Again
        while(tempInputNumber != 0):
            # Taking the Remainder And Dividing the number
            tempVari = tempInputNumber % outputNumberSystem
            tempInputNumber //= outputNumberSystem

            # Adding A B C D E F values for Hexadecimal values
            if(tempVari < 10):
                val = str(tempVari) + val
            else:
                if(tempVari == 10):
                    val = "A" + val
                
                elif(tempVari == 11):
                    val = "B" + val
                
                elif(tempVari == 12):
                    val = "C" + val
                
                elif(tempVari == 13):
                    val = "D" + val
                
                elif(tempVari == 14):
                    val = "E" + val
                
                else:
                    val = "F" + val

        # Printing The Result
        print(val)    



# ForntHand Code
# Taking Input From User
inputNum = input("Enter A Number: ")

# Selecting Value Type
print("Select 10 for Decimal Value")
print("Select 2 for Binary Value")
print("Select 8 for Octal Value")
print("Select 16 for Hexadecimal Value\n")

numType = int(input("Select the type of number entered: "))

outputNumType = int(input("\nEnter the number of the number system you want to convert into from the above: "))
print("")

numberSystemConverter(inputNum,numType,outputNumType)