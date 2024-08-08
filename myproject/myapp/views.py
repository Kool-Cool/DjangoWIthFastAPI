from django.shortcuts import render
import requests
from .fastapi import hello
# Create your views here.

def home(request):
    response = requests.get("http://localhost:5000/api/data")
    data = response.json()

    return render(request , "home.html" ,{"message": data["message"]})
