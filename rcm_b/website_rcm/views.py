from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
# Create your views here.


def home(request):
    #vérifier si vous êtes connecté
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        #Authentifier
        user = authenticate(
            request,
            username = username,
            password = password
        )

        if user is not None:

            login(request, user)
            messages.success(request, "Vous avez été connecté")

            return redirect('home')
        else:
            messages.success(request, "Le nom ou le mots de passe n'existe pas dans votre systeme informatique")        
    return render(request, 'home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "Deconnection effectuée avec succès")
    return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})

