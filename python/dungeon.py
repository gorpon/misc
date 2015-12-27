# 2d maze
# monster randomly placed
# player randomply placed
# exit randomly placed
# player wins if reaches exit
# player loses if reaches monster
# player cannot leave the map (except by exit)
import random
from subprocess import call
grid = 5

def rand_spot(grid):
    x = random.randrange(0,grid)    
    y = random.randrange(0,grid)    
    # print("gen rand {} {}".format(x, y))
    return [ x, y ]

def init_player_map(grid):
    player_map = {}
    for x in list(range(0,grid)):
        for y in list(range(0,grid)):
            player_map[ (x, y)] = '?'
    return player_map

def place_actors(grid):
    actors = {}
    for actor in ["player", "monster", "the_exit"]:
        while True:
            try_coord = rand_spot(grid)
            if try_coord in actors.values():
                # print("{0}, {1} already matched another actor. retrying".format(try_coord))
                next
            else:
                # print("setting actor {} to {}, {}".format(actor, try_coord[0], try_coord[1]))
                actors[actor] = try_coord
                break 
    return actors

def print_help():
    print("""dungeon game
QUIT to quit
HELP for help
n north
w west
s south
e east
""")

def get_input(player):
    # none shall pass without the proper response
    while True:
        response = input("{0}, {1} Type HELP for help: ".format(*player))
        if response == 'QUIT':
            print("quitting early.  good bye")
            exit(0)
        elif response == 'HELP':
            print_help()
        elif response in 'nwse' and len(response):
                return response
        else:
             print("unknown command {}".format(response))

def encounter_check(actors):
    #check to see if player has encountered another actor
    # exit or monster)
    playa = actors['player']
    for actor in actors.keys():
        if playa == actors[actor] and actor == 'monster':
            monster_eats_you()
        elif playa == actors[actor] and actor == 'the_exit':
            found_the_exit()

def map_direction(direction):
    # map direction to relative coordinates
    if direction ==   'n':
        return [0, -1] 
    elif direction == 'w':
        return [-1, 0]
    elif direction == 's':
        return [0, 1]
    elif direction == 'e':
        return [1, 0]

def get_new_coord(actors, direction):
    cur_coord = actors['player']
    direction_coord = map_direction(direction)
    new_coord_x = cur_coord[0] + direction_coord[0]
    new_coord_y = cur_coord[1] + direction_coord[1]
    return [new_coord_x,  new_coord_y]

def boundary_check(new_coord, grid):
    # just return true or false if player can 
    # move in the desired direction
    new_coord_x = new_coord[0]
    new_coord_y = new_coord[1]
    if new_coord_x < 0 or new_coord_x > (grid - 1):
        return False
    elif new_coord_y < 0 or new_coord_y > (grid - 1):
        return False
    else:
        return True

def monster_eats_you():
    print("the monster eats you!")
    print("game over")
    exit(0)

def found_the_exit():
    print("you've found the exit!")
    print("you have one the game!")
    exit(0)

def debug_actors(actors):
    print("player {player} monster {monster} the_exit {the_exit}".format(**actors))

def player(actors):
    return(actors['player'])

def draw_map(player_map, actors):
    for y in list(range(0,grid)):
        for x in list(range(0,grid)):
            if actors['player'] == [x, y]:
              print("P ", end="") 
            else:
              print(player_map[(x, y)] + " ", end="") 
        print("\n")

def clear_screen():
    call(["clear"])
     

print("starting dungeon game with grid size {}".format(grid))
actors = place_actors(grid)
player_map = init_player_map(grid)

while True:
    #debug_actors(actors)
    clear_screen()
    player_map[tuple(player(actors))] = '_'
    draw_map(player_map, actors)
    direction = get_input(player(actors))
    new_coord = get_new_coord(actors, direction)
    if boundary_check(new_coord, grid):
        actors['player'] = new_coord
        encounter_check(actors)
        player_map[tuple(new_coord)] = '_'
    else:
        print("unable to move to direction {}".format(direction))

