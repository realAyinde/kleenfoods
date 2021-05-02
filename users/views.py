from django.shortcuts import render, redirect
from .models import User
from .forms import UserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.
# class UserListView(ListView):
#     model = User
#     template_name = "home.html"

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm
        
    context = {'form': form}
    return render(request, 'registration/signup.html', context)

# def signIn(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)

#         if form.is_valid():
#             form.save()
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password1']
#             user = authenticate(email=email, password=password)
#             login(request, user)
#             return redirect('/')
#     else:
#         form = UserCreationForm
    
#     context = {'form': form}
#     return render(request, 'registration/signup.html', context)
