from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('catalog')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('catalog')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('catalog')

from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    from courses.models import UserProgress
    from orders.models import Order

    total_completed = UserProgress.objects.filter(
        user=request.user, completed=True
    ).count()

    purchased_count = Order.objects.filter(
        user=request.user, status='paid'
    ).count()

    reputation = purchased_count * 2 + total_completed
    knowledge = total_completed * 10

    activity_days = [bool(i % 3) for i in range(28)]
    streak = total_completed

    context = {
        'total_completed': total_completed,
        'purchased_count': purchased_count,
        'reputation': reputation,
        'knowledge': knowledge,
        'activity_days': activity_days,
        'streak': streak,
    }
    return render(request, 'users/profile.html', context)