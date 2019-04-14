def add(a , b):
    print(f" adding {a} + {b}")
    return a+b
def substract(a , b):
    print(f" substracting {a} - {b}")
    return a-b
def multiply(a , b):
    print(f" multiplying {a} * {b}")
    return a*b
def divide(a , b):
    print(f" division {a} / {b}")
    return a/b

print(" Lets do some maths with just the funstions !")
age = add(30,5)
height = substract(78,4)
weight = multiply(90,2)
iq = divide(100,2)
#print(age)
print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")
# puzzle for extra credit
print(" Here is the puzzle")
what = add(age,substract(height,multiply(weight,divide(iq,2))))
print(" that becomes :", what, "\n can you do it with hand ?")
