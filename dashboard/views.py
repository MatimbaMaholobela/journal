from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")

def journal_entry(request):
    return render(request,"journal.html")
    
def login(request):
    return render(request,"login.html")
