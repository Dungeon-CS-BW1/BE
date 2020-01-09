# from adventure.rooms import rooms
from .models import Room

# rooms = {"Vine of Mire": "The room has a huge vine running up through the ceiling.",
# "Bright Flat": "There is a bright light coming through the ceiling and shining onto a small pool in the middle of the room.",
# "Ash County": "This room is so large it seem like a country.",
# "Southknoll	": "There is a knoll of grass that seems to have grown around the most southern point in the room.",
# "Goldwood": "A grove of trees with bark a bright shiny yellow.",
# "Inns lake": "This underground lake is vast, but there is boat on the water. you cant see across it.",
# "Archers rock": "There is a rock in here with a a large whole cut into it. You see a few old arrow heads in inside it.",
# "Owlgreen": "You stumble into a very green area with hundreds of hooting owls. It is pretty creepy.",
# "Valleylock": "You walk into the room and it is as wide as a glacier cravas and as at leas a mile long. ",
# "Helmsrapid": "You walk it and there is a small bridge running accross an underground rapid.",
# "Crystalmoors": "The vast purple crystals are mesmerizing you could stare at them for hours.",
# "True Strait": "You see the narrow path.",
# "Redcrypt": "You wish you were not colorblind.",
# "Westronwash": "If your car was in this room you would wash it.",
# "Westronhold": "Hold on! Hold on!",
# "Witch Run": "Why are these old ladies signing up for a 5k?",
# "Sorcerers Wilds": "Look out for gandalf, he is a wildman.",
# "Stonedowns": "There is no place like home, or stonedowns.",
# "Elmpeak": "There is now way to open the trapdoor.",
# "Arrach Bridge": "Don't fall off the bridge",
# "Blessed Gorge": "You have stepped into a sacred place.",
# "Mossy road": "The floor is slippery in here, is that moss?",
# "Archerskeep": "You could really use a bow and arrows.",
# "Sparrow hollow": "There is something flying around in here.",
# "Shieldgate": "You don't know why but this room has stalagtites.",
# "Rogue passage": "There are people watching star wars in here.",
# "Stoutmoor": "You wish that you could eat a lot of food right now.",
# "Leechkeep": "The sound of hissing comes from the back of the room.",
# "Cragpeak": "The floor in this room is really bumpy.",
# "Mosspoint": "There is a big x on the floor covered in moss.",
# "Scout Hill": "You found a woodcarving merit badge!!",
# "Grey Divide": "Everything is in grayscale and divided.",
# "Marble Plateau": "This plateau is made of marbles and feels strange under your feet.",
# "Low Ruin": "This ruin is below sea level, so luckily it isn't raining.",
# "Lookout Road": "You look out from your spot on the road and the wind hits you in the face.",
# "Carn River": "You see a slow flowing river with stones piled up on the banks.",
# "Bronzewood Bluff": "You are not bluffing, the trees in here are shiny and brown like bronze.",
# "Dungeon Basin": "There is a basin full of glowing purple liquid that you probably should not touch.",
# "Mud Dome": "The dome is dark and cool inside, a perfect place to rest.",
# "Mink Canyon": "What is that you just heard, it sounds like water.",
# "Mud Divide": "It is just sandy right now.",
# "Long Divide": "This room is sooooo long.",
# "Piratescleft": "There is a statue of a pirate, you don't think it will help you on your quest.",
# "Keelpond": "There are no fish in the pond.",
# "Tunnels of the Phantom Guardian": "You have entered the crypt of the phantom guardian.",
# "Haunt of the Destroyed Monk": "The monk in here is nothing special, he's not even bald!",
# "Burrows of the Spirit Priest": "The priest of spirit is very into yoga!",
# "The Dragon Grotto": "Why does the dragon have to live in a grotto?",
# "The Fire Burrow": "You see your childhood flash before your eyes.",
# "The Lion Tooth Quarter": "Are there animal dentists? You don't think so.",
# "The Raging Pit": "There is a feeling of general rage in this room.",
# "The Courage Cell": "You feel so courageous!",
# "Labyrinth of the Phantom King": "It is said the king was very kind.",
# "Vault of the Furious Dragon": "The dragon gets really mad is you step on his tail.",
# "Grotto of the Dishonored Arachnid": "That spider is so shamefull.",
# "Vault of the Thunder Forest": "Why is it so loud in this room?",
# "The Violent Haunt": "The ghosts in here have been very docile so far.",
# "The Flowing Delve": "You have found the flowing delve!",
# "The Prisoner Quarter": "There are old chains in this room, it looks like some one used to keep captives in here.",
# "The Volcanic Delve": "Don't step in the lava!The room has old hyrogliph paintings a large valcano errupting.",
# "The Crescent Moon Vault": "The light of the moon filters through the roof.",
# "The Sanguine Cells": "There are forlorn squirrells in here.",
# "The Eternal Rest Point": "Wow you are feeling sleepy. Don't die here!",
# "The Eternal Labyrinth": "This is a maze inside a maze.People have gotten lost in the labrynth of this room and never made it, be weery of which way you enter.",
# "The Forsaken Cells": "There is nobody in here...nice more cheese-its for you!his room is teaming with bacteria and viruses.",
# "The Murky Cells": "Super murky and kind of gross inside",
# "The Wailing Tunnels": "Is that moaning mertle?he wind blows through to tunnels and causes a horrendous wailing noise. Or it's ghosts.",
# "The Ogre Caverns": "Strange, the ogre has two eyes.here are huge piles of ogre bones towards the edges of the room.",
# "la Tanière Terrible": "Something is terrible in here. You should probably get out!",
# "la Grotte Cachée": "Wow it is dark in here.",
# "les Cavernes Invisibles": "There seems to be something invisible in here, but you don't know because it's invisible",
# "les Tunnels de Bronze": "Oh no a monster, oh actually it's just a rock.",
# "les Tunnels Brûlés": "You're getting hungry, hopefully there is some food in here.",
# "le Tunnel Sec": "Is it snowing in here?",
# "le Donjon Secret": "This room has 3 walls. Nice!",
# "The Lower Quarters": "This is your favorite room yet!",
# "Cavern of the Fallen Widow": "What was that noise?",
# "The Cold Maze": "You wish you had thought to bring you ipod.",
# "The Collapsing Tomb": "You find a friendly gnome in this room.",
# "The Overhanging Catacomb": "This room has a gravel floor.",
# "The Fractured Chamber": "This is the fracture chamber room.",
# "The Fire Tunnel": "There is no fire in here but you still want to move fast.",
# "Cavern of the Hidden Eagle": "You don't see a hidden eagle but eagles are good at hiding, especialy hidden eagles.",
# "Delve of the Conquered Soldier": "You will never be conquered!",
# "The Chaotic Cavern": "The cave room seems chaotic.",
# "The Infernal Lair": "There is a rug on the floor, you can't move it though.",
# "The Phoenix Pit": "Is that dumbledore?",
# "The Unknown Vault": "The contents of the room are unknown, you'll have to look around.",
# "les Terriers en Cristal": "You hear french music.",
# "la Grotte Dansante": "There is some writing on the wall but you don't know french.",
# "la Caverne Démoniaque": "This cavern is more like a maze, don't get lost.",
# "les Donjons Détruits": "THe room is dark but you find places on the walls were there are lanturns and long wooden table in the middle.",
# "le Terrier d'Arrogance": "There is an inscription on the side of the wall, that says beware the arrogant, for they will only find hardship.",
# "la Tanière Lugubre": "The room is is filled with onld stained paintings, you can see one of them looks like the painting of lake high in the mountains.",
# "le Tunnel Ancien": "This tunnel must be close to the surface because it you can see light coming in through cracks in the ceiling.",
# "le Tunnel d'Hurlement": "This tunnels is windy and has a fewi doors on the sides. some look caved in.",
# "le Repaire du Feu": "This is a vary narrow path, be careful you don't get stuck.",
# "The Lucent Burrow": "Be careful in this room, people tend to lose a bit of themselves in here.",
# "The Mirage Vault": "This vault is filled with crystals. So that are so large and smoothe you can see your reflection in them.",
# "The Wondering Chambers": "THis vast chamber is so high and wide that your not sure which direction you should go. If you continue on will you be able to find your way back?"
# }

# roomskey = []
# roomsvalue = []
# def getList(rooms):
#     for key, value in rooms.items():
#         roomskey.append(key)
#         roomsvalue.append(value)

# class Room:
#     def __init__(self, id, title, description, x, y):
#         self.id = id
#         self.title = title
#         self.descriprion = description
#         self.n_to = None
#         self.s_to = None
#         self.e_to = None
#         self.w_to = None
#         self.x = x
#         self.y = y
#     def __repr__(self):
#         if self.e_to is not None:
#             return f"({self.x}, {self.y}) -> ({self.e_to.x}, {self.e_to.y})"
#         return f"({self.x}, {self.y})"
#     def connectRooms(self, connecting_room, direction):
#         # destinationRoomID = destinationRoom.id

#         '''
#         Connect two rooms in the given n/s/e/w direction
#         '''
#         reverse_dirs = {"n": "s", "s": "n", "e": "w", "w": "e"}
#         reverse_dir = reverse_dirs[direction]
#         setattr(self, f"{direction}_to", connecting_room)
#         setattr(connecting_room, f"{reverse_dir}_to", self)
#         # try:
#         #     destinationRoom = Room.objects.get(id=destinationRoomID)
#         # except Room.DoesNotExist:
#         #     print("That room does not exist")
#         # if direction == "n":
#         #     self.n_to = destinationRoomID
#         # elif direction == "s":
#         #     self.s_to = destinationRoomID
#         # elif direction == "e":
#         #     self.e_to = destinationRoomID
#         # elif direction == "w":                self.w_to = destinationRoomID
#         # else:
#         #     print("Invalid direction")
#         #     return
#         # self.save()
#     # def playerNames(self, currentPlayerID):
#     #     return [p.user.username for p in Player.objects.filter(currentRoom=self.id) if p.id != int(currentPlayerID)]
#     # def playerUUIDs(self, currentPlayerID):
#     #     return [p.uuid for p in Player.objects.filter(currentRoom=self.id) if p.id != int(currentPlayerID)]

# # print(rooms)

class World:
    def __init__(self):
        self.grid = None
        self.width = 0
        self.height = 0
        self.roomskey = []
        self.roomsvalue = []
    def getList(self, rooms):
        for key, value in rooms.items():
            # setattr(self, 'roomskey', key)
            # setattr(self, 'roomsvalue', value)
            self.roomskey.append(key)
            self.roomsvalue.append(value)
    def generate_rooms(self, size_x, size_y, num_rooms):
        '''
        Fill up the grid, bottom to top, in a zig-zag pattern
        '''

        # Initialize the grid
        self.grid = [None] * size_y
        self.width = size_x
        self.height = size_y
        for i in range( len(self.grid) ):
            self.grid[i] = [None] * size_x

        # Start from lower-left corner (0,0)
        x = -1 # (this will become 0 on the first step)
        y = 0
        room_count = 0

        # Start generating rooms to the east
        direction = 1  # 1: east, -1: west


        # While there are rooms to be created...
        previous_room = None
        while room_count < num_rooms:

            # Calculate the direction of the room to be created
            if direction > 0 and x < size_x - 1:
                room_direction = "e"
                x += 1
            elif direction < 0 and x > 0:
                room_direction = "w"
                x -= 1
            else:
                # If we hit a wall, turn north and reverse direction
                room_direction = "n"
                y += 1
                direction *= -1

            # Create a room in the given direction
            room = Room(room_count, self.roomskey[room_count], self.roomsvalue[room_count], x, y)
            # Note that in Django, you'll need to save the room after you create it
            room.save()

            # Save the room in the World grid
            self.grid[y][x] = room

            # Connect the new room to the previous room
            if previous_room is not None:
                previous_room.connectRooms(room, room_direction)

            # Update iteration variables
            previous_room = room
            room_count += 1



    def print_rooms(self):
        '''
        Print the rooms in room_grid in ascii characters.
        '''

        # Add top border
        str = "# " * ((3 + self.width * 5) // 2) + "\n"

        # The console prints top to bottom but our array is arranged
        # bottom to top.
        #
        # We reverse it so it draws in the right direction.
        reverse_grid = list(self.grid) # make a copy of the list
        reverse_grid.reverse()
        for row in reverse_grid:
            # PRINT NORTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.n_to is not None:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"
            # PRINT ROOM ROW
            str += "#"
            for room in row:
                if room is not None and room.w_to is not None:
                    str += "-"
                else:
                    str += " "
                if room is not None:
                    str += f"{room.title}".zfill(3)
                else:
                    str += "   "
                if room is not None and room.e_to is not None:
                    str += "-"
                else:
                    str += " "
            str += "#\n"
            # PRINT SOUTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.s_to is not None:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"

        # Add bottom border
        str += "# " * ((3 + self.width * 5) // 2) + "\n"

        # Print string
        print(str)


# getList(rooms)
# world = World()
# num_rooms = 100
# width = 10
# height = 10
# world.generate_rooms(width, height, num_rooms)
# world.print_rooms()