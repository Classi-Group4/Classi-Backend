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

def user_info(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            role = data.get('role')
            if role == 'student':
                student = Student.objects.filter(email=email).first()
                if student:
                    user_info = {'name': student.name, 'email': student.email, 'user_type':'student'}
                    return JsonResponse({"status":"success","user_info": user_info})
                else:
                    return JsonResponse({"status":"error","message":"Invalid Email"})
            elif role == 'teacher':
                teacher = Teacher.objects.filter(email=email).first()
                if teacher:
                    user_info = {'name': teacher.name, 'email': teacher.email, 'user_type':'teacher'}
                    return JsonResponse({"status":"success","user_info": user_info})
                else:
                    return JsonResponse({"status":"error","message":"Invalid Email"})
            else:
                return JsonResponse({"status":"error","message":"Invalid role"})
        except Exception as e:
            return JsonResponse({"status":"error","message":"Error retrieving user information"})