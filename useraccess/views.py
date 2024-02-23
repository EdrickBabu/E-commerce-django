from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# admin admin
# 

# Create your views here.
def signUp(request):

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')

        if password != confirm_password:
            messages.warning(request, "The passwords dont match")
            return redirect('/signup')

        try:
            if User.objects.get(username=email):
                messages.warning(request, "This user already exists")
                return redirect('/signup')

        except Exception as identifier:
            pass

        user = User.objects.create_user(email,email,password)
        user.save()
        messages.success(request, "You have signed up Successfully")
        #return HttpResponse("User created", email)    

    return render(request, 'signup.html')


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('email')
        userpassword = request.POST.get('password1')

        user = authenticate (username = username, password = userpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful")

            next_page = request.GET.get('next', '/')
            return redirect(next_page)

        else:
            messages.warning(request, "Invalid Credentials")
            return redirect('/login')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/")
