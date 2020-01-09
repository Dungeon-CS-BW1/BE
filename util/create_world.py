from django.contrib.auth.models import User
from adventure.models import Player, Room


Room.objects.all().delete()

r_1 = Room(title="Outside Cave Entrance",
               description="North of you, the cave mount beckons")

r_2 = Room(title="Foyer", description="""Dim light filters in from the south. Dusty
passages run north and east.""")

r_3 = Room(title="Grand Overlook", description="""A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""")

r_4 = Room(title="Narrow Passage", description="""The narrow passage bends here from west
to north. The smell of gold permeates the air.""")

r_5 = Room(title="Treasure Chamber", description="""You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")

# r_1.save()
# r_2.save()
# r_3.save()
# r_4.save()
# r_5.save()

print(r_1.title)

# Link rooms together
r_1.connectRooms(r_2, "n")
r_2.connectRooms(r_1, "s")

r_2.connectRooms(r_3, "n")
r_3.connectRooms(r_2, "s")

r_2.connectRooms(r_4, "e")
r_4.connectRooms(r_2, "w")

r_4.connectRooms(r_5, "n")
r_5.connectRooms(r_4, "s")

players=Player.objects.all()
for p in players:
  p.currentRoom=r_1.id
  p.save()

