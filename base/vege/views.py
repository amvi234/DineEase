from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required
def receipes(request):
    if request.method == "POST":
        data = request.POST
        receipe_price = data.get('receipe_price')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        Receipe.objects.create(
            receipe_price = receipe_price,
            receipe_name = receipe_name,
            receipe_description = receipe_description,
        )

        return redirect('/')
    
    queryset = Receipe.objects.all()

    # if request.GET.get('search'):
    #     queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))

    context = {'receipes': queryset}

    return render(request, 'receipes.html', context)

# @login_required
def update_receipe(request, id):
    queryset = Receipe.objects.get(id = id)

    if request.method == 'POST':
        data = request.POST
        receipe_price = data.get('receipe_price')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        queryset.receipe_name = receipe_name
        if receipe_description:
            queryset.receipe_description = receipe_description
        
        if receipe_price:
            queryset.receipe_price = receipe_price

        queryset.save()
        return redirect('/')

    context = {'receipe': queryset}

    return render(request, 'update_receipes.html', context)

# @login_required
def delete_receipe(request, id):
    queryset = Receipe.objects.get(id = id)
    queryset.delete()
    return redirect('/')

def login_page(request):
    # queryset = CustomUser.objects.get(id = id)
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid username')
            return redirect('/login')
        
        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('/login')
        
        else:
            login(request, user)
            return redirect('/')
        
    return render(request, 'login.html', {})

def logout_view(request):
    logout(request)
    return redirect('/login/')

def register_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if len(password) < 8:
            messages.error(request, 'Password must be atleast 8 characters')
            return redirect('register')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, 'username already exists')
            return redirect('/register/')

        user = User.objects.create_user(
            first_name = first_name,
            last_name = last_name,
            username = username,
            password = password,
        )
        user.save()

        messages.info(request, 'Account Created Successfully')

        return redirect('/login/')

    return render(request, 'register.html')