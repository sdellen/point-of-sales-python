import functions, os, Inventory

class Transaction:

  def __init__(self, itemsInStore):

    self.itemsInStore = itemsInStore
    self.cart = []
    self.tax = 0
    self.subtotal = 0
    self.total = 0
    self.listOfPayments = []
  # end __init__

  def computeSubtotal(self):
    # computeSubtotal calculated the subtotal of the purchase
    # no params
    # returns self.subtotal (float)
    
    # for runs through every item that will be purchased
    for item in self.cart:

      # adds the cost of the item multiplied by how many are being bought to the subtotal
      self.subtotal += item.salesPrice * item.quantity
    # end for

    return self.subtotal
  # end computeSubtotal
  
  def computeTax(self):
    # computeTax calculates the tax of the purchase
    # no params
    # returns self.tax (float)

    # HST is the tax percentage constant (float)
    HST = .13

    # adds the subtotal multiplied by the the tax constant, HST to self.tax
    self.tax += self.subtotal * HST

    return self.tax
  # end computeTax

  def computeTotal(self):
    # computeTotal calculates the total of the purchase
    # no params
    # returns self.total (float)

    # uses computeSubtotal() and computeTax() to add to self.total
    self.total += self.computeSubtotal() + self.computeTax()

    return self.total
  # end computeTotal

  def chooseItem(self):
    # chooseItem chooses the item and quantity that a user wants to purchase
    # no params
    # returns the chosen item (object)
    
    os.system('CLS')
    
    # chosenItem will be the item that the user wants to buy (str)
    chosenItem = ''

    # quantity will be the quantity of the item that the user wants to buy (int)
    quantity = 0
      
    # chosenItem is redefined to the item that the user wants to buy (object)
    chosenItem = Inventory.ItemPicker(self.itemsInStore).chooseItemByNameOrSku()

    # if check if chosenItem is equal to None, meaning that the user chose to go back
    if chosenItem != None:

      # if checks if the item chosen by the user is out of stock
      if chosenItem.stock < 1:

        os.system('CLS')
        print(f'sorry we do not have any {chosenItem.name} left in stock')
        functions.waitForEnter()

      else:

        # gets the user to input the quantity of the item that they want to purchase
        quantity = int(functions.BetterInputs('enter the quantity you would like to purchase >>> ', 'invalid input\n\ninput must be a positive integer\n\nenter the quantity you would like to purchase >>> ', f'{chosenItem}').integerInput())

        # while repeats until the quantity to be purchased inputted by the user is less than or equal to the stock left of the chosen item
        while quantity > chosenItem.stock:

          os.system('CLS')

          # gets the user to input the quantity of the item that they want to purchase again
          quantity = int(functions.BetterInputs(f'sorry we only have {chosenItem.stock} left in stock\n\nenter the quantity >>> ', f'invalid input\n\ninput must be a positive integer\n\nqauntity left: {chosenItem.stock}\n\nenter the quantity as an integer >>> ', f'{chosenItem}\n\n').integerInput())
        # end while

        chosenItem.changeQuantity(quantity)
      

        os.system('CLS')
        print(f'{chosenItem}\n\n{quantity} {chosenItem.name} have been added to the cart')
        functions.waitForEnter()
      # end if
    # end if
      
    return chosenItem
  # end chooseItem

  def fillCart(self):
    # fillCart gets dictionary of information about the items that the user is purchasing
    # itemsInStore are all of the items in the store (list)
    # returns the information gathered (dictionary)

    # end is the boolean conditional for the while loop (bool)
    end = False

    # for runs through from 0 to the lenght of the list of the items in the store
    for i in range(len(self.itemsInStore)):

      # resests the quantity of the item
      self.itemsInStore[i].resetQuantity()
    # end for

    # while repeats until end equals True
    while not end:

      os.system('CLS')
      
      # userInput is the option of the user (str)
      userInput = functions.getOption(['Add to Cart', 'Checkout'])

      # if checks what the user input is
      if userInput == '1':

        # chosen item is the item chosen by the user (object or None)
        chosenItem = self.chooseItem()


        # if checks if chosenItem equals None, if the the user chose an item but chose a quantity of 0 and if the item has already been purchased. if item is already in cart then it adds the quantities of both order under one item, instead of having the same item appear twice on a receipt. if the user chose to purchase a quantity of 0 of an item, the item will not show up on the receipt. if the user chose to go back, chosenItem would be None, in this case, the item would not be added to cart.
        if chosenItem != None and chosenItem.quantity != 0 and chosenItem not in self.cart:

          # adds the item to cart
          self.cart += [chosenItem]
        # end if

      else:

        # sets end to equal True
        end = True
      # end if

    return self.cart
  # end fillCart

  def takePayment(self):
    # takePayment gets the users payment methods
    # no params
    # returns the list of payments (list) and the change left over (float) (tuple)

    # end is the boolean conditional for the while loop (boolean)
    end = False

    # total is the total of the purchase, this is to preserve the original value of total (float)
    total = self.total

    # change is the amount of change left over (float)
    change = 0

    # invalid will be the message that appears if the user did not valid payment type (str)
    invalid = ''

    # stillOwed is the amount that the customer still owes the store (str)
    stillOwed = ''

    # while loop repeats until the purchase is fully payed for
    while not end:

      # paymentType is the type of payment the user would like to use (object)
      paymentType = Payment(functions.BetterInputs(f'how would you like to pay >>> ', '', f'{stillOwed}{invalid}').advancedInput(), 0)

      # if checks if the user entered a valid payment type
      if paymentType.paymentType == False:

        # sets invalid to the invalid payment type message
        invalid = 'invalid input\n\nplease enter cash, debit or credit\n\n'

      else:
        
        # resets invalid to nothing
        invalid = ''

        # gets the user to input the amount of money they have of the unputted source
        paymentType.amount = float(functions.BetterInputs('how much money do you have of this source >>> ', 'invalid input\ninput must be a number\nhow much money do you have of this source >>> ', stillOwed).numberInput())

        # if checks if purchase has been fully payed for
        if total <= paymentType.amount:

          # if checks if the user is paying with cash
          if paymentType.paymentType == 'CASH':

            # adds what the change the store owes the customer to change
            change += paymentType.amount - total
          else:
            paymentType.amount = total
          # end if

          # sets end to True
          end = True

        else:

          # subtracts the amount the user has of the inputted payment type from the total
          total -= paymentType.amount

          # sets stilOwed to the still owed message, using total
          stillOwed = f'you owe ${total:.2f}\n\n'
        # end if

        # adds the payment type to the list of payment types
        self.listOfPayments += [paymentType]

    return self.listOfPayments, change
  # end takePayment
# end Transaction

class PaymentType:

  def __init__(self, paymentType):

    # if checks what payment type is being used
    if paymentType.lower().rstrip() == 'cash':

      # sets paymentType to CASH
      self.paymentType = 'CASH'

    elif paymentType.lower().rstrip() in ['debit', 'debit card']:

      # sets paymentType to DEBIT_CARD
      self.paymentType = 'DEBIT_CARD'
    
    elif paymentType.lower().rstrip() in ['credit', 'credit card']:

      # sets paymentType to CREDIT_CARD
      self.paymentType = 'CREDIT_CARD'

    else:
      # sets paymentType to False
      self.paymentType = False
    # end if
  # end __init__
# end PaymentType

class Payment:

  def __init__(self, paymentType, amount):

    # sets paymentType to paymentType attribute of a PaymentType object using the parameter of the __init__ paymentType, as the parameter for the class PaymentType
    self.paymentType = PaymentType(paymentType).paymentType
    self.amount = amount
  # end __init__
# end Payment

class Receipt:

  def __init__(self, itemsInStore):

    # sets transaction to the object Transaction using the __init__ parameter, itemsInStore as the parameter for the class Transaction
    self.transaction = Transaction(itemsInStore)
  # end __init__

  def getReceiptString(self):
    # getReceiptString formats a transaction into a receipt ready to be displayed
    # no params
    # returns the formatted receipt (str)

    # fills the carts of the transaction
    self.transaction.fillCart()

    # total uses the computeTotal method to get the total of the transaction for the formatted string (str)
    total = f'${self.transaction.computeTotal():.2f} '

    # tax is the tax of the transaction (str)
    tax = f'${self.transaction.tax:.2f} '

    # subtotal is the subtotal of the transaction (str)
    subtotal = f'${self.transaction.subtotal:.2f} '

    # listOfPayments uses the takePayment method to gather the list of payment types that the user used (list)
    # change is the amount of change that the store owes to the customer (float)
    listOfPayments, change = self.transaction.takePayment()

    # lines 286 - 295 are for the f-strings all are (str)
    change = f'${change:.2f} '
    STORE_NAME = "Sam's Store"
    CASHIER = '| Cashier: Sam Ellenbogen'
    TAX_STRING = 'Tax'
    SUBTOTAL_STRING = 'Subtotal'
    TOTAL_STRING = 'Total'
    BALANCE_STRING = 'Balance'
    GOODBYE_MESSAGE = 'Thank You for Shopping!'
    EQUAL_SIGNS = '====  '
    LINE_BREAK = '+=======================================+'
    CONTINUE_RECEIPT = '\n|                                       |\n'
    START_OF_PAYMENT_STUFF = '|---------------------------------------|'
    SPACER = ' ' * 15

    # receipt starts off with the top of the receipt, which is always the same (str)
    receipt = f'{LINE_BREAK}{CONTINUE_RECEIPT}|{STORE_NAME.center(39)}|{CONTINUE_RECEIPT}{LINE_BREAK}{CONTINUE_RECEIPT}{CASHIER:<40}|{CONTINUE_RECEIPT}{LINE_BREAK}{CONTINUE_RECEIPT}'

    os.system('CLS')

    # for runs through every item is the cart of transaction
    for item in self.transaction.cart:

      # regularPrice is the regular price of the transaction (str)
      salesPrice = f'${item.salesPrice:.2f} '

      # cost is the single unit price of the item multiplied by the quantity of the item purchased (str)
      cost = f'${item.salesPrice * item.quantity:.2f} '

      # name is the name of the item (str)
      name = item.name

      # if checks if the name is over 20 characters long
      if len(item.name) > 20:

        # updates local variable, name, to the first 20 characters of the name of the item
        name = item.name[20]
      # end if

      receipt += f'| {item.quantity:<3}{name:<12}{salesPrice:<11}{cost:<12}|{CONTINUE_RECEIPT}'
    # end for

    # adds the subtotal, tax and total to the receipt
    receipt += f"{START_OF_PAYMENT_STUFF}{CONTINUE_RECEIPT}|{SPACER}{SUBTOTAL_STRING:<15}{subtotal:>9}|{CONTINUE_RECEIPT}|{SPACER}{TAX_STRING:<15}{tax:>9}|{CONTINUE_RECEIPT}|{EQUAL_SIGNS:>39}|{CONTINUE_RECEIPT}|{SPACER}{TOTAL_STRING:<15}{total:>9}|{CONTINUE_RECEIPT}"
    
    # for runs through every payment type
    for paymentType in listOfPayments:

      # amount is the amount the user has of the payment type (str)
      amount = f'${paymentType.amount:.2f} '

      # adds the payment type to the receipt
      receipt += f"|{SPACER}{paymentType.paymentType:<15}-{amount:>8}|{CONTINUE_RECEIPT}"
    # end for
    
    # adds the balance, and finishes off the receipt
    receipt += f"|{EQUAL_SIGNS:>39}|{CONTINUE_RECEIPT}|{SPACER}{BALANCE_STRING:<15}-{change:>8}|{CONTINUE_RECEIPT}{LINE_BREAK}{CONTINUE_RECEIPT}|{GOODBYE_MESSAGE.center(39)}|{CONTINUE_RECEIPT}{LINE_BREAK}"
    
    return receipt
  # end getReceiptString
# end Receipt