# greetings to wlcome to the coffee shop
print("hello welcome to starbucks")

#name of the customer
name = input("what is your name?\n")
print("Hello " + name  +  " thank you for coming in")

#using if to prevent something

if name == "Ben":
   evil_status = input("Are you evil\n")
   print("you are not allowed")
   exit()
#menu of the coffee shop
menu = "latte, african tea, ginger tea, espresso \n"

#placing the order
order = input(name + " what would you like in the following menu \n\n" + menu )

#price of the order
price = 5000
quantity = input("how many coffees would you like?\n")

total = price * int(quantity)
#output of the final result
print("thank you! \nYour total for " + quantity  + order + " will be RWF" + str(total))
 
print("thanks for shopping with us!!!")