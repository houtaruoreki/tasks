import json

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Diaries


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user=user)
            next_url = request.POST.get('next')  # Get the 'next' parameter from the form
            if next_url:
                return redirect(next_url)
            else:
                return redirect('index')  # Redirect to a specific view ('profile' in this case)
        else:
            # Handle authentication failure
            pass
    return render(request, 'login.html')


def index(request):
    user_id = request.user.id
    filtered_diaries = Diaries.objects.filter(user_id=user_id)
    context = {'filtered_diaries': filtered_diaries,
               'user_id': user_id}

    return render(request, 'index.html', context)


def add_diary(request):
    if request.method == 'POST':
        user = User.objects.filter(id=request.user.id).first()
        data = json.loads(request.body)

        # Assuming the data keys are 'memo' and 'tags'
        memo = data.get('memo')
        tags = data.get('tags')
        new_diary_entry = Diaries.objects.create(
            user=user,
            memo=memo,
            tags=tags
        )
        new_diary_entry.save()
        return redirect('index')
