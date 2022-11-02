from django.shortcuts import render

def index(request):
    return render(request, "chat/template/chat/index.html")

def room(request, room_name):
    return render(request, "chat/template/chat/room.html", {"room_name": room_name})

