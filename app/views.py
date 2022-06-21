from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q  # QuerySet for complex queries in filter
from . models import *
from django.contrib.auth.forms import UserCreationForm
from . forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import re

# Create your views here.

# rooms=[
#     {'id':1, 'name':'Python Developers'},
#     {'id':2, 'name':'React Developers'},
#     {'id':3, 'name':'Java Developers'},
# ]


def loginPage(request):
    page = 'login'
    context = {'page': page}
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User with this email does not exist')
            return render(request, 'app/login_register.html', context)

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Password does not exist')
    return render(request, 'app/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = MyUserCreationForm()

    if request.method == 'POST':
        reg = "^(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$"
        pattern = re.compile(reg)

        pswd1=request.POST.get('password1')
        pswd2=request.POST.get('password2')
        
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        elif pswd1 != pswd2:
            messages.error(request, 'Both passwords should match')
        elif not(re.search(pattern, pswd1)) or not(re.search(pattern, pswd2)):
            messages.error(request, "Password should be atleast 8chars & include alphanumeric and symbols")
        else:
            messages.error(request, 'This email or username has already been registered')

    context = {'form': form}
    return render(request, 'app/login_register.html', context)



@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', user.id)
        else:
            messages.error(request, 'This email or username has already been registered')
    context = {
        'form': form
    }
    return render(request, 'app/update-user.html', context)


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )
    topics = Topic.objects.all()[:5]
    room_count = rooms.count()
    mssgs = Message.objects.filter(Q(room__topic__name__icontains=q))
    TOTAL_ROOMS = Room.objects.all().count()

    context = {
        'rooms': rooms,
        'topics': topics,
        'room_count': room_count,
        'mssgs': mssgs,
        'TOTAL_ROOMS': TOTAL_ROOMS
    }
    return render(request, 'app/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    participants = room.participants.all()
    mssgs = room.message_set.all()
    # mssgs=Message.objects.filter(room=room) #same as above

    if request.method == 'POST':
        mssg = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room', pk=room.id)

    context = {
        'room': room,
        'mssgs': mssgs,
        'participants': participants
    }

    return render(request, 'app/room.html', context)


def userProfile(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    mssgs = user.message_set.all()
    topics = Topic.objects.all()
    TOTAL_ROOMS = Room.objects.all().count()

    context = {
        'user': user,
        'rooms': rooms,
        'topics': topics,
        'mssgs': mssgs,
        'TOTAL_ROOMS': TOTAL_ROOMS
    }
    return render(request, 'app/profile.html', context)


@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()
    topics = Topic.objects.all()

    if request.method == 'POST':
        topic_name = request.POST['topic']
        topic, created = Topic.objects.get_or_create(name=topic_name)

        room, created = Room.objects.get_or_create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name')
        )
        if created:
            room.description = request.POST.get('description')
            room.save()
        else:
            messages.error(
                request, f'Room with name "{room.name}" has already been created by you')
            return redirect('create-room')

        # form = RoomForm(request.POST)
        # if form.is_valid():
        #     room=form.save(commit=False)
        #     room.host=request.user
        #     room.save()
        return redirect('room', room.id)

    context = {'form': form, 'topics': topics}
    return render(request, 'app/room_form.html', context)


@login_required(login_url='login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    topics = Topic.objects.all()

    if request.user != room.host:
        return HttpResponse('You are not allowed here!!')

    if request.method == 'POST':
        topic_name = request.POST['topic']
        topic, created = Topic.objects.get_or_create(name=topic_name)

        room.name = request.POST.get('name')
        room.topic = topic
        room.description = request.POST.get('description')
        room.save()
        # form = RoomForm(request.POST, instance=room)
        # if form.is_valid():
        #     form.save()
        return redirect('room', pk)

    context = {'form': form, 'topics': topics, 'room': room}
    return render(request, 'app/room_form.html', context)


@login_required(login_url='login')
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse('You are not allowed here!!')

    if request.method == 'POST':
        room.delete()
        return redirect('home')

    context = {'obj': room.name}
    return render(request, 'app/delete.html', context)


@login_required(login_url='login')
def deleteMessage(request, pk):
    mssg = Message.objects.get(id=pk)

    if request.user != mssg.user:
        return HttpResponse('You are not allowed here!!')

    if request.method == 'POST':
        mssg.delete()
        return redirect('home')

    context = {'obj': mssg.body}
    return render(request, 'app/delete.html', context)


def topicPage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    topics = Topic.objects.filter(name__icontains=q)
    TOTAL_ROOMS = Room.objects.all().count()
    context = {'topics': topics,
    'TOTAL_ROOMS':TOTAL_ROOMS}
    return render(request, 'app/topics.html', context)


def activityPage(request):
    mssgs = Message.objects.all()
    context={
        'mssgs':mssgs
    }
    return render(request, 'app/activity.html', context)