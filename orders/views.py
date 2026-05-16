from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order
from courses.models import Course


@login_required
def cart(request):
    orders = Order.objects.filter(user=request.user, status='pending')
    total = sum(o.course.price for o in orders)
    return render(request, 'orders/cart.html', {'orders': orders, 'total': total})


@login_required
def add_to_cart(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if course.price == 0:
        Order.objects.get_or_create(user=request.user, course=course, defaults={'status': 'paid'})
        return redirect('course_detail', pk=pk)
    Order.objects.get_or_create(user=request.user, course=course, status='pending')
    return redirect('cart')


@login_required
def remove_from_cart(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)
    order.delete()
    return redirect('cart')


@login_required
def checkout(request):
    orders = Order.objects.filter(user=request.user, status='pending')
    if request.method == 'POST':
        orders.update(status='paid')
        return redirect('my_courses')
    total = sum(o.course.price for o in orders)
    return render(request, 'orders/checkout.html', {'orders': orders, 'total': total})