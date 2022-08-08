from django.shortcuts import render

def plataforma(request):
    return render(request, "plataforma/plataforma.html")