from sys import exit
from textwrap import dedent


class Scene(object):
    print("Nothing is written yet")

    def enter(self):
        print("I need to write it")
        exit(1)

class Start(Scene):
    def enter(self):
        print(dedent(
               """
               You are starting the Game Of Thrones.
               Would you survive in the Seven Kingdoms?
               In the game of thrones,you win or you die...
               """))
        print(dedent(""" You need to choose whether you are a 'Lover' or 'Fighter' in GoT
                    """))
        choice = input("lover or fighter >")
        if choice == 'lover':
            char1 = Lover()
            char1.enter()
        elif choice == 'fighter':
            char2 = Fighter()
            char2.enter()


class Lover(object):
    def dwarf():
        dwarf_status = input("Are you a dwarf >")
        if dwarf_status == 'yes':
            print(dedent("""Stay low and you'll die at the ripe age of 80, with a belly full of wine
                        and a maiden's mouth around your cock.If you can keep your mouth shut,thats it
                        """))
        elif dwarf_status == 'no':
            girl_status = input("Are you a girl>")
            if girl_status == 'yes':
                print("War is easier than daugthers. you may live,if you are willing to get bloody")
            elif girl_status == 'no':
                print("Pray for oak and Iron to guard you well or Else you're dead and doomed to hell.Winter is coming")

    def enter(self):
        print(dedent("""You choose to be a Lover in GoT!!!..we proceed"""))
        family_hist = input(" Does your family have a hostory to marry their siblings? >")
        if family_hist == 'yes':
            victory_will = input(" Are you willing to do anything for victory ?>")
            if victory_will == 'yes':
                print("You cant wake the dragon and it cost you your life..so you die")
            elif victory_will == 'no':
                dragon_awaken = input("Do you know how to wake up the dragon?")
                if dragon_awaken == 'yes':
                    print("You are the blood of the dragon..fire can not kill you,but swords can.Tread carefully..Khaleesi!!")
                elif dragon_awaken == 'no':
                    Lover.dwarf()
        elif family_hist == 'no':
            sibling_like = input("Would you like to marry siblings?>")
            if sibling_like == 'yes':
                print("The things you do for love may one day get you killed")
            elif sibling_like == 'no':
                Lover.dwarf()

class Fighter(object):
    def king():
        print("You need to answer a call")
        king_call = input("Do you call yourself a King? ")
        if king_call == 'yes':
            kill_all = input("Do you want to kill all those who oppose you?")
            if kill_all == 'yes':
                print(dedent("""A good king knows when to save his strength and when
                            to destroy his enemies. you are not a good king
                            """))
            elif kill_all == 'no':
                print(dedent(""" Laws are tedious business and counting coppers worse
                            If boredom doesn't kill you, your subjects will
                            """))
        elif king_call == 'no':
            kill_king = input("Do you kill kings?")
            if kill_king == 'yes':
                print(dedent("""You'll be loved for a kindness. You never did and reviled
                            for your finest act, but you'll probably live for a time
                            King of The North
                            """))
            elif kill_king == 'no':
                print("Pray for oak and Iron to guard you well or Else you're dead and doomed to hell.Winter is coming")

    def enter(self):
        print(dedent("""You choose to be a Fighter in GoT!!!..we proceed"""))
        bound = input("Are you bound by duty and honor?")
        if bound == 'yes':
            meddle_life = input("Does your duty and honor cause you to meddle into the lives of kings?")
            if meddle_life == 'yes':
                print("Valor is a poor substitute for numbers. you'll have an honorable death,but You'll still be dead")
            elif meddle_life == 'no':
                bro_night_watch = input("Are you a brother of the night's watch?")
                if bro_night_watch == 'yes':
                    print("Long life or Short life, you'll live and die at your watch")
                elif bro_night_watch == 'no':
                    Fighter.king()
        elif bound == 'no':
            Fighter.king()


start_GOT = Start()
start_GOT.enter()
