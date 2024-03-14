from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")

def journal(request):
    return render(request,"journal.html")