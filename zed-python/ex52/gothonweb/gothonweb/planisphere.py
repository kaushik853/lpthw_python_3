# create class 'Room'
class Room(object):
        # define __init__ self function, accepts 'name', 'description'
    def __init__(self, name, description):
        # maps param 'name' to 'self.name = name' and 'self.description = description'
        # 'self.paths = {}'
        self.name = name
        self.description = description
        self.paths = {}

        # define function go, accepts params 'self' and 'direction', it calls itself
        # using self.paths.get returns the values within the dictionary assigned to
        # Room.paths
    def go(self, direction):
        return self.paths.get(direction, None)

        # define function 'add_paths', accepts params 'self' and 'paths' which calls
        # 'self.paths.update' which is used to update the dictionary in the class
        # Room.paths
    def add_paths(self, paths):
        self.paths.update(paths)


central_corridor = Room('Central Corridor',
"""
    The Gothons of Planet Percal #25 have invaded your ship and
    destroyed your entire crew. You are the last surviving member
    and your last mission is to get the neutron destruct bomb
    from the Weapons Armoury, put it in the bridge, and blow up
    the ship up after getting into an escape pod.

    You're running down the central corridor to the weapons Armoury
    when a Gothon jumps out. Red scaly skin, dark grimy teeth, and
    evil clown costume flowing around his hate-filled body. He's
    blocking the door to the Armoury and about to pull a weapon to
    blast you.
""")
laser_weapon_armory = Room('Laser Weapon Armory',
"""
    Luckily, they make you learn Gothon insults while in the
    academy. You tell the one Gothon joke you know:
    'Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr,
    fur fvgf nebhaq gur ubhfr'. The Gothon stops. It tries not
    to laugh but eventually it bursts out laughing and cant'
    move. While he's laughing you run up and shoot the Gothon
    square in the head, putting it down before jumping through
    the Weapon Armoury door.

    You do a diving roll into the Weapon Armoury before crouching
    and scanning the room for more Gothons that might be hiding
    It's dead quiet, too quiet. You stand up and run to the far
    side of the room and find the neutron bomb in it's container.
    There's a keypad lock on the box and you will need the code
    to retrieve the bomb. If you get the code wrong 10 times then
    the lock closes and can never be opened. The code is 4 digits.
""")
the_bridge = Room('The Bridge',
"""
    The container clicks open and the seal breaks with a hiss
    as the gas escapes. You grab the neutron bom and run as
    fast as you can to the bridge where you must place it in
    the right spot.

    You burst onto the Bridge with the neutron bomb under your arm.
    You surprise 5 Gothons who are trying to take control of the ship.
    Each of them has an even uglier face and costume than the last.
    They haven't pulled their weapons yet as they have seen the active
    bomb under your arm and don't wish to set it off.
""")
escape_pod = Room('Esacpe Pod',
"""
    You point your blaster at the bomb under your arm and the Gothons
    put their hands up and start to move backward. Sweat beads on their
    large grotesque foreheads. You inch towards the door, open it, and
    then place the bomb on the floor, pointing your blaster at it. You
    then jump backwards through the door, punching the close button.
    You blast the lock so the Gothons can't get out. Now that the bomb
    placed, you run to the escape pod to get off this tin can.

    You rush through the ship desperately trying to make it to the escape
    pod before the ship explodes. It seems like hardly any Gothons are onboard
    the ship so you are left unhindered. You get to the chamber with the escape
    pods and now need to pick one. Several have have been damaged, some more than
    others, but you don't have time to check them all. There's 5 pods, which one
    do you take?
""")
the_end_winner = Room('The End',
"""
    You jump into pod {guess} and hit the eject button. The pod easily
    slides out into space heading to the planet below. As it flies to
    to the planet, you look back and see your ship explode like a bright
    star, taking out the Gothon ship at the same time. You won.
""")
the_end_loser = Room("The End",
"""
    You jump into pod {guess} and hit the eject button. The pop escapes out
    into the void of space then implodes as the hull ruptures, crushing your
    body into human jam.
""")

generic_death = Room('Death', "You died!")

escape_pod.add_paths({
    '2':the_end_winner,
    '*':the_end_loser
})
the_bridge.add_paths({
    'throw the bomb':generic_death,
    'slowly place the bomb':escape_pod
})
laser_weapon_armory.add_paths({
    '0132':the_bridge,
    '*':generic_death
})



central_corridor.add_paths({
    'shoot!':generic_death,
    'dodge!':generic_death,
    'tell a joke':laser_weapon_armory
})

START = 'central_corridor'
def load_room(name):
    return globals().get(name)

def name_room(room):
    for key, value in globals().items():
        if value == room:
            return key
