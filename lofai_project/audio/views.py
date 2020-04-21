from django.shortcuts import render
from django.http import HttpResponse

def audio(request):
    # return HttpResponse("<h1>Lo-fi Beat Generator</h1>")
    return render(request, 'audio/audio.html')
