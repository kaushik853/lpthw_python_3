curr = ''
magic_dict = {'k':'क्'}
text = input(">")
for key,value in enumerate(text):
    trans = magic_dict.get(value, '')
    curr = curr+trans
print(curr)
