from sys import argv
script,filename = argv
print(f" we will delete the file {filename}")
print("if you dont want that press CTRL-C(^C)")
print(" if you do want that press enter")
input("?")
print("opening the file....")


target = open(filename,'w')
print("truncating the file.. Goodbye!")
target.truncate()



print("Now i am going to ask you for 3 lines")
line1 = input("line1 :")
line2 = input("line2 :")
line3 = input("line3 :")
print("i am going to write this in file")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally,we close it")
target.close()
