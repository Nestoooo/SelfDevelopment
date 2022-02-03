from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Category, Room, Message
from .forms import RoomForm, MessageForm
from django.contrib.auth.models import User
from django.http import HttpResponse



# user can login or get an error message  & navegation bar included
def login_page(request):
    if request.method=='POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        try:
            user= User.objects.get(username=username)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'username or password is not exist')
        except :
            messages.error(request, 'username is not exist')

    context ={}
    return render(request, 'base/login.html' , context)

#user can logout
def logout_page(request):
    logout(request)
    return redirect('home')

#user can see all categories in the home page and get in it & create new rooms  & navegation bar included
def home(request):
    category = Category.objects.all()
    #rooms = Room.objects.all()
    context ={'category': category}
    return render(request, "base/home.html", context)

#user can see all rooms in every category with the room details & navegation bar included
def category(request, pk):
    #get all rooms of specific category
    categorys = Category.objects.get(id=pk)
    rooms = Room.objects.all()
    room=[]
    for x in rooms:
        if x.category == categorys:
            room.append(x)

    context ={'categorys': categorys, 'room': room }
    return render(request, "base/category.html", context)

#user can see room details and all the comments inside this room & navegation bar included
def room(request, pk):
    #get descriptions of rooms
    room = Room.objects.get(id=pk)
    room_messages= Message.objects.filter(room=room)

    if request.method == 'POST':
        #message=request.POST
        message= Message.objects.create(
            user= request.user,
            room= room,
            body= request.POST.get('message')
        )
        return(redirect('room', pk=room.id))

    context = {'room': room, 'room_messages': room_messages}
    return render(request, 'base/room.html' , context)

#user can create new room & it will be saved in the database
@login_required(login_url='login')
def create_room(request):
    form= RoomForm()
    if request.method=='POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={'form': form }
    return render(request, 'base/room_form.html', context)

#user can update a room &the updates will be saved
def update_room(request,pk):
    room= Room.objects.get(id=pk)
    form= RoomForm(instance=room)

    if request.method == 'POST':
        form=RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form': form}
    return render(request, 'base/room_form.html', context)

#user can delete the room
def delete_room(request, pk):
    room= Room.objects.get(id=pk)
    if request.method== 'POST':
        room.delete()
        return redirect('home')
    context={'room':room}
    return render(request, 'base/delete.html', context)
