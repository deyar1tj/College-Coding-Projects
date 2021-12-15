#Greeting block
customer = input("What's your name?\n")
str ="Welcome to Danny's market, "+ customer +". We have following items for sale: "
print(str)
print("T-shirt $18.95 15% off")
print("Chips $1.79 15% off")
print("Coke $2.99");
#Contstant variable declaration
TSHIRT_PRICE=18.95          #Capitals represent contants
CHIP_PRICE=1.79
COKE_PRICE=2.99
DEPOSIT=1.20
#Calculation block
tShirt_Counter= input("How many T-shirts do you want?")
chip_Counter= input("How many bags of potato chips?")
coke_Counter= input("What about 12-pack coke?")
tShirt_Counter = int(tShirt_Counter)
chip_Counter = int(chip_Counter)
coke_Counter = int(coke_Counter)
tShirt_Total=TSHIRT_PRICE* tShirt_Counter
chip_Total=chip_Counter*CHIP_PRICE
coke_Total=coke_Counter*COKE_PRICE
DEPOSIT=coke_Counter*DEPOSIT
Subtotal=coke_Total+DEPOSIT+chip_Total+tShirt_Total
discount= tShirt_Total*.15 +chip_Total*.15
tax=(tShirt_Total*.85)*0.06
total=Subtotal-discount+tax
#Reciept block
print ("Your total is $",round(total,2))
payment =int(input("Please enter your payment"))
change = payment -total
print(customer +" Here is your receipt")
print("item\t\t\tunit price\t\t\thow many\t\t\tcost")
print("T-shirt\t\t\t",round(TSHIRT_PRICE,2),"\t\t\t\t",round(tShirt_Counter,2),"\t\t\t\t",round(tShirt_Total,2))
print("Chips\t\t\t",round(CHIP_PRICE,2),"\t\t\t\t",round(chip_Counter,2),"\t\t\t\t",round(chip_Total,2))
print("Coke\t\t\t",round(COKE_PRICE,2),"\t\t\t\t",round(coke_Counter,2),"\t\t\t\t",round(coke_Total,2))
print("DEPOSIT\t\t\t\t\t\t\t\t\t\t\t",round(DEPOSIT,2))
print("Subtotal\t\t\t\t\t\t\t\t\t\t",round(Subtotal,2))
print("Discount\t\t\t\t\t\t\t\t\t\t-",round(discount,2))
print("Tax\t\t\t\t\t\t\t\t\t\t\t",round(tax,2))
print("Total\t\t\t\t\t\t\t\t\t\t\t",round(total,2))
print("Your change is\t\t\t\t\t\t\t\t\t\t",round(change,2))
print("Thank you,come again ")
#Partner Conner Elliot
