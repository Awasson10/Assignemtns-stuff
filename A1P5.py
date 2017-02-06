#problem 5
#asks user for current age and when the want to retirer. Sweet stuff
x= input("What is your current age?  ")
y= input("What age would you like to retire? ")
#changes the string over to integers and stuff. WHAT WHAT? ?
X=int(x)
Y=int(y)
print ("You have", Y-X, "years left until you can retire.")
import datetime
now = datetime.datetime.now()
print("It's", now.year, "so you can retire in", now.year+(Y-X))
