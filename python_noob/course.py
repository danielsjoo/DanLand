print("big">"small")

#this is an if statement
x = 2
if x>2:
    print("Hi", "big">"small")
elif x==2:
    print(2+2)
else:
    print(1)

# this is a while statement
i = 1
while i<5:
    print(i, end = " ")
    i = i+1
print()

def cups(i):
    #this is a recursive function for factorial
    if i<2:
        return 1
    else:
        return i*cups(i-1)

print(cups(5))