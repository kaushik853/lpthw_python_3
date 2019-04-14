from sys import argv
from os.path import exists
script,from_file,to_file = argv
print(f" copying from {from_file} to {to_file} ")
in_file = open(from_file)
indata = in_file.read()
print(f" the input file is {len(indata)} bytes long ")
print(f" Does the output file exist? {exists(to_file)} ")
print(" ready... press ENTER to continue or hit CTRL+C to abort")
input()
out_file = open(to_file,'w')
out_file.write(indata)
print(" Allright....we are done here")
out_file.close()
in_file.close()
