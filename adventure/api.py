from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# from pusher import Pusher
from django.http import JsonResponse
from decouple import config
from django.contrib.auth.models import User
from .models import *
from rest_framework.decorators import api_view
import json
from django.core import serializers
from django.http import HttpResponse

# instantiate pusher
# pusher = Pusher(app_id=config('PUSHER_APP_ID'), key=config('PUSHER_KEY'), secret=config('PUSHER_SECRET'), cluster=config('PUSHER_CLUSTER'))

@csrf_exempt
@api_view(["GET"])
def initialize(request):
    print('***************************checking response in get request***********************', request.user.player.currentRoom)
    user = request.user
    player = user.player
    player_id = player.id
    uuid = player.uuid
    room = player.room()
    players = room.playerNames(player_id)
    return JsonResponse({'uuid': uuid, 'name':player.user.username, 'title':room.title, 'description':room.description, 'players':players, 'x':room.x, 'y':room.y}, safe=True)

@csrf_exempt
@api_view(["GET"])
def rooms(request):
    user = request.user
    rooms = serializers.serialize('json', Room.objects.all()) 

    # room = user.room
    print(f'*******************************checking the info receieved from the user: {user}***********************************')

    # return JsonResponse({'roomlist': room.roomlist})
    return HttpResponse(rooms, content_type="application/json")
    



@csrf_exempt
@api_view(["POST"])
def move(request):
    dirs={"n": "north", "s": "south", "e": "east", "w": "west"}
    reverse_dirs = {"n": "south", "s": "north", "e": "west", "w": "east"}
    player = request.user.player
    player_id = player.id
    player_uuid = player.uuid
    data = json.loads(request.body)
    direction = data['direction']
    play_x = data['x']
    play_y = data['y']
    room = player.room()
    # print('*********************************************')
    # rE = Room.objects.get(id=room.e_to)
    # print(rE.x)
    # print('*********************************************')
    nextRoomID = None
    if direction == "n":
        nextRoomID = room.n_to
        player.x = play_x
        player.y = play_y
    elif direction == "s":
        nextRoomID = room.s_to
        player.x = play_x
        player.y = play_y
    elif direction == "e":
        nextRoomID = room.e_to
        player.x = play_x
        player.y = play_y
    elif direction == "w":
        nextRoomID = room.w_to
        player.x = play_x
        player.y = play_y
    if nextRoomID is not None and nextRoomID > 0 and player.stamina > 0:
        nextRoom = Room.objects.get(id=nextRoomID)
        player.currentRoom=nextRoomID
        player.move()
        player.save()
        players = nextRoom.playerNames(player_id)
        currentPlayerUUIDs = room.playerUUIDs(player_id)
        nextPlayerUUIDs = nextRoom.playerUUIDs(player_id)
        # for p_uuid in currentPlayerUUIDs:
        #     pusher.trigger(f'p-channel-{p_uuid}', u'broadcast', {'message':f'{player.user.username} has walked {dirs[direction]}.'})
        # for p_uuid in nextPlayerUUIDs:
        #     pusher.trigger(f'p-channel-{p_uuid}', u'broadcast', {'message':f'{player.user.username} has entered from the {reverse_dirs[direction]}.'})
        return JsonResponse({'name':player.user.username, 'title':nextRoom.title, 'description':nextRoom.description, 'players':players, 'stamina':player.stamina, 'x': player.x, 'y':player.y, 'error_msg':""}, safe=True)
    elif player.stamina == 0:
        players = room.playerNames(player_id)
        player.reset_player()
        return JsonResponse({'name':player.user.username, 'title':room.title, 'description':room.description, 'players':players, 'stamina':player.stamina, 'x': player.x, 'y': player.y,'error_msg':""}, safe=True)
    else:
        players = room.playerNames(player_id)
        return JsonResponse({'name':player.user.username, 'title':room.title, 'description':room.description, 'players':players, 'stamina':player.stamina, 'error_msg':"You cannot move that way."}, safe=True)

@csrf_exempt
@api_view(["POST"])
def say(request):
    # IMPLEMENT
    return JsonResponse({'error':"Not yet implemented"}, safe=True, status=500)


@csrf_exempt
@api_view(["POST"])
def pick_up(request):
    fruit = {'apple', 'orange', 'banana'}
    user = request.user
    player = request.user.player
    player_id = player.id
    data = json.loads(request.body)
    item_id = data['item_id']
    # room_id = data['room_id']
    fruit = Item.objects.get(id=item_id)
    fruit.pick_up(player_id)
    return JsonResponse({'item_id': fruit.id, 'room_id': fruit.room_id, 'name':fruit.name, 'stamina': fruit.staminaPoints, 'error':""}, safe=True)

@csrf_exempt
@api_view(["POST"])
def drop(request):
  fruit = {'apple', 'orange', 'banana'}
  user = request.user
  player = request.user.player
  data = json.loads(request.body)
  room_id = data['room_id']
  item_id = data['item_id']
  fruit = Item.objects.get(id=item_id)
  fruit.drop_it(room_id)
  return JsonResponse({'item_id':fruit.id, 'room_id':fruit.room_id, 'name':fruit.name, 'stamina':fruit.staminaPoints, 'error':""}, safe=True)

@csrf_exempt
@api_view(["POST"])
def eat(request):
  fruit = {'apple', 'orange', 'banana'}
  user = request.user
  player = request.user.player
  data = json.loads(request.body)
  player_id = player.id
  room_id = data['room_id']
  item_id = data['item_id']
  fruit = Item.objects.get(id=item_id)
  fruit.eat_it(room_id, player_id)
  return JsonResponse({'message':"You ate the item!", 'room_id':fruit.room_id, 'player_id':fruit.player_id, 'error':""}, safe=True)

@csrf_exempt
@api_view(["GET"])
def items(request):
    print('***************************checking response in get request***********************', request.user.player.currentRoom)
    user = request.user
    player = user.player
    player_id = player.id
    item = serializers.serialize('json', Item.objects.all()) 
    return HttpResponse(item, content_type="application/json")