from django.shortcuts import render
from notes.models import note
# Create your views here.

def base(request):
    return render(request,'base.html')
