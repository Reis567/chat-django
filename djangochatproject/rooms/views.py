from django.shortcuts import render
from .models import Room
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'rooms/homerooms.html',{
        'rooms':rooms
    })

@login_required
def room(request,slug):
    room = Room.objects.get(slug=slug)

    return render(request, 'rooms/room.html',{
        'room':room
    })