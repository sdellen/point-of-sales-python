import functions, os, math
from datetime import datetime
from pytz import timezone

class Item:

  def __init__(self, sku, name, category, stock, minStock, vendorPrice, markUpPercentage, regularPrice, salesPercentage, salesPrice):

    self.name = name
    self.regularPrice = regularPrice
    self.stock = stock
    self.salesPercentage = salesPercentage
    self.vendorPrice = vendorPrice
    self.markUpPercentage = markUpPercentage
    self.category = category
    self.minStock = minStock
    self.sku = sku
    self.salesPrice = salesPrice
    self.warning = ''
    self.profit = 0
    self.quantity = 0
    
    
    # updates the warning on the item
    self.updateWarning()
  # end __init__

  def updateWarning(self):
    # updateWarning updates the warning on the item
    # no params
    # returns None

    # if checks if the stock of the item is less than the minimum stock of the item
    if self.stock < self.minStock:

      # updates the warning of the item to WARNING! (str)
      self.warning = 'WARNING!'
    else:

      # updates the warning of the item to an empty string (str)
      self.warning = ''
    # end if

    return
  # end updateWarning

  def changeQuantity(self, quantity):
    # changeQuantity changes the quantity of the item
    # quantity is the new quantity of the item (int)
    # returns None

    # subtracts the new quantity from the stock of the item
    self.stock -= quantity

    # adds the new quantity to the quantity of the item
    self.quantity += quantity

    # updates the profit of the item
    self.profit += quantity * (self.salesPrice - self.vendorPrice)

    # updates the warning of the item
    self.updateWarning()

    return
  # end changeQuantity

  def changeSalesPercentage(self, percentage):
    # changeSalesPercentage changes the sales percentage of the item
    # percentage is the new sales percentage of the item (int)
    # returns None

    # updates the sales price of the item with the new sales percentage
    self.salesPrice = self.regularPrice * (1 - (percentage / 100))

    # updates the sales percentage of the item to the new sales percentage
    self.salesPercentage = percentage

    return
  # end changeSalesPercentage

  def resetQuantity(self):
    # resetQuantity resets the quantity of the item
    # no params
    # returns None

    # sets the quantity of the item to 0
    self.quantity = 0

    return
  # end resetQuantity

  def updatePrices(self):
    # updatePrices updates the prices of the item
    # no params
    # returns None

    # updates the regular price of the item
    self.regularPrice = self.vendorPrice * (1 + (self.markUpPercentage / 100))

    # updates the sales price of the item
    self.salesPrice = self.regularPrice * (1 - (self.salesPercentage / 100))

    return
  # end updatePrices

  def __str__(self):
    # __str__ is the print code of the class
    # no params
    # returns the formatted item information (str)

    # regularPriceString is string of the regular price of the item with a $ added to the front (str)
    regularPriceString = f'${self.regularPrice:.2f}'

    # salesPriceString is string of the sales price of the item with a $ added to the front (str)
    salesPriceString = f'${self.salesPrice:.2f}'

    # salesPercentageString is string of the sales percentage of the item with a % added to the end (str)
    salesPercentageString = f'{self.salesPercentage}%'

    # name is the name of the item (str)
    name = self.name

    # if checks if the name is over 20 characters long
    if len(self.name) > 20:
      # updates local variable, name, to the first 20 characters of the name of the item
      name = self.name[20]
    # end if

    # itemInformation is the formatted information of the item (str)
    itemInformation = f'\nItem: {self.sku}\n\n\tName:{name:>22}\n\tCategory:{self.category:>18}\n\tStock:{self.stock:>21}\n\tRegular price:{regularPriceString:>13}\n\tSales price:{salesPriceString:>15}\n\tSales percentage:{salesPercentageString:>10}\n\n'
      
    return itemInformation
  # end __str__

  def fullInfo(self):
    # fullInfo prepares the full information of the item for when displaying a single item
    # no params
    # returns the formatted information of the item (str)

    # regularPriceString is string of the regular price of the item with a $ added to the front (str)
    regularPriceString = f'${self.regularPrice:.2f}'

    # salesPriceString is string of the sales price of the item with a $ added to the front (str)
    salesPriceString = f'${self.salesPrice:.2f}'

    # vendorPriceString is string of the vendor price of the item with a $ added to the front (str)
    vendorPriceString = f'${self.vendorPrice:.2f}'
    
    # profitString is string of the profit of the item with a $ added to the front (str)
    profitString = f'${self.profit:.2f}'

    # markUpPercentageString is string of the mark up percentage of the item with a % added to the end (str)
    markUpPercentageString = f'{self.markUpPercentage}%'

    # salesPercentageString is string of the sales percentage of the item with a % added to the end (str)
    salesPercentageString = f'{self.salesPercentage}%'

    # name is the name of the item (str)
    name = self.name

    # if checks if the name is over 20 characters long
    if len(self.name) > 20:

      # updates local variable, name, to the first 20 characters of the name of the item
      name = self.name[20]
    # end if

    # itemInformation is the formated string of all the information about the item (str)
    itemInformation = f'\nItem: {self.sku}\n\n\tName:{name:>22}\n\tCategory:{self.category:>18}\n\tStock:{self.stock:>21}\n\tMinimum stock:{self.minStock:>13}\n\tVendor price:{vendorPriceString:>14}\n\tMark up percentage:{markUpPercentageString:>8}\n\tRegular price:{regularPriceString:>13}\n\tSales percentage:{salesPercentageString:>10}\n\tSales price:{salesPriceString:>15}\n\tProfit:{profitString:>20}\n\n'

    return itemInformation
  # end fullInfo

  def reportItem(self):
    # reportItem prepares the full information of the item for when displaying multiple items, each on one line
    # no params
    # returns None


    # regularPriceString is string of the regular price of the item with a $ added to the front (str)
    regularPriceString = f'${self.regularPrice:.2f}'

    # salesPriceString is string of the sales price of the item with a $ added to the front (str)
    salesPriceString = f'${self.salesPrice:.2f}'

    # profitString is string of the profit of the item with a $ added to the front (str)
    profitString = f'${self.profit:.2f}'


    # name is the name of the item (str)
    name = self.name

    # if checks if the name is over 20 characters long
    if len(self.name) > 20:

      # updates local variable, name, to the first 20 characters of the name of the item
      name = self.name[20]
    # end if

    # itemInformation is the formatted information of the item (str)
    itemInformation = f'{self.sku:<10}{name:<22}{self.category:<10}{self.stock:<10}{self.minStock:<10}{regularPriceString:>10}{salesPriceString:>10}{profitString:>10}'

    print(itemInformation)

    return
  # end reportItem
# end Item

class Report:
  
  def __init__(self, itemsInStore):

    self.itemsInStore = itemsInStore
  # end __init__

  def runInventoryReport(self):
    # runInventoryReport displays the item in the store as the user chooses
    # no params
    # returns None

    # userInput is the user's choice o2f the options below (str)
    userInput = functions.getOption(['All items', 'Category', 'Less than a given stock', 'Items with a warning', 'Single item', 'back'], 'How would you like to display items?\n')

    # if checks what the userInput is
    if userInput == '1':

      # reports all items in store
      self.reportItems(self.itemsInStore)

    elif userInput == '2':

      # reports the items in the store in the inputted category
      self.reportItems(ItemPicker(self.itemsInStore).chooseCategory())
    elif userInput == '3':

      # reports items in the store under the inputted stock
      self.reportByQuantity()
    elif userInput == '4':

      # reports the items with a warning
      self.reportItemsWithWarning()
    elif userInput == '5':

      # reports a single item
      self.reportItem()
    # end if

    return
  # end runInventoryReport

  def reportItems(self, itemsToBeDisplayed):
    # report items displays the given list of items
    # itemsToBeDisplayed is the list of items that will be displayed (list)
    # returns None

    os.system('CLS')

    # Constants for the f-string
    SKU = 'SKU'
    NAME = 'NAME'
    CATEGORY = 'Category'
    STOCK = 'STOCK'
    MIN_STOCK = 'MIN STOCK'
    REG_PRICE = 'REG'
    SALES_PRICE = 'SALE'
    PROFIT = 'PROFIT'

    # prints the column headers for the items
    print(f'{SKU:<10}{NAME:<22}{CATEGORY:<10}{STOCK:<10}{MIN_STOCK:<10}{REG_PRICE:>10}{SALES_PRICE:>10}{PROFIT:>10}\n')

    # for runs from 0 to the length of the items to be displayed, increasing by 21 each repeatition
    for i in range(0, len(itemsToBeDisplayed), 21):
      # for runs from 0 to 21
      for j in range (i, i + 21):
        # displays an item
        if len(itemsToBeDisplayed) > j:
          itemsToBeDisplayed[j].reportItem()
      
      # waits for the user to hit enter
      functions.waitForEnter()
      os.system('CLS')
      # end for
    # end for

    return
  # end reportItems

  def reportItem(self):
    # reportItem reports a single item
    # no params
    # returns None

    # item is the item that will be displayed (object or None)
    item = ItemPicker(self.itemsInStore).chooseItemByNameOrSku(True)

    # if checks if item is None, meaning that no item was chosen
    if item != None:

      os.system('CLS')
      print(item.fullInfo())
      functions.waitForEnter()
    # end if

    return
  # end reportItem

  def reportByQuantity(self):
    # reportByQuantity reports items under a given quantity
    # no params
    # returns None

    # quantity is the user's minimum stock. every item below this stock will be reported (int)
    quantity = int(functions.BetterInputs(f'enter the minimum stock you would like to display >>> ', 'invalid input\n\ninput must be a positive integer\n\nenter the minimum stock you would like to display >>> ').integerInput())

    # itemsToBeDisplayed are the items under the given quantity (list)
    itemsToBeDisplayed = []

    # for runs through every item in the store
    for i in self.itemsInStore:

      # if checks if the item's stock is under the given quantity
      if i.stock < quantity:

        # adds the item to the list of items under the given quantity
        itemsToBeDisplayed += [i]
      # end if
    # end for

    # reports the items under the given quantity
    self.reportItems(itemsToBeDisplayed)

    return
  # end reportByQuantity

  def reportItemsWithWarning(self):
    # reports items with a warning
    # no params
    # returns None

    # itemsWithWarnings will be the list of the items with a warning (list)
    itemsWithWarnings = []

    # for runs through every item in the store
    for i in self.itemsInStore:

      # if checks if the item has a warning
      if i.warning == 'WARNING!':

        # adds item to the list of items with a warning
        itemsWithWarnings.append(i)
      # end if
    # end for
    
    # reports items with a warning
    self.reportItems(itemsWithWarnings)

    return
  # end reportItemsWithWarning
# end Report

class Restock:
  
  def __init__(self, itemsInStore):

    self.itemsInStore = itemsInStore
  # end __init__

  def restockItems(self):
    # restockItems navigates the user to how and what they want to restock
    # no params
    # returns None

    # userInput is the choice of the user (str)
    userInput = functions.getOption(['Chosen item', 'minimum quantity', 'warning message', 'back'], 'Restock by:')

    # if checks what the user inputs
    if userInput == '1':
      os.system('CLS')
      # restocks based off of a chosen item
      self.restockChosenItem()
    elif userInput == '2':
      os.system('CLS')
      # restocks based off of a minimum value
      self.restockBasedOnValue()
    elif userInput == '3':
      os.system('CLS')
      # restocks based off of a warning
      self.restockBasedOnWarning()
    # end if

    return
  # end restockItems

  def restockChosenItem(self):
    # restockChosenItem restocks a specific item
    # no params
    # returns None

    # chosenItem is the item that the user wants to restock(object or None)
    chosenItem = ItemPicker(self.itemsInStore).chooseItemByNameOrSku(True)   

    # if checks if the user decided not to pick an item
    if chosenItem != None:
    
      # quantity is the quantity that the user wants to order (int)
      quantity = int(functions.BetterInputs('enter the qauntity that you want to order >>> ', 'invalid input\n\ninput must be a positive integer\n\nenter the qauntity that you want to order >>> ', chosenItem.fullInfo()).integerInput())

      # if checks if minimum stock of the item is greater than the current stock of the item + the quantity chosen by the user to be added
      if chosenItem.minStock > chosenItem.stock + quantity:

        # brings the stock of the item back up to the minimum stock of the item by ordering the difference
        chosenItem.stock += (chosenItem.minStock - chosenItem.stock)
      else:

        # adds the quantity to the item
        chosenItem.stock += quantity
      # end if

      # updates the warning of the item
      chosenItem.updateWarning()

      os.system('CLS')
      print(f'{chosenItem.fullInfo()}stock has been ordered')
      functions.waitForEnter()
    # end if

    return
  # end restockChosenItem

  def restockBasedOnValue(self):
    # restockBasedOnValue restocks every item under a given quantity
    # no params
    # returns None

    # maxQuantity is the qauntity that an item must be under to have stock added (int)
    maxQuantity = int(functions.BetterInputs('enter the maximum qauntity that an item can have >>> ', 'invalid input\n\ninput must be a positive integer\n\nenter the maximum qauntity that an item can have >>> ').integerInput())

    # quantity to add is the amount of stock that each item will get (int)
    quantityToAdd = int(functions.BetterInputs('enter the qauntity that you want to order >>> ', 'invalid input\n\ninput must be a positive integer\n\nenter the qauntity that you want to order >>> ').integerInput())

    # itemsThatAreUnder will be the list of items that are under the given minimum (list)
    itemsThatAreUnder = []

    # for runs through every item in the store
    for i in self.itemsInStore:

      # if checks if the item has less stock than the given minimum
      if i.stock < maxQuantity:

        # adds item to the list ofitems that have stock less than the given minimum
        itemsThatAreUnder += [i]

        # if checks if minimum stock of the item is greater than the current stock of the item + the quantity chosen by the user to be added
        if i.minStock > (i.stock + quantityToAdd):

          # brings the stock of the item back up to the minimum stock of the item by ordering the difference
          i.stock += (i.minStock - i.stock)

        else:
        # adds the quantity inputted by the user to the item
          i.stock += quantityToAdd
        # end if

        # updates the warning of the item
        i.updateWarning()
      # end if
    # end for

    # reports the items that are under the given minimum
    Report(self.itemsInStore).reportItems(itemsThatAreUnder)

    return
  # end restockBasedOnValue

  def restockBasedOnWarning(self):
    # restockBasedOnWarning restocks every item with a warning
    # no params
    # returns None

    # quantityToAdd is the quantity the user wants to add over the refill to minimum stock (int)
    quantityToAdd = int(functions.BetterInputs('enter the qauntity that you want to order >>> ', 'invalid input\n\ninput must be a positive integer\n\nenter the qauntity that you want to order >>> ').integerInput())

    # for runs through every item in the store
    for i in self.itemsInStore:

      # if checks if the item has a warning
      if i.warning != '':

        # refills the item to its minimum stock, and adds the amount the user wants over that minimum
        i.stock += (i.minStock - i.stock) + quantityToAdd
      # end if

      # updates the warning of the item
      i.updateWarning()
    # end for
    
    # reports the items with a warning
    Report(self.itemsInStore).reportItemsWithWarning()

    return
  # end restockBasedOnWarning
# end Restock

class Modify:
  
  def __init__(self, itemsInStore):

    self.itemsInStore = itemsInStore
  # end __init__
  
  def modifyItems(self):
    # modifyItems navigates the user to what and how the want to modify
    # no params
    # returns None
    
    os.system('CLS')

    # userInput1 checks if the user want to modify a category or an item (str)
    userInput1 = functions.getOption(['Category','Item', 'Back'], 'Modify by:\n')

    # if checks what the user input is
    if userInput1 == '1':

      # calls categoryMenu
      self.categoryMenu()

    elif userInput1 == '2':

      # calls itemMenu
      self.itemMenu()  
    # end if

    return
  # end modifyItems

  def categoryMenu(self):
    # categoryMenu is the menu if the user wants to modify a category
    # no params
    # returns None

    os.system('CLS')

    # category is the category that the user wants to modify (list)
    category = ItemPicker(self.itemsInStore).chooseCategory()

    os.system('CLS')
    if category != None:

      # userInput2 is the choice of how the user wants to modify the category (str)
      userInput2 = functions.getOption(['Sales percentage', 'Minimum stock', 'Back'], 'What would you like to modify:\n')

      # checks what the user chose
      if userInput2 == '1':

        # modifies the sales of a category
        self.modifySales(category)
      elif userInput2 == '2':

        # modifies the minimum stock of a category
        self.modifyMinimumStock(category)
      else:
        # calls modifyItems
        self.modifyItems()
      # end if
    else:
      print('category not found')
      functions.waitForEnter()
    
    return
  # end categoryMenu

  def itemMenu(self):
    # itemMenu is the menu if the user wants to modify an item
    # no params
    # returns None

    os.system('CLS')

    # chosenItem is the item that the user wants to modify
    chosenItem = [ItemPicker(self.itemsInStore).chooseItemByNameOrSku(True)]

    os.system('CLS')

    # if checks if the user wants to go back
    if chosenItem[0] != None:
      
      # userInput2 is the choice of how the user wants to modify the item (str)
      userInput2 = functions.getOption(['Sales percentage', 'Minimum stock', 'name', 'Vendor price', 'Mark up percentage', 'Delete item', 'Back'], f'{chosenItem[0].fullInfo()}What would you like to modify:\n')

      os.system('CLS')

      # checks what the user wants to do to the item
      if userInput2 == '1':

        # modifies the salesPercentage of the item
        self.modifySales(chosenItem, True)
      elif userInput2 == '2':

        # modifies the minimum stock of the item
        self.modifyMinimumStock(chosenItem, True)
      elif userInput2 == '3':
      
        # changes the name of the item
        self.changeName(chosenItem[0])
      elif userInput2 == '4':

        # changes the vendor price of the item
        self.changeVendorPrice(chosenItem[0])
      elif userInput2 == '5':

        # changes the mark up percentage of the item
        self.changeMarkUpPercentage(chosenItem[0])
      elif userInput2 == '6':

        self.deleteItem(chosenItem[0])
      else:

        # runs modifyItems again
        self.modifyItems()
      # end if
    else:

      # runs modifyItems again
      self.modifyItems()
    # end if

    return
  # end itemMenu

  def deleteItem(self, chosenItem):
    # deleteItem deletes the item from the list of the items in the store
    # chosenItem is item chosen by the user (object)
    # returns None

    # pops the chosen item from the list of the items in the store
    self.itemsInStore.remove(chosenItem)

    return
  # end deleteItem

  def modifySales(self, items, single = False, invalid = ''):
    # modifySales modifies the sales of a list of items
    # items is the list of items that will have their sales percentage changed (list)
    # single is a boolean, true if the there is only one item being changed (bool)
    # invalid is the invalid messsage if the user did not input a valid percentage, used by recursion (str)
    # returns None

    # if checks if there is only one item to be modified
    if single:

      # newPercentage is the new sales percentage that the user wants to put on the item (int)
      newPercentage = int(functions.BetterInputs('enter the new sales percentage >>> ', 'invalid input\n\ninput must be an integer between 0 and 100\n\nenter the new sales percentage >>> ', items[0].fullInfo() + invalid + f'maximum input for sales percentage: {math.floor(100 - (100 / (1 + (items[0].markUpPercentage / 100))))}%\n\n').percentageInput())

      # if checks if the users new sales percentage would make the sales price less than the vendor price
      if items[0].regularPrice * (1 - newPercentage / 100) < items[0].vendorPrice:

        # newPercentage redefined by recursivly calling modifySales until the user enters an sales percentage that won't make the sales price less than the regular price
        newPercentage = self.modifySales(items, True, 'Invalid input\n\nsales price cannot be less than the vendor price\n\n')
      # end if

      # changes the sales percentage to the new one inputted by the user
      items[0].changeSalesPercentage(newPercentage)

      os.system('CLS')
      print(f'{items[0].fullInfo()}Sales percentage changed')
      functions.waitForEnter()
      
    else:
      # newPercentage is the new sales percentage that the user wants to put on the items (int)
      newPercentage = int(functions.BetterInputs('enter the new sales percentage >>> ', 'invalid input\n\ninput must be an integer between 0 and 100\n\nenter the new sales percentage >>> ', invalid).percentageInput())

      # for runs through every item that will have its sales price modified
      for i in items:

        # if checks if the users new sales percentage would make the sales price less than the vendor price
        if i.regularPrice * (1 - newPercentage / 100) < i.vendorPrice:

          # newPercentage redefined by recursivly calling modifySales until the user enters an sales percentage that won't make the sales price less than the regular price
          newPercentage = self.modifySales(items, False, 'Invalid input\n\nsales price cannot be less than the vendor price\n\n')
        # end if
      # end for

      # for runs through every item that was chosen to be modified
      for i in items:

        # changes the sales percentage of the item to the new percentage
        i.changeSalesPercentage(newPercentage)
      # end for
    # end if

    return newPercentage
  # end modifySales

  def modifyMinimumStock(self, items, single = False):
    # modifyMinimumStock modifies the minimum stock of a list of items
    # items is the list of items that will have their minimum stock changed (list)
    # single is a boolean, true if the there is only one item being changed (bool)
    # returns None

    # if checks if there is only one item to be modified
    if single:

      # initializes newMin to 0 (int)
      newMin = 0

      # while repeats until the new minimum stock inputted by the user is greater than or equal to the stock of the item
      while newMin > items[0].stock:

        # newMin is the new minimum stock inputted by the user
        newMin = int(functions.BetterInputs('enter the new minimum stock >>> ', 'invalid input\n\ninput must be a positive integer\n\nenter the new minimum stock >>> ', items[0].fullInfo() + f'maximum input for minimum stock: {items[0].stock}\n\n').integerInput())
      # end while

      # if checks if the item being modified is out of stock
      if items[0].stock == 0:

        # informs the user that they must first order stock before modifying the minimum stock. This is because they cannot enter a value less than the current stock of the item. Therefore, if the item is out of stock, then they can only set the minimum to 0. instead of this happening, I don't let them update the minimum stock at all. They have to order stock first.
        print(f'{items[0].fullInfo()}item is out of stock\n\nstock must be reordered before minimum stock can be changed')
        functions.waitForEnter()
      else:

        # changes the minimum stock of the item to the new one inputted by the user
        items[0].minStock = newMin

        os.system('CLS')
        print(f'{items[0].fullInfo()}Minimum stock changed')
        functions.waitForEnter()
      # end if
    else:

      # newMin is the new minimum stock inputted by the user (int)
      newMin = int(functions.BetterInputs('enter the new minimum stock >>> ', 'invalid input\n\ninput must be a positive integer\n\nenter the new minimum stock >>> ').integerInput())

      # for runs through every item that was chosen to be modified
      for i in items:

        # changes the minimum stock of the item to the new one inputted by the user
        i.minStock = newMin
      # end for
    # end if
    
    return
  # end modifyMinimumStock
    
  def changeName(self, item):
    # changeName changes the name of an item
    # item is the item that will have its name changed (object)
    # returns None

    # newName is the new name inputted by the user (str)
    newName = functions.BetterInputs('enter the new name >>> ', 'invalid input\n\ninput must be a alphabetical\n\nenter the new name >>> ', item.fullInfo()).advancedInput().lower().rstrip()

    # changes the name of the item to the new name chosen by the user
    item.name = newName

    os.system('CLS')
    print(f'{item.fullInfo()}Name changed')
    functions.waitForEnter()

    return
  # end changeName

  def changeVendorPrice(self, item):
    # changeVendorPrice changes the vendor price of an item
    # item is the item that will have its vendor price changed (object)
    # returns None

    # newVendorPrice is the new vendor price iputted by the user (float)
    newVendorPrice = float(functions.BetterInputs('enter the new vendor price >>> ', 'invalid input\n\ninput must be a positive number\n\nenter the new regular regularPrice >>> ', item.fullInfo()).numberInput())

    # changes the vendor price of the item
    item.vendorPrice = newVendorPrice

    # updates the other prices in light of the changed vendor price
    item.updatePrices()

    os.system('CLS')
    print(f'{item.fullInfo()}Vendor price changed')
    functions.waitForEnter()

    return
  # end changeVendorPrice

  def changeMarkUpPercentage(self, item):
    # changeMarkUpPercentage changes the mark up percentage of an item
    # item is the item that will have its mark up percentage changed (object)
    # returns None

    # newMarkUpPercentage is the new mark up percentage inputted by the user (int)
    newMarkUpPercentage = int(functions.BetterInputs('enter the new mark up percentage >>> ', 'invalid input\n\ninput must be an integer between 0 and 100\n\nenter the new mark up percentage >>> ', item.fullInfo()).percentageInput())

    # change the mark up percentage of the item
    item.markUpPercentage = newMarkUpPercentage

    # updates the prices of the item in light of the changed mark up percentage
    item.updatePrices()

    os.system('CLS')
    print(f'{item.fullInfo()}Mark up percentage changed')
    functions.waitForEnter()

    return
  # end changeMarkUpPercentage
# end Modify

class AddItem:

  def __init__(self, itemsInStore):

    self.itemsInStore = itemsInStore
  # end __init__

  def getItemInformation(self):
    # getItemInformation gather the required information to add an item from the user
    # no params
    # returns the name (str), category (str), vendorPrice (float), markUpPercentage (int), salesPercentage (int), stock (int) and minStock (int) (tuple)

    # name is the name inputted by the user (str)
    name = functions.BetterInputs('enter the name of the item >>> ').advancedInput().lower().rstrip()

    # category is the category inputted by the user (str)
    category = functions.BetterInputs('enter the category of the item >>> ', 'invalid input\n\ninput must be alphabetical\n\nenter the category of the item >>> ').alphabeticalInput().upper().rstrip()

    # validPriceInfo is the conditional for the while loop (bool)
    validPriceInfo = False

    # while repeats until the sales percentage is a value that ensures the sales price will be equal to or greater than the vendor price
    while not validPriceInfo:

      # vendor price is the vendor price inputted by the user (float)
      vendorPrice =  float(functions.BetterInputs('enter the vendor price of the item >>> ', 'invalid input\n\ninput must be a positive number\n\nenter the vendor price of the item >>> ').numberInput())

      # mark up percentage is the mark up percentage inputted by the user (int)
      markUpPercentage = int(functions.BetterInputs('enter the mark up percentage of the item >>> ', 'invalid input\n\ninput must be an integer between 0 and 100\n\nenter the mark up percentage of the item >>> ').percentageInput())
      
      # sales percentage is the sales percentage inputted by the user.
      # for the math: the maximum input possible for the sales percentage is 100 - (100 / the mark up percentage in the 1.xx format (if mark up percentage is 47%, the denomenator would be 1.47))
      salesPercentage = int(functions.BetterInputs('enter the sales percentage of the item >>> ', 'invalid input\n\ninput must be an integer between 0 and 100\n\nenter the sales percentage of the item >>> ', f'maximum input for sales percentage: {math.floor(100 - (100 / (1 + (markUpPercentage / 100))))}%\n\n').percentageInput())

      # if checks if the sales percentage is a value that ensures the sales price will be less than the vendor price
      if ((1 - (salesPercentage / 100)) * ((1 + (markUpPercentage / 100)) * vendorPrice)) < vendorPrice:
        os.system('CLS')

        # informs the user that they have entered an invalid combination of vendor price, mark up percentage and sales percentage
        print('invalid inputs for vendor price, mark up percentage and sales percentage\n\nvendor price must be less than sales price\n\nre-enter vendor price, mark up percentage and sales percentage')
        functions.waitForEnter()
      else:

        # sets validPriceInfo to True
        validPriceInfo = True
      # end if
    # end while

    # validStockInfo is the condtional for the while loop (bool)
    validStockInfo = False

    # while repeats until minstock is less than or equal to stock
    while not validStockInfo:

      # stock is the stock inputted by the user (int)
      stock = int(functions.BetterInputs('enter the initial stock of the item >>> ', 'invalid input\n\ninput must be a positive integer\n\nenter the initial stock of the item >>> ').integerInput())

      # minStock is the minimum stock inputted by the user (int)
      minStock = int(functions.BetterInputs('enter the minimum stock of the item >>> ', 'invalid input\n\ninput must be a positive integer\n\nenter the minimum stock of the item >>> ', f'maximum input for minimum stock: {stock}\n\n').integerInput())

      # if checks if minStock is greater than stock
      if minStock > stock:
        os.system('CLS')

        # informs the user that they have entered an invalid combination of minStock and stock
        print('invalid inputs for stock and minimum stock\n\nminimum stock must be less than stock\n\nre-enter stock and minimum stock')
        functions.waitForEnter()
      else:

        # sets validStockInfo to True
        validStockInfo = True
      # end if
    # end while

    return name, category, vendorPrice, markUpPercentage, salesPercentage, stock, minStock
  # end getItemInformation

  def createItem(self):
    # createItem creates the item
    # no params
    # returns itemsInStore (list)

    # name is the name inputted by the user (str)
    # category is the category inputted by the user (str)
    # vendor price is the vendor price inputted by the user (float)
    # mark up percentage is the mark up percentage inputted by the user (int)
    # sales percentage is the sales percentage inputted by the user (int)
    # stock is the stock inputted by the user (int)
    # minStock is the minimum stock inputted by the user (int)
    name, category, vendorPrice, markUpPercentage, salesPercentage, stock, minStock = self.getItemInformation()

    doubleCheck = functions.BetterInputs('are you sure you want to add this item? Y or N >>> ', 'invalid input\n\ninput must be either Y / y or N / n\n\nare you sure you want to add this item? Y or N >>> ').yesNoInput()

    if doubleCheck not in 'Nn':

      # regularPrice is the vendor price multiplied by the mark up percentage (float)
      regularPrice = vendorPrice * (1 + markUpPercentage / 100)

      # sales price is the regular price multiplied by the sales percentage (float)
      salesPrice = regularPrice * (1 - salesPercentage / 100)

      # counter is the length of the list of the items in the store (int)
      counter = len(self.itemsInStore) - 1

      # end is the condtional for the while loop (bool)
      end = False

      # while repeats until end is True or counter reaches 0
      while not end and counter > -1:

        # if checks if the category of the item's category is the same as the category of the item being added
        if self.itemsInStore[counter].category == category:

          # mostRecentSku is the most recent item in the category that the user is adding an item to (str)
          mostRecentSku = self.itemsInStore[counter].sku

          # nextSku is the sku of the item being added (str)
          nextSku = mostRecentSku[:4] + f'{str(int(mostRecentSku[4:]) + 1):0>4}'
          
          # completedItem is the item that the user is adding (object)
          completedItem = Item(nextSku, name, category, stock, minStock, vendorPrice, markUpPercentage, regularPrice, salesPercentage, salesPrice)

          # adds the item to the list of the items in the store
          self.itemsInStore.insert(counter + 1, completedItem)

          # sets end to True
          end = True
        # subtracts one from counter
        counter -= 1
        # end if
      # end while
      
      # if checks if end equals True, if the category chosen has an item other than the one the user is adding
      if end != True:

        # sku is the sku of the item being added (str)
        sku = category[:3] + '-0001'

        # completedItem is the item that the user is adding (object)
        completedItem = Item(sku, name, category, stock, minStock, vendorPrice, markUpPercentage, regularPrice, salesPercentage, salesPrice)

        # adds the item to the list of the items in the store
        self.itemsInStore.append(completedItem)

      os.system('CLS')
      print(f'{completedItem.fullInfo()}Item added')
      functions.waitForEnter()
    # end if

    return self.itemsInStore
  # end createItem
# end AddItem

class Inventory:

  def getInventory(self):
    # getInventory gets the inventory from the file
    # no params
    # returns the list of items in the store (list)

    # inventory opens inventory.txt for reading
    inventory = open('src\inventory.txt', 'r')

    # itemsInStore is a list of every line in inventory (list)
    itemsInStore = inventory.readlines()

    # counter keeps track of the index of itemsInStore (int)
    counter = 0

    # validFormat is the boolean conditional for the while loop (bool)
    validFormat = True

    while validFormat and counter < len(itemsInStore):

      # temp is the line stripped of spaces and split at the commas (list)
      temp = itemsInStore[counter].rstrip().split(',')

      # if checks if the line from inventory.txt is in the valid format
      if not (len(temp) == 10 and len(temp[0]) == 8 and functions.isAlphabetical(temp[0][:3]) and temp[0][3] == '-' and functions.isInteger(temp[0][5:]) and functions.isInteger(temp[3]) and functions.isInteger(temp[4]) and functions.isNumber(temp[5]) and functions.isPercentage(temp[6]) and functions.isNumber(temp[7]) and functions.isPercentage(temp[8]) and functions.isNumber(temp[9])):

        # sets validFormat to False
        validFormat = False

        # sets itemsInStore to a list only containing one index which is None (list)
        itemsInStore = [None]

        # prints the error message, notifying the user that the format of the line is incorrect
        print(f'line {counter + 1} of inventory.txt does not match format\n\nplease try again')
        functions.waitForEnter()

      else:

        # overwrites the index of itemsInstore with temp
        itemsInStore[counter] = Item(temp[0], temp[1], temp[2], int(temp[3]), int(temp[4]), float(temp[5]), int(temp[6]), float(temp[7]), int(temp[8]), float(temp[9]))

        # increases counter by 1
        counter += 1
      # end if
    # end while
    
    # closes inventory.txt
    inventory.close()

    return itemsInStore
  # end getInventory

  def save(self, itemsInStore):
    # save saves the state of itemsInStore to inventory.txt and moves the old copy to a backup
    # itemsInStore is the list of every item in the store (list)
    # returns None

    # currentDate is the current date
    currentDate = datetime.now(timezone('US/Eastern'))

    # dateString is the currect date in a string format (str)
    dateString = currentDate.strftime("%m-%d-%y %H_%M_%S")

    # fileName is the name of the backup file that will be created (str)
    fileName = f'src\logs\inventory{dateString}.txt'

    # creates the file for writing as backup
    with open(fileName, 'w') as backup:

      # current opens inventory.txt for reading
      current = open('src\inventory.txt', 'r')

      # old is a list of every line in current (list)
      old = current.readlines()

      # for runs from 0 to the length of old
      for i in range(len(old)):

        # writes every line in old into backup
        backup.write(old[i])
      # end for 
    # end with

    # opens inventory.txt for writing as inventory
    with open('src\inventory.txt', 'w') as inventory:

      # for runs through every item in itemsInStore
      for i in itemsInStore:

        # writes the item into inventory, overwriting the old lines
        inventory.write(f'{i.sku},{i.name},{i.category},{i.stock},{i.minStock},{i.vendorPrice},{i.markUpPercentage},{i.regularPrice},{i.salesPercentage},{i.salesPrice}\n')
      # end for
    # end with
  
    os.system('CLS')
    print('\n\nInventory state saved!\n\n')
    functions.waitForEnter()

    return
  # end save
# end Inventory

class ItemPicker:

  def __init__(self, itemsInStore):

    self.itemsInStore = itemsInStore
    self.itemNames = []
    self.itemSkus = []
    self.categories = []

    # for runss through every item in the store
    for i in self.itemsInStore:

      # adds the name of the item to the list of the item names
      self.itemNames += [i.name.lower()]

      # adds the SKU of the item to the list of the item SKUs
      self.itemSkus += [i.sku]

      # adds the category of the item to the list of the item category
      self.categories += [i.category]
    # end for
  # end __init__

  def chooseItemByName(self):
    # chooseItemByName chooses the item picked by the user through a name
    # no params
    # returns the items with the chosen name (list) and chosen name (str) (tuple)

    # itemsWithChosenName will hold every item with the chosen name (list)
    itemsWithChosenName = []

    os.system('CLS')

    # chosenName is the name of the item that the user wants to find (str)
    chosenName = functions.BetterInputs(f'enter the name of the the item >>> ').advancedInput().lower().rstrip()

    # for runs through from 0 to the length of the list of the item in the store
    for i in range (len(self.itemsInStore)):

      # if checks if the chosenName is equal to the items name
      if chosenName == self.itemNames[i]:

        # appends the item to the list of items with the chosen name
        itemsWithChosenName.append(self.itemsInStore[i])
      # end if
    # end for

    return itemsWithChosenName, chosenName
  # end chooseItemByName

  def chooseItemBySku(self, fullInfo = False):
    # chooseItemBySku choose an item by the user inputted SKU
    # fullInfo is the conditional whether or not the user wants to display the full info of the item or just what a customer should see (bool)
    # returns chosen item (list) and the chosen SKU (str) (tuple)

    os.system('CLS')

    # chosenSku is the SKU of the item that they want to choose (str)
    chosenSku = functions.BetterInputs(f'enter the SKU of the the item >>> ').advancedInput().upper().rstrip()

    # chosenItem will contain the item with the chosen SKU. if no such item exists, chosenItem will remain as it is (list)
    chosenItem = []

    # end is the boolean conditional for the while loop (bool)
    end = False

    # counter is the indexer for the while loop (int)
    counter = 0

    # while repeats until end is True or the counter is equal to the length of the list of the items in the store
    while not end and counter < len(self.itemsInStore):

      # if checks if the sku in self.itemsSkus matches the given sku
      if self.itemSkus[counter] == chosenSku:

        # appends the item with the sku that matches the chosen sku to chosenItem
        chosenItem.append(self.itemsInStore[counter])

        # sets end to True
        end = True
      # end if
      
      counter += 1
    # end while

    return chosenItem, chosenSku
  # end chooseItemBySku

  def chooseItemByNameOrSku(self, fullInfo = False):
    # chooseItemByNameOrSku chooses an item by name or sku
    # fullInfo is the conditional whether or not the user wants to display the full info of the item or just what a customer should see (bool)
    # returns the chosen item (object or None)

    os.system('CLS')

    nameOrSku = functions.getOption(['Name', 'SKU', 'Back'], 'Choose item By:\n') # nameOrSku user getOption to generate a menu for the user to pick if they want to choose an item by name or SKU (str)
    chosenItem = None # chosenItem will be the item chosen by the user (None)
    itemsWithChosenNameOrSku = [None] # itemsWithChosenNameOrSku will be the items with the chosen name or sku (list)
    itemFound = False # itemFound is the boolean conditional for the while loop (bool)
    itemNotFoundMessage = '' # itemNotFoundMessage is the message that will display if the item is not found (str)
    
    if nameOrSku == '1': # if checks what the user chose for nameOrSku
      
      itemsWithChosenNameOrSku, chosenName = self.chooseItemByName() # calls chooseItemByName to get the chosen item(s) (list)
      itemNotFoundMessage = f'no items with the name {chosenName} exist' # changes itemNotFoundMessage
    elif nameOrSku == '2':
      
      itemsWithChosenNameOrSku, chosenSku = self.chooseItemBySku() # calls chooseItemByName to get the chosen item(s) (list)
      itemNotFoundMessage = f'item with SKU {chosenSku} does not exist' # changes itemNotFoundMessage
    # end if

    # if checks if itemsWithChosenNameOrSku is [None]. this serves two purposes. if the user selected 3, itemsWithChosenNameOrSku would have had no chance to change, so it would remain its initial value, [None]. this acts like if I checked if nameOrSku == '3'. the second purpose is if that if the user picked 1 or 2, if recursion occured in chooseItemByName or chooseItemBySku, and the outcome was the user deciding not to pick an item at all (e.i. option 3), it recognizes that recursive choice of option 3 as the final choice of the user.
    if itemsWithChosenNameOrSku == [None]:

      # sets itemFound to True. even though the item hasnt been found, the choice of the user has. they have chosen to not pick an item at all. this skips the search and returns None for the chosenItem
      itemFound = True
    # end if
    
    counter = 0 # counter is the indexer for the while (int)

    # while repeats until item is found, or until the counter is equal to the length of the items with the chosen name
    while not itemFound and (counter < len(itemsWithChosenNameOrSku)) and itemsWithChosenNameOrSku[0] != None:
      
      if fullInfo: # if checks is fullInfo is True or False

        # doubleCheck is the yesNoInput to make sure the user has chosen correctly (str)
        doubleCheck = functions.BetterInputs('is this the item you are looking for? Y or N >>> ', 'invalid input\n\ninput must be either Y / y or N / n\n\nis this the item you are looking for? Y or N >>> ', itemsWithChosenNameOrSku[counter].fullInfo()).yesNoInput()
      else:

        # doubleCheck is the yesNoInput to make sure the user has chosen correctly (str)
        doubleCheck = functions.BetterInputs('is this the item you are looking for? Y or N >>> ', 'invalid input\n\ninput must be either Y / y or N / n\n\nis this the item you are looking for? Y or N >>> ', itemsWithChosenNameOrSku[counter]).yesNoInput()
      # end if
      
      if doubleCheck not in 'Nn': # checks if doubleCheck is Y, y or 'enter', meaning the user decided they chose correctly
        
        chosenItem = itemsWithChosenNameOrSku[counter] # sets chosenItem to the item at the index counter of itemsWithChosenName (object)
        
        itemFound = True # sets itemFound to True
      # end if
      
      counter += 1 # add 1 to counter
    # end while
    
    if itemFound == False: # if checks if item has not been found

      # if checks if counter is equal to 0, if it is not, that means that the while loop ran, meaning items were found, but since itemFound == False, the user did not choose any of them but hasn't chosen to quit looking either. meaning the itemNotFoundMessage will be changed to someone more appropriate to the situation.
      if counter != 0:
        
        itemNotFoundMessage = 'item not found' # changes itemNotFoundMessage
      # end if

      os.system('CLS')
      print(itemNotFoundMessage)
      functions.waitForEnter()
      
      chosenItem = self.chooseItemByNameOrSku(fullInfo) # recursivly calls chooseItemByNameOrSku until the user chooses an item
    # end if

    return chosenItem
  # end chooseItemByNameOrSku

  def chooseCategory(self):
    # chooseCategory chooses a category of items
    # no params
    # returns a list of every item is the chosen category. if there are no items in the chosen category, returns None(list or None)

    # chosenItem will be the list of every item in the chosen category (list)
    chosenItems = []

    os.system('CLS')

    # userInput is the category that the user wants to choose (str)
    userInput = functions.BetterInputs('enter the category >>> ').advancedInput().upper().rstrip()

    # if checks if the inputted category exists
    if userInput not in self.categories:

      # sets chosenItems to None, meaning that the category chosen by the user does not have any items in it (None)
      chosenItems = None

    else:
    
      # for runs through every item in the store
      for i in self.itemsInStore:

        # if checks if the item is in the category inputted by the user
        if i.category == userInput:

          # adds the item to the list of chosen items, the items with the same category as the inputted category
          chosenItems += [i]
        # end if
      # end for
    # end if
    
    return chosenItems
  # end chooseCategory
# end ItemPicker