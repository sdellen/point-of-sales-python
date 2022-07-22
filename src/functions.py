import os

'''             ----------------BETTER INPUTS COMMENTS----------------

each input method acts as an advanced version of input()

the purpose of these input functions are to get the user input and check whether they are an acceptable input (integer, float, alphabetical, etc...)

**(all numeric input functions do not accept negative values as valid inputs)**

each one has three parameters:

parameter 1: inputMessage (string)
  inputMessage is the message the the user sees when they are asked for an input

parameter 2: invalidInputMessage (string)
  invalidInputMessage is the message the user sees if they enter an input that is not allowed

parameter 3: prefix (string)
  prefix is a message that stays at the top of the console even when it is cleared. for example, this is used to display the item that the user chooses to modify while they are modifying it.

return: userInput (string)
  every input function returns the users input as a string, just like input()

                -----------------------------------------------------
'''
class BetterInputs:
  
  def __init__(self, inputMessage, invalidInputMessage = '', prefix = ''):
    self.inputMessage = inputMessage
    self.invalidInputMessage = invalidInputMessage
    self.prefix = prefix

  def integerInput(self):

    os.system('CLS')

    userInput = input(f'{self.prefix}{self.inputMessage}')

    while not isInteger(userInput) or int(userInput) < 0:

      os.system('CLS')

      userInput = input(f'{self.prefix}{self.invalidInputMessage}')
    
    doubleCheck = BetterInputs('are you sure you have entered the right value? Y or N >>> ', 'invalid input\n\ninput must be either Y / y or N / n\n\nare you sure you have entered the right value? Y or N >>> ', f'{self.prefix}{self.inputMessage}{userInput}\n\n').yesNoInput()

    if doubleCheck in 'Nn':
      userInput = BetterInputs(self.inputMessage, self.invalidInputMessage, self.prefix).integerInput()

    return userInput

  def floatInput(self):

    os.system('CLS')

    userInput = input(f'{self.prefix}{self.inputMessage}')

    while not isFloat(userInput) or float(userInput) < 0:

      os.system('CLS')

      userInput = input(f'{self.prefix}{self.invalidInputMessage}')

    doubleCheck = BetterInputs('are you sure you have entered the right value? Y or N >>> ', 'invalid input\n\ninput must be either Y / y or N / n\n\nare you sure you have entered the right value? Y or N >>> ', f'{self.prefix}{self.inputMessage}{userInput}\n\n').yesNoInput()

    if doubleCheck in 'Nn':
      userInput = BetterInputs(self.inputMessage, self.invalidInputMessage, self.prefix).floatInput()

    return userInput

  def numberInput(self):

    os.system('CLS')

    userInput = input(f'{self.prefix}{self.inputMessage}')

    while not isNumber(userInput) or float(userInput) < 0:

      os.system('CLS')

      userInput = input(f'{self.prefix}{self.invalidInputMessage}')

    doubleCheck = BetterInputs('are you sure you have entered the right value? Y or N >>> ', 'invalid input\n\ninput must be either Y / y or N / n\n\nare you sure you have entered the right value? Y or N >>> ', f'{self.prefix}{self.inputMessage}{userInput}\n\n').yesNoInput()

    if doubleCheck in 'Nn':
      userInput = BetterInputs(self.inputMessage, self.invalidInputMessage, self.prefix).numberInput()

    return userInput

  def yesNoInput(self):

    os.system('CLS')

    userInput = input(f'{self.prefix}{self.inputMessage}')

    while not isYesNo(userInput):

      
      os.system('CLS')

      userInput = input(f'{self.prefix}{self.invalidInputMessage}')

    if userInput == '':
      userInput = 'y'

    return userInput

  def percentageInput(self):

    os.system('CLS')

    userInput = input(f'{self.prefix}{self.inputMessage}')

    while not isPercentage(userInput):

      os.system('CLS')

      userInput = input(f'{self.prefix}{self.invalidInputMessage}')

    doubleCheck = BetterInputs('are you sure you have entered the right value? Y or N >>> ', 'invalid input\n\ninput must be either Y / y or N / n\n\nare you sure you have entered the right value? Y or N >>> ', f'{self.prefix}{self.inputMessage}{userInput}\n\n').yesNoInput()

    if doubleCheck in 'Nn':
      userInput = BetterInputs(self.inputMessage, self.invalidInputMessage, self.prefix).percentageInput()

    return userInput

  def alphabeticalInput(self):

    os.system('CLS')

    userInput = input(f'{self.prefix}{self.inputMessage}')

    while not isAlphabetical(userInput):

      os.system('CLS')

      userInput = input(f'{self.prefix}{self.invalidInputMessage}')

    doubleCheck = BetterInputs('are you sure you have entered the right value? Y or N >>> ', 'invalid input\n\ninput must be either Y / y or N / n\n\nare you sure you have entered the right value? Y or N >>> ', f'{self.prefix}{self.inputMessage}{userInput}\n\n').yesNoInput()

    if doubleCheck in 'Nn':
      userInput = BetterInputs(self.inputMessage, self.invalidInputMessage, self.prefix).alphabeticalInput()

    return userInput

  def advancedInput(self):

    os.system('CLS')

    userInput = input(f'{self.prefix}{self.inputMessage}')
  
    doubleCheck = BetterInputs('are you sure you have entered the right value? Y or N >>> ', 'invalid input\n\ninput must be either Y / y or N / n\n\nare you sure you have entered the right value? Y or N >>> ', f'{self.prefix}{self.inputMessage}{userInput}\n\n').yesNoInput()

    if doubleCheck in 'Nn':
      userInput = BetterInputs(self.inputMessage, '',self.prefix).advancedInput()

    return userInput

'''       ----------------VARIABLE TYPE CHECKING FUNCTION COMMENTS----------------

each is___() function determines if the variable fullfills certain conditions

the purpose of these functions are to be used the the input functions above and when needed elsewhere

each one has one parameter:

parameter 1: number/choice/string (string)
  number/choice/string is the variable that will be checked to fullfill certain conditions

return: a boolean of if the parameter has met the conditions (string)

                -----------------------------------------------------
'''

#function only used in floatInput (which is not used)
def isFloat(number):

  isValid = True
  try:
    
    int(number)
    isValid = False
  except:
    try:
      float(number)
    except:
      isValid = False

  return isValid

def isInteger(number):

  isValid = True

  try:
    int(number)


  except ValueError:

    isValid = False

  return isValid

def isNumber(number):

  validNumber = True

  try:
    float(number)

  except :
    validNumber = False

  return validNumber

def isYesNo(choice):

  validChoice = True

  if (len(choice) != 1 or choice not in 'ynYN') and choice != '':

    validChoice = False

  return validChoice

def isAlphabetical(string):

  validWord = True

  counter = 0

  while validWord and counter < len(string):

    if string[counter] not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':

      validWord = False

    counter += 1

  return validWord

def isPercentage(number):

  validInput = False

  if isInteger(number) and int(number) > -1 and int(number) < 101:

    validInput = True

  return validInput

def listToString(aList):
  # puts elements of aList in string
  # aList list to be put into string (list)
  # returns resultant string (string)

  # result is the string that will contain the contents of aList
  result = '' 

  # for loop repeats through every element of aList
  for element in aList:

    # concatinates element to result
    result += element
  # end for loop

  return result
# end listToString  

def stringToList(string):
  # stringToList converts a string to a list
  # string is the string that will be turned into a list (list)
  # returns the string, but every character is seperated into a list (list)

  # listOfString is the list that will contain all of the characters in string (list)
  listOfString = []

  # for loop runs through every character in stringToList
  for char in string:

    # adds char to the end of listOfString
    listOfString += [char]
  # end for statement

  return listOfString
# end stringToList

def waitForEnter():
  # waitForEnter stalls the program until the user presses enter
  # no params
  # returns null

  input ('\n\npress enter to continue    ')

  return
# end waitForEnter

def convertToLower(string):

  newLowercasedString = ''

  for i in string:

    if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':

      newLowercasedString += chr(ord(i) + 32)

    else:

      newLowercasedString += i

  return string

def goodbyeMessage():
  # goodbyeMessage prints a goodbye message when the user chooses to quit
  # no params
  # returns null

  print('\n\nHave a nice day!\n\n')

  return
# goodbyeMessage

def greetingsMessage():
  # goodbyeMessage prints a greetings message when the user runs the program
  # no params
  # returns null

  welcomeMessage = 'Welcome to the best Point of Sales System Ever!\n\n'

  return welcomeMessage
# greetingsMessage


# -----------------------------GET OPTION MENU CREATOR---------------------------------

def getOption(unformattedMenuOptions, title = ''):
  # getOption creates a menu that the user will choose an option from
  # unformattedMenuOptions are all of the options that the menu will have (list)
  # title is an optional message that will stay at the top while the menu is displayed (string)
  # returns userInput (string)


  # formattedMenuOptions uses createMenu to format unformattedMenuOptions into a presentable string (string)
  formattedMenuOptions = createMenu(unformattedMenuOptions)

  # acceptableInputs uses convertMenuOptionsToAcceptableInputs to determine what the userInput is allowed to be (string)
  acceptableInputs = convertMenuOptionsToAcceptableInputs(len(unformattedMenuOptions))

  # end is the variable that will store the boolean of whether or not to end the program (boolean)
  end = False 

  # while loop repeats until end equals True
  while not end:

    # userInput presents the formattedMenuOptions and gets the user's choice (string)
    userInput = input(title + formattedMenuOptions + '\nenter your choice >>> ')

    # if statement checks if userInput is acceptable
    if len(userInput) != 1 or userInput not in acceptableInputs:

      os.system('CLS')

      print('Please enter a valid input\n')

    else:

      # doubleCheck uses yesNoInput to get the user to input whether or not the have selected the correct choice (string)
      doubleCheck = BetterInputs('are you sure you have entered the right value? Y or N >>> ', 'invalid input\n\ninput must be either Y / y or N / n\n\nare you sure you have entered the right value? Y or N >>> ', f'{title}{formattedMenuOptions}\nenter your choice >>> {userInput}\n\n').yesNoInput()

      # if statement checks if doubleCheck is in the string 'Nn'
      if doubleCheck in 'Nn':

        os.system('CLS')

        # reassigns userInput using getOption
        userInput = getOption(unformattedMenuOptions, title)
      # end if statement

      # sets end to equal True
      end = True
    # end if statement
  # end while loop

  return userInput
# end createMenu

def createMenu(options):
  # createMenu formats the options of the menu
  # options are the options of the menu (list)
  # returns the options formatted to look like a menu (string)

  # formattedMenuOptions is the variable that will store the formatted menu (string)
  formattedMenuOptions = '\n'

  # for loop repeats from 0 to the number of options given
  for i in range (0, len(options)):

    # concatinates a formatted menu option to formattedMenuOptions
    formattedMenuOptions += f'\t{i + 1}: {options[i]}\n'
  # end for loop
  
  return formattedMenuOptions
# end createMenu

def convertMenuOptionsToAcceptableInputs(numberOfMenuOptions):
  # convertMenuOptionsToAcceptableInputs determines what the acceptable inputs for a menu will be
  # numberOfMenuOptions is the number of options there are in the menu (integer)
  # returns all of the acceptable inputs for the menu (string)

  # acceptableInputs is the variable that will store all of the acceptable inputs (string)
  acceptableInputs = ''

  # for loop repeats from 1 to numberOfMenuOptions
  for i in range (1, numberOfMenuOptions + 1):

    # adds the acceptable input to acceptableInputs
    acceptableInputs += str(i)
  # end for loop

  return acceptableInputs
# end convertMenuOptionsToAcceptableInputs

# -------------------------------------------------------------------------------------