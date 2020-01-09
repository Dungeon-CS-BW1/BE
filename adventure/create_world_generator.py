# from adventure.rooms import rooms
from .models import Room


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
                if room is not None and room.n_to is not 0:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"
            # PRINT ROOM ROW
            str += "#"
            for room in row:
                if room is not None and room.w_to is not 0:
                    str += "-"
                else:
                    str += " "
                if room is not None:
                    str += f"{room.id}".zfill(3)
                else:
                    str += "   "
                if room is not None and room.e_to is not 0:
                    str += "-"
                else:
                    str += " "
            str += "#\n"
            # PRINT SOUTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.s_to is not 0:
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