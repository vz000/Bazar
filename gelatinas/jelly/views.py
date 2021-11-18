from django.shortcuts import render

# Create your views here.
def home(request): 
    if request.user_agent.is_mobile:
        return render(request,"home.html")
    else:
        return render(request,"notavailable.html")