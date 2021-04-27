from django.shortcuts import render, get_object_or_404, redirect
from .models import Visit
from .forms import UserForm


def home(request):
    users = Visit.objects.all()  # list of objects
    context = {
        "users": users
    }
    return render(request, 'index.html', context)


def detail(request, user_id):
    user = get_object_or_404(Visit, pk=user_id)
    context = {
        "user": user
    }
    return render(request, 'detail.html', context)


def add_user(request):
    if request.method == 'GET':
        return render(request, 'add_user.html', {'form': UserForm()})
    else:
        try:
            form = UserForm(request.POST)
            newuser = form.save()
            return redirect('/')
        except ValueError:
            return render(request, 'add_user.html', {'form': UserForm(), 'error': 'Bad data passed in. Try again'})

