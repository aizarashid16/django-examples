from django.shortcuts import render
from usersApp.models import User
from usersApp.forms import NewUserForm

# Create your views here.
def index(request):
    return render(request,'usersApp/users.html')

def Users(request):
    form = NewUserForm()
    if request.method =="POST":
        form = NewUserForm(request.POST)

    if form.is_valid():
        form.save(commit = True)
        return index(request)
    else:
        print("ERROR FORM INVALID!")
        return render(request,'usersApp/users.html',{'form':form})
