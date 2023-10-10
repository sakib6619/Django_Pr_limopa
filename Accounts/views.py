from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
# Login 
def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.warning(request, "Wrong input")
            return redirect('login')
    return render(request, 'Accounts/login.html')
# Register 
def register(request):
    if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        userName = request.POST['userName']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if len(password) == 0 and len(password1) == 0:
            messages.warning(request, "Input Password !!!")
        elif len(password) < 8:
            messages.warning(request, "Password at least 8 character")
        else:
            if password:
                pass
            else:
                if password == password1:
                    if User.objects.filter(username=userName).exists():
                        messages.warning(request, "Username Already Taken !!!")
                    elif User.objects.filter(email=email).exists():
                        messages.warning(request, "email Already Taken !!!")
                    else:
                        user = User.objects.create_user(first_name=firstName, last_name=lastName, username=userName,
                                                        email=email, password=password)
                        user.set_password(password)
                        user.save()
                        messages.success(request, "User Created !!!")
                        return redirect('login')
                else:
                    messages.warning(request, "Password not matched !!!")

    return render(request, 'accounts/register.html')
def logout(request):
    auth.logout(request)
    messages.warning(request, "logout successful")
    return redirect('login')
def forgotten(request):
    return render(request, 'Accounts/forgotten.html')