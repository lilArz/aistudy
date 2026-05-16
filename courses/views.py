from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Course, Lesson, UserProgress


def catalog(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    courses = Course.objects.all()
    language = request.GET.get('language')
    level = request.GET.get('level')

    if language:
        courses = courses.filter(language=language)
    if level:
        courses = courses.filter(level=level)

    context = {
        'courses': courses,
        'language': language,
        'level': level,
    }
    return render(request, 'courses/catalog.html', context)


def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    lessons = course.lessons.all()
    purchased = False

    if request.user.is_authenticated:
        from orders.models import Order
        purchased = Order.objects.filter(
            user=request.user,
            course=course,
            status='paid'
        ).exists()

    context = {
        'course': course,
        'lessons': lessons,
        'purchased': purchased,
    }
    return render(request, 'courses/course_detail.html', context)


@login_required
def lesson_detail(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    from orders.models import Order
    from .models import Comment, Like
    
    purchased = Order.objects.filter(
        user=request.user,
        course=lesson.course,
        status='paid'
    ).exists()

    if not purchased:
        return redirect('course_detail', pk=lesson.course.pk)

    progress, _ = UserProgress.objects.get_or_create(
        user=request.user,
        lesson=lesson
    )

    liked = Like.objects.filter(user=request.user, lesson=lesson).exists()
    likes_count = lesson.likes.count()
    comments = lesson.comments.all()

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'quiz':
            answer = request.POST.get('answer', '').strip().lower()
            correct = lesson.quiz_answer.strip().lower()
            if answer == correct:
                progress.completed = True
                progress.save()

        elif action == 'comment':
            text = request.POST.get('text', '').strip()
            if text:
                Comment.objects.create(user=request.user, lesson=lesson, text=text)

        elif action == 'like':
            if liked:
                Like.objects.filter(user=request.user, lesson=lesson).delete()
            else:
                Like.objects.create(user=request.user, lesson=lesson)

        return redirect('lesson_detail', pk=pk)

    context = {
        'lesson': lesson,
        'progress': progress,
        'liked': liked,
        'likes_count': likes_count,
        'comments': comments,
    }
    return render(request, 'courses/lesson_detail.html', context)


@login_required
def my_courses(request):
    from orders.models import Order
    orders = Order.objects.filter(user=request.user, status='paid')
    courses = [order.course for order in orders]

    course_progress = []
    for course in courses:
        lessons = course.lessons.all()
        total = lessons.count()
        completed = UserProgress.objects.filter(
            user=request.user,
            lesson__in=lessons,
            completed=True
        ).count()
        percent = int((completed / total) * 100) if total > 0 else 0
        course_progress.append({
            'course': course,
            'completed': completed,
            'total': total,
            'percent': percent,
        })

    return render(request, 'courses/my_courses.html', {'course_progress': course_progress})