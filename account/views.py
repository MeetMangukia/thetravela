from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

def edit_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = User.objects.get(pk=request.user.id)
            
            user.username = request.POST['username']
            user.email = request.POST['email'] 
            user.userprofile.phone = request.POST['phone'] 
            user.userprofile.gender = request.POST['gender'] 
            user.userprofile.dob = request.POST['dob']
            user.userprofile.address = request.POST['address']

            user.save()  
    return render(request, "account/edit-profile.html")
