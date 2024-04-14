from django.http import HttpResponse
from django.shortcuts import redirect, render
# import the journal from models and pass variables


# Create your views here.
def home(request):
    return render(request, "home.html")

def journal_entry(request):
    return render(request,"journal.html")
    
def login(request):
    return render(request,"login.html") 

def login_cred(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password= request.POST.get("password")
        print("Username: ", username)
        print("Password: ", password)
        
        return render(request,"home.html") 
    
    else:
        return HttpResponse(status=404)
    
def journal_login(request):
    if request.method == "POST":
        entryDate=request.POST.get("entryDate")
        entryTitle=request.POST.get("entryTitle")
        entryContent=request.POST.get("entryContent")

        
