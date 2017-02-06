#problem 7
#program figures out how many slices you've got for you and your cheap friends.
x = input("how many people you got? ")
y = input("how many pizza's you get hommie? ")
z = input("how many slices each pizza got? ")
#convents strings into integers for calculations
X=int(x)
Y=int(y)
Z=int(z)
#performs the math for figuring out number of slices per person and leftover slices
yz= (Y*Z)
ZAA= (Y%X)
Zep = (yz-ZAA)
#prints out answers to inputs asked by program
print( X, "people with", Y, "pizza's")
print("each mofo get's ", Zep, "slices")
print("you got", ZAA, "slices left over")
