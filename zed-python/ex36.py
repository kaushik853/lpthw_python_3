from sys import exit
def poopoo_drink():
    print("poopoo loves to drink milk")
    print("Poopoo's Mama gives her milk")
    print("Poopoo is very happy after milk")
    #poopoo-nappy-wet = False

def poopoo_play():
    print("when poopoo is happy poopoo play a lot")
    print("Poopoo play in her playing mat")
    print("poopoo make noise like 'AWAWAWAAAA...aahhh..AWWAA'")

def sleep():
    print("poopoo is sleeping...ZZZzzzz")
    exit(0)

def start():
    print("halo ! meine name ist Poopoo")
    print("This play is my story")
    choice = input("What you want me to do now play or drink or poop: ")
    if choice == "play":
        print("poopoo will play now")
        print("did you check her nappy?")
        poopoo_play()
        print("after this poopoo like to sleep")
        sleep()
    elif choice == "drink":
        #poopoo-nappy-wet = True
        poopoo_drink()
        print("poopoo likes to sleep now")
        sleep()
    elif choice == "poop":
        pass
    else:
        print("give me better things to do")


start()
