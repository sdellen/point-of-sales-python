1# POS with classes
# this program is the cash register protion of a POS system. the user can input the forms of payement they want to use. formats and creates receipt
# Sam Ellenbogen
# 23/11/2020

import functions, os, Inventory
from CashRegister import *

class Main:
  def mainMenu():
    # mainMenu is the main function of the program, it navigates the user to whatever they choose to do. the user will always end up back here when they finish their desired task. they have an option to end the program in this function
    # no params

    # end is the variable that will store the boolean of whether or not to end the program (boolean)
    end = False
    
    # itemsInStore are all of the items in the store (list)
    itemsInStore = Inventory.Inventory().getInventory()

    # if checks if itemsInStore is None, meaning the inventory file, inventory.txt, was not formatted correctly
    if itemsInStore[0] == None:

      # sets end to true
      end = True
    # end if

    # hasUserBeenGreeted is the variable that stores the boolean of whether or not the user has been greeted (boolean)
    hasUserBeenGreeted = False

    # while loop repeats until end equals True
    while not end:

      os.system('CLS')

      # checks if the user hasn't been greeted
      if not hasUserBeenGreeted:

        # userInput uses getOption to get the user to decide what they want to do, and greets the user to the program (string)
        userInput = functions.getOption(['Purchase Items', 'Run inventory report', 'Restock', 'Modify items', 'Add item', 'Save', 'Quit'], functions.greetingsMessage())

        # hasUserBeenGreeted is the conditional of if the user has or has not been greeted (bool)
        hasUserBeenGreeted = True

      else:

        # userInput uses getOption to get the user to decide what they want to do, without greeting them to the program (string)
        userInput = functions.getOption(['Purchase Items', 'Run inventory report', 'Restock', 'Modify items', 'Add item', 'Save', 'Quit'])
      # end if

      os.system('CLS')

      # if statement runs different things depending on what userInput is (from 1 to 7)
      if userInput == '1':

        print(Receipt(itemsInStore).getReceiptString())
        functions.waitForEnter()

      elif userInput == '2':
        Inventory.Report(itemsInStore).runInventoryReport()
      elif userInput == '3':
        Inventory.Restock(itemsInStore).restockItems()
      elif userInput == '4':
        Inventory.Modify(itemsInStore).modifyItems()
      elif userInput == '5':
        Inventory.AddItem(itemsInStore).createItem()
      elif userInput == '6':
        Inventory.Inventory().save(itemsInStore)
      else:
        end = True
      # end if
    # end while

    functions.goodbyeMessage()

    return
  # end mainMenu 
# end Main

# calls mainMenu (finally done) 
Main.mainMenu()