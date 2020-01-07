from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST, require_GET
from student.models import Student
from django.views.decorators.csrf import csrf_protect
from django.core.serializers import serialize


# Create your views here.
def homepage(request):
    return render(request, 'home.html')

def student_fetch_form(request):
    return render(request, 'student_fetch.html')

def student_save_form(request):
    return render(request, 'student_save.html')

@require_GET
def get_student(request):
    name = request.GET.get("name", "")
    if not name:
        return JsonResponse({"found": False})
    stu_obj = [(stu.name, stu.age, stu.std) for stu in Student.objects.filter(name__iexact=name)]
    if not stu_obj:
        return JsonResponse({"found": False})
    return JsonResponse({"data": stu_obj})

@require_POST
@csrf_protect
def save_student(request):
    name = request.POST.get("name", "")
    age = request.POST.get("age", -1)
    std = request.POST.get("std", -1)
    if not name or age==-1 or std==-1:
        return JsonResponse({"saved": False}, status=400)
    stu_obj = Student(name=name, age=age, std=std)
    stu_obj.save()
    return JsonResponse({"saved": True})
