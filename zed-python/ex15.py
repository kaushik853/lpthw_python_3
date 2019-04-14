from sys import argv
script,filename = argv
txt = open(filename)
print(f"here is your file {filename}")

file_read = txt.read()

print(file_read)
txt.close()
print("Please type the filename again")
filename_again = input(">")
txt_again = open(filename_again)
print(txt_again.read())
txt_again.close()
