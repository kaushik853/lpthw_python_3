# -*- coding: utf-8 -*-
from sys import exit
from random import randint
from textwrap import dedent


class Scene(object):
    def enter(self):
        print("This scene is not yet configured")
        print("Subcalss it and implement enter()")
        exit(1)


class Engine(object):
    def __init__(self,scene_map):
        self.scene_map = scene_map


    def play(self):
        #print(">>>Play>>>")
        breakpoint()
        current_scene = self.scene_map.openning_scene()
        last_scene = self.scene_map.next_scene('finished')
        #print(f"before while current scene is {current_scene} and last scene is {last_scene}")
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
            #print(f"end of while current scene is {current_scene} and next scene name is {next_scene_name} ")
        #print(f" end of play current scene is {current_scene}")
        current_scene.enter()





class Death(Scene):
    quips = [
        " You are dead. You are not good for living.",
        "Your mom will be proud of you..if she were smarter",
        "such a looser",
        "The small puppy is better than this",
        "You are worse than dad's jokes",
    ]
    def enter(self):
        print(Death.quips[randint(0,len(self.quips)-1)])
        exit(1)


class CentralCorridor(Scene):
    def enter(self):
        print(dedent("""

            The Gothons of Planet Percal #25 have invaded your ship and 
             destroyed your entire crew. You are the last surviving 
             member and your last mission is to get the neutron destruct 
             bomb from the Weapons Armory, put it in the bridge, and 
             blow the ship up after getting into an escape pod. 
             You're running down the central corridor to the Weapons 
             Armory when a Gothon jumps out, red scaly skin, dark grimy 
             teeth, and evil clown costume flowing around his hate 
             filled body. He's blocking the door to the Armory and 
             about to pull a weapon to blast you.
             """))
        action = input(" > ")
        if action == "shoot!":
            print(dedent("""
                 Quick on the draw you yank out your blaster and fire it at the Gothon
                 His clown custom is flowing and moving around his body.This ruins the Gothon new costum bought by his mom.Gothon was in full rage and hit you with laser gun
                 .You died instantly and then Gothon eats you.
                 """))
            return 'death'
        elif action == "dodge!":
            print(dedent("""
                 Like a world class boxer you dodge,weave,slip and slide right as a Gothon's blaster crank a laser past
                 your head .In the middle of artfull dodge ,your foot slips and your head hit the metal wall and you pass out.
                 Then Gothon stomps on your head and eat You
                 """))
            return 'death'
        elif action == "tell a joke!":
            print(dedent("""
                 Lucky that you learned Gothon insults in academy.You tell the only Gothon joke you know:
                 lubdLKJh QWRDSVB ghfd ASddffk xyASMNB QWERasdfQW ABCyxz MkjhNbKJhhg.
                 The gothon stops and tries not to laugh but burst out laughing and cannot move
                 While he is lau


                 ghing, you shoot on his head and run towards weapon armory door.
                 """))
            return 'laser_weapon_armory'
        else:
            print('Not possible to compute')
            return 'central_corridor'


class LaserWeaponArmory(Scene):
    def enter(self):
        print(dedent("""
             You do a dive roll into the Weapon Armory, crouch and scan 
             the room for more Gothons that might be hiding. It's dead 
             quiet, too quiet. You stand up and run to the far side of 
             the room and find the neutron bomb in its container. 
             There's a keypad lock on the box and you need the code to 
             get the bomb out. If you get the code wrong 10 times then 
             the lock closes forever and you can't get the bomb. The 
             code is 3 digits.
 """))
        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        print(code)
        guess = input("3 digit integer > ")
        #code = guess
        guesses = 1
        while guess != code and guesses < 10:
            print('BZZZZEDDD')
            #print(f">>>before increment{guesses}")
            guess = input('3 digit integer > ')
            guesses+=1
            print(f">>>>increment {guesses}")


        if guess == code:
            print(dedent("""
                 The container clicks open and the seal breaks, letting 
                 gas out. You grab the neutron bomb and run as fast as 
                 you can to the bridge where you must place it in the 
                 right spot
                 """))
            return 'the_bridge'

        else:
            print(dedent("""
                 The lock buzzes one last time and then you hear a
                 sickening melting sound as the mechanism is fused
                 together. You decide to sit there, and finally the
                 Gothons blow up the ship from their ship and you die.
                 """))
            return 'death'



class TheBridge(Scene):
    def enter(self):
        print(dedent("""
             You burst onto the Bridge with the netron destruct bomb
             under your arm and surprise 5 Gothons who are trying to
             take control of the ship. Each of them has an even uglier
             clown costume than the last. They haven't pulled their
             weapons out yet, as they see the active bomb under your
             arm and don't want to set it off.
             """))
        action = input("> ")
        if action == 'throw the bomb':
            print(dedent("""
                 In a panic you throw the bomb at the group of Gothons
                 and make a leap for the door. Right as you drop it a
                 Gothon shoots you right in the back killing you. As
                 you die you see another Gothon frantically try to
                 disarm the bomb. You die knowing they will probably
                 blow up when it goes off.
                 """))
            return 'death'
        elif action == 'slowly place the bomb':
            print(dedent("""
                 You point your blaster at the bomb under your arm and
                 the Gothons put their hands up and start to sweat.
                 You inch backward to the door, open it, and then
                 carefully place the bomb on the floor, pointing your
                 blaster at it. You then jump back through the door,
                 punch the close button and blast the lock so the
                 Gothons can't get out. Now that the bomb is placed
                 you run to the escape pod to get off this tin can.
                 """))
            return 'escape_pod'
        else:
            print('This will not compute')
            return 'the_bridge'


class EscapePod(Scene):
    def enter(self):
        print(dedent("""
             You rush through the ship desperately trying to make it to
             the escape pod before the whole ship explodes. It seems
             like hardly any Gothons are on the ship, so your run is
             clear of interference. You get to the chamber with the
             escape pods, and now need to pick one to take. Some of
             them could be damaged but you don't have time to look.
             There's 5 pods, which one do you take?
             """))
        good_pod = randint(1,5)
        print(good_pod)
        guess = input('single digit [pod #]> ')
        #good_pod = int(guess)
        if int(guess) != good_pod:
            print(dedent(f"""
                 You jump into pod {guess} and hit the eject button. The pod escapes out into the void of space,
                 then implodes as the hull ruptures, crushing your body into jam jelly.
                 """))
            return 'death'
        else:
            print(dedent(f"""
                 You jump into pod {guess} and hit the eject button.
                 The pod easily slides out into space heading to the
                 planet below.  As it flies to the planet, you look
                 back and see your ship implode then explode like a
                 bright star, taking out the Gothon ship at the same
                 time.  You won!
                 """))
            return 'finished'


class Finished(Scene):
    def enter(self):
        print("You won !! XXX..congo")
        return 'finished'
class Map(object):
    scenes = {
        'central_corridor':CentralCorridor(),
        'laser_weapon_armory':LaserWeaponArmory(),
        'the_bridge':TheBridge(),
        'escape_pod':EscapePod(),
        'death':Death(),
        'finished':Finished()
    }
    def __init__(self,start_scene):
        self.start_scene = start_scene
    def next_scene(self,scene_name):
        val = Map.scenes.get(scene_name)
        return val
    def openning_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
#print("All works")
