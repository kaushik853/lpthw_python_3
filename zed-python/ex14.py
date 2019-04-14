from sys import argv
script,username = argv
prompt = ">"
print(f"Hi user {username} , i am {script} script")
print("i have couple of questions")
print(f" Do you like me {username} ? ")
like = input(prompt)
print(f"Where do you live {username}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)
print(f"""
Alright, so you said {like} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice. """)
