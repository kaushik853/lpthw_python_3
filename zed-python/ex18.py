def print_all(*args):
    args1,args2 = args
    print(f" The first argument is :{args1} and the second argument is: {args2}")
def print_together(args1,args2):
    print(f" argument1 : {args1} and argument2 : {args2} ")
def print_one(args):
    print(f" this will only print one argument: {args} ")
def print_none():
    print(" We have nothing to print")

carina = "Carina"
kiewitt = "pal"
tara = "tara pal"
print_all("kaushik","pal")
print_together(carina,kiewitt)
print_one(tara)
print_none()
