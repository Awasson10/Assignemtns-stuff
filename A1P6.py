#Problem 6
#asks user for length of a room and width to calculate area and area in sq meters
x= input("What is the length of the room in feet? ")
y= input("What is the width of the room in feet? ")
X=int(x)
Y=int(y)
#performs the calculations for Sqaure feet and for Square meters
SF= Y*X
SM=SF*0.092903
#pritns the users input and gives the calculations back to the user in a print format
print("You entered", X ,"feet by", Y ,"feet for length and width")
print(SF, "square feet")
print(SM, "square meters")
