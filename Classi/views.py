# from django.shortcuts import render, redirect
# from .models import Student
# from django.contrib.auth import authenticate, login
# from django.http import JsonResponse


# def student_registration(request):
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         email = request.POST['email']
#         password = request.POST['password']
#         date_of_birth = request.POST['date_of_birth']
#         address = request.POST['address']
#         student = Student(first_name=first_name, last_name=last_name, email=email, password=password, date_of_birth=date_of_birth, address=address)


#         student.save()
#         return JsonResponse({"status":"success","message":"Register Successful"})
#     else:
#         return JsonResponse({"status":"error","message":"Invalid request"})




# def login_view(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user = authenticate(request, email=email, password=password)
#         if user is not None:
#             login(request, user)
#             # Return a success message
#             return JsonResponse({"status":"success","message":"Login Successful"})
#         else:
#             # Return an error message
#             return JsonResponse({"status":"error","message":"Invalid login"})
#     else:
#         return JsonResponse({"status":"error","message":"Invalid request"})

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Student,Teacher
from django.http import JsonResponse
import json

def student_registration(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            password = data.get('password')
            student = Student(name=name, email=email, password=password)
            student.save()
            return JsonResponse({"status":"success","message":"Student registered"})
        except Exception as e:
            return JsonResponse({"status":"error","message":"error creating student"})
        
def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')
            student = Student.objects.filter(email=email).first()
            if student:
                if student.password == password:
                    return JsonResponse({"status":"success","message":"Student logged in"})
                else:
                    return JsonResponse({"status":"error","message":"Invalid login"})
            else:
                return JsonResponse({"status":"error","message":"Invalid login"})
        except Exception as e:
            return JsonResponse({"status":"error","message":"error logging in"})

def teacher_registration(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            password = data.get('password')
            student = Teacher(name=name, email=email, password=password)
            student.save()
            return JsonResponse({"status":"success","message":"Teacher registered"})
        except Exception as e:
            return JsonResponse({"status":"error","message":"error creating teacher"})
        
def teacher_login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')
            student = Teacher.objects.filter(email=email).first()
            if student:
                if student.password == password:
                    return JsonResponse({"status":"success","message":"teacher logged in"})
                else:
                    return JsonResponse({"status":"error","message":"Invalid login"})
            else:
                return JsonResponse({"status":"error","message":"Invalid login"})
        except Exception as e:
            return JsonResponse({"status":"error","message":"error logging in"})