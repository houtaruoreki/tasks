from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def login_view(request):
    if not request.session.get('is_authenticated'):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user=user)
                next_url = request.POST.get('next')  # Get the 'next' parameter from the form
                if next_url:
                    return redirect(next_url)
                else:
                    request.session['is_authenticated'] = True
                    return redirect('index')  # Redirect to a specific view ('profile' in this case)
            else:
                # Handle authentication failure
                pass
        return render(request, 'login.html')
    else:
        return redirect('index')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        User.objects.create_user(username=username, email="email@gmail.com", password=password).save()

        return redirect('login')
    return render(request, 'registration.html')


def logout_view(request):
    if request.session.get('is_authenticated'):
        request.session.pop('is_authenticated')
        return redirect('login')
