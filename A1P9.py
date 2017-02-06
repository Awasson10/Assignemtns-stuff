#Problem 9
#Ask user for three item prices, and quantitys and calculates cost, with tax
#User inputs informaiton for price and Quantity
Item= input("enter price of item 1 $:")
Quantity= input("enter the quantity of item 1:")
Item2= input("enter the price of item 2 $:")
Quantity2= input("enter the quantity of item 2:")
Item3= input("enter the price of item 3 $:")
Quantity3= input("enter the quantity of item 3:")
#Converts user inputs into floats for $value
i1=float(Item)
q1=float(Quantity)
i2=float(Item2)
q2=float(Quantity2)
i3=float(Item3)
q3=float(Quantity3)
#Calculate the subtotal, tax, and total for the floaats
Subtotal = ((i1*q1)+(i2*q2)+(i3*q3))
tax= Subtotal*.055
total= Subtotal + tax
#Prints output for user Subtotal, tax and total
print("Subtotal", "$",Subtotal)
print("tax", "$",tax)
print("total", "$",total)
