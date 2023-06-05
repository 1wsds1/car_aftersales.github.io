from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def QA(request):
    return render(request, 'QA.html', {})

def tb(request):
    return render(request, 'tb.html', {})

def room(request, room_name):
    return render(request, 'room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })


# Create your views here.
