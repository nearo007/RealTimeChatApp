from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Room

# Create your views here.
def index(request):
    return render(request, 'index.html')

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
            newroom = Room.objects.create(name=room_name)
            newroom.save()
            return redirect('/'+room_name+'/?username='+username)
    
    else:
        return redirect('index')