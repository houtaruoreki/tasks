from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Diaries
import json


# Create your views here.
def index(request):
    if request.session.get('is_authenticated'):
        user_id = request.user.id
        filtered_diaries = Diaries.objects.filter(user_id=user_id)
        context = {'filtered_diaries': filtered_diaries,
                   'user_id': user_id,
                   'username': request.user.username}

        return render(request, 'index.html', context)
    else:
        return redirect('/login')


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
