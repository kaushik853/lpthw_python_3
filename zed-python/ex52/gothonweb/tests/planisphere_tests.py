from nose.tools import *
from gothonweb.planisphere import *


def test_room():
    gold = Room('GoldRoom',
                """This room has gold in it you can grab. There is a door to the north""")
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})

def test_room_paths():
    center = Room("Center", "test room in the center")
    north = Room("North", "test room in the north")
    south = Room("South", "test room in south")
    center.add_paths({'north':north, 'south':south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

def test_map():
    start = Room('Start', 'You can go west and down a hole')
    west = Room("Tree", "there are trees here ,you can go to east.")
    down = Room("Dungeon", "It's dark down here, you can go up.")
    start.add_paths({'west':west, 'down':down})
    west.add_paths({'east':start})
    down.add_paths({'up':start})
    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)

def test_gothon_game_map():
    start_room = load_room(START)
    assert_equal(start_room.go('shoot!'), generic_death)
    assert_equal(start_room.go('dodge!'), generic_death)
    assert_equal(start_room.go('tell a joke'), laser_weapon_armory)
    assert_equal(start_room.go('tell a joke').go('*'), generic_death)
    assert_equal(start_room.go('tell a joke').go('0132'),the_bridge)
    assert_equal(start_room.go('tell a joke').go('0132').go('throw the bomb'), generic_death)
    assert_equal(start_room.go('tell a joke').go('0132').go('slowly place the bomb'), escape_pod)
    assert_equal(start_room.go('tell a joke').go('0132').go('slowly place the bomb').go('*'), the_end_loser)
    assert_equal(start_room.go('tell a joke').go('0132').go('slowly place the bomb').go('2'), the_end_winner)
