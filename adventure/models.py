from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
import uuid

class Room(models.Model):
    title = models.CharField(max_length=50, default="DEFAULT TITLE")
    description = models.CharField(max_length=500, default="DEFAULT DESCRIPTION")
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
    n_to = models.IntegerField(default=0)
    s_to = models.IntegerField(default=0)
    e_to = models.IntegerField(default=0)
    w_to = models.IntegerField(default=0)
    def connectRooms(self, connecting_room, direction):
        '''
        Connect two rooms in the given n/s/e/w direction
        '''
        reverse_dirs = {"n": "s", "s": "n", "e": "w", "w": "e"}
        reverse_dir = reverse_dirs[direction]
        setattr(self, f"{direction}_to", connecting_room.id)
        setattr(connecting_room, f"{reverse_dir}_to", self.id)
        self.save()
        # destinationRoomID = destinationRoom.id
        # try:
        #     destinationRoom = Room.objects.get(id=destinationRoomID)
        # except Room.DoesNotExist:
        #     print("That room does not exist")
        # else:
        #     if direction == "n":
        #         self.n_to = destinationRoomID
        #     elif direction == "s":
        #         self.s_to = destinationRoomID
        #     elif direction == "e":
        #         self.e_to = destinationRoomID
        #     elif direction == "w":
        #         self.w_to = destinationRoomID
        #     else:
        #         print("Invalid direction")
        #         return
        #     self.save()
      # destinationRoomID = destinationRoom.id

    def playerNames(self, currentPlayerID):
        return [p.user.username for p in Player.objects.filter(currentRoom=self.id) if p.id != int(currentPlayerID)]
    def playerUUIDs(self, currentPlayerID):
        return [p.uuid for p in Player.objects.filter(currentRoom=self.id) if p.id != int(currentPlayerID)]


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    currentRoom = models.IntegerField(default=0)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    stamina = models.IntegerField(default=100)
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
    def initialize(self):
        if self.currentRoom == 0:
            self.currentRoom = Room.objects.first().id
            self.x = Room.objects.first().x
            self.y = Room.objects.first().y
            self.save()
    def room(self):
        try:
            return Room.objects.get(id=self.currentRoom)
        except Room.DoesNotExist:
            self.initialize()
            return self.room()
    def move(self):
        self.stamina -= 1
        self.save()
    def eat(self):
        self.stamina += 5
        self.save()

class Item(models.Model):
    name = models.CharField(max_length=100, default="default item")
    staminaPoints = models.IntegerField(default=5)
    player_id = models.IntegerField(default=0)
    room_id = models.IntegerField(default=0)
    def pick_up(self, p_id):
        self.room_id = 200000000
        self.player_id = p_id
        self.save()
    def drop_it(self, r_id):
        self.room_id = r_id
        self.player_id = 0
        self.save()
    def eat_it(self, r_id, p_id):
        self.room_id = 2000000
        self.player_id = 0
        self.save()
    



@receiver(post_save, sender=User)
def create_user_player(sender, instance, created, **kwargs):
    if created:
        Player.objects.create(user=instance)
        Token.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_player(sender, instance, **kwargs):
    instance.player.save()





