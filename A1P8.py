#problem 8
#Import Math Function
import math
#Ask user for length and width of the room for input
length = float(input("What is the length of the room in feet?"))
width = float(input("What is the width of the room in feet?"))
#Converts the length and width of the room into totla size
total_size = length * width
#Converts the amount into 350 for the purpose of this program
convert = 350
#Performs the math for the total size of the room and the number of gallons required per room
gallons = math.ceil(total_size / convert)
output = "You will need to purchase {} gallons of paint to cover {} square feet".format(gallons, total_size)

print(output)
