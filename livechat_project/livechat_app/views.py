from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Room, Message
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    available_rooms = list(Room.objects.get_queryset())

    context = {'available_rooms': available_rooms}

    return render(request, 'index.html', context)

def room(request, room):
    room_details = get_object_or_404(Room, name=room)
    username = request.GET.get('username')

    context = {
        'room_name':room,
        'room_details': room_details,
        'username': username,
        }
    
    return render(request, 'room.html', context)

def checkview(request):
    if request.method == "POST":
        room_name = request.POST['room_name']
        username = request.POST['username']

        if Room.objects.filter(name=room_name).exists():
            return redirect('/'+room_name+'/?username='+username)
        
        else:
            new_room = Room.objects.create(name=room_name)
            new_room.save()
            return redirect('/'+room_name+'/?username='+username)
    
    else:
        return redirect('index')
    
def send(request):
    if request.method == 'POST':
        room_id = request.POST['room_id']
        #room = Room.objects.filter(room_id=room_id) # Django creates OBJETO + _id automatically

        username = request.POST['username']
        message = request.POST['message']

        new_message = Message.objects.create(value=message, user=username, room_id=room_id)
        new_message.save()
        
    return HttpResponse('Message sent succesfully!')

def get_available_rooms(request):
    if request.method == 'GET':
        available_rooms = list(Room.objects.values())
        context = {'available_rooms': available_rooms}

        return JsonResponse(context)

def get_messages(request, room_name, room_id):
    if request.method == 'GET':
        room_messages = Message.objects.filter(room_id=room_id)
        
        context = {'room_messages': list(room_messages.values())}

        return JsonResponse(context)
    
def delete_room(request, room_name):
    if request.method == 'GET':
        room = Room.objects.get(name=room_name)
        room.delete()

        return redirect('index')