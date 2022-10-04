from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def dashboard (request, id):
    myuser = User.objects.get(id=id)
    return render (request,'dashboard.html')