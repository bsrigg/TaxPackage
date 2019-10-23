from django.shortcuts import render, redirect, HttpResponse

def index(request):
    # return HttpResponse("This is equiv to app.route.")
    return render(request,'index.html')
