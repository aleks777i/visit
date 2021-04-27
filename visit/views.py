from django.shortcuts import render, get_object_or_404, redirect
from .models import Visit
from .forms import UserForm
from django.http import HttpResponse


def home(request):
    users = Visit.objects.all()  # list of objects
    context = {
        "users": users
    }
    return render(request, 'index.html', context)


def detail(request, user_id):
    user = get_object_or_404(Visit, pk=user_id)
    if request.method == 'GET':
        form = UserForm(instance=user)
        return render(request, 'detail.html', {'form': form, 'user': user})
    else:
        try:
            form = UserForm(request.POST, instance=user)
            form.save()
            return redirect('/')
        except ValueError:
            return render(request, 'add_user.html', {'form': form, 'user': user, 'error': 'Bad data passed in. Try again'})


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


def delete_user(request, user_id):
    user = get_object_or_404(Visit, pk=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('/')
    else:
        user.delete()
        atbilde = "Deleted " + user.name
        return HttpResponse(atbilde)


