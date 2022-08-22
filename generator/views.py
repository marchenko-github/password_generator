from django.shortcuts import render
from django.http import HttpResponse
import random

def homes(request):
     return render(request, "generator_tem/home.html")

def password(request):

     characters = list("abcdefghijklmnopqrstuvwxyz")
     length = int(request.GET.get('length'))

     if request.GET.get("uppercase"):
          characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
     if request.GET.get("special"):
          characters.extend(list("!@#$%^&*"))
     if request.GET.get("numbers"):
          characters.extend(list("123456789"))
     thepassword = ''
     for x in range(length):
          thepassword += random.choice(characters)


     return render(request, "generator_tem/password.html", {'password' : thepassword})

def creator(request):
     return render(request, "generator_tem/creator.html")
