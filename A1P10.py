#problem 10
P= input("how much money do you want to invest? ")
T= input("how many years do you want to put it away for? ")
I= input("what is the rate of return %? ")
p= int(P)
t= int(T)
i= float(I)
In= i/100
Value = p*(1+t*In)
print("after", t, "years at", i,"%","you will have", "$",Value)
