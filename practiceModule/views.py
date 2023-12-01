from django.shortcuts import render
from datetime import datetime

def index(request):
    d = {'name' : 'alif', 'age':45, 'val' : [1,2,3,4,5], 'date' : datetime.now()}
    return render(request,"index.html",d)