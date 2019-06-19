from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.models import User
def login_page(request):
	form=LoginForm(request.POST or None)
	
	context= {
		"form": form
	 }
	print("user logged in ")
	if form.is_valid():
		print(form.cleaned_data)
		username=form.cleaned_data.get("username")
		password=form.cleaned_data.get("password")
		user = authenticate( username= username, password= password)    # different for various versions of django
		print(user)
		# print(request.user.is_authenticated())

		if user is not None:
			print(request.user.is_authenticated())
			
			login(request, user)
			# context['form']= LoginForm()
			return redirect("/login")
		else :
			print("error")
	return render(request, "auth/login.html",context)
user= get_user_model()
def register_page(request):
	form=RegisterForm(request.POST or None)
	context= {
		"form": form
	 }
	if form.is_valid():
		print(form.cleaned_data)
		username=form.cleaned_data.get("username")
		password=form.cleaned_data.get("password")
		email=form.cleaned_data.get("email")
	
		new_User=user.objects.create_user(username,email, password)
		print(new_User)
	return render(request, "auth/register.html",context)


def home_page(request):
	context={
		"title":"hello World",
		 "content": "welcome to the home  page",
		 
	}
	if request.user.is_authenticated():
		context["premium_content"]='yeahhhh'

	return render(request, "home_page.html", context)

def about_page(request):
	context={
	"title": "about_page",
	"content": "welcome to the about page"
	}
	return render(request, "home_page.html", context)

def contact_page(request):
	contact_form= ContactForm(request.POST or None)

	context={
	"title": "contact_page",
	"content": "welcome to the contact Page",
	"form": contact_form
	}
	if contact_form.is_valid():
		print(contact_form.cleaned_data)
	# if request.method=='POST':
	# 	print(request.POST)
	# 	print (request.POST.get('fullname'))
	# 	print (request.POST.get('email'))
	# 	print (request.POST.get('content'))
	
	


	return render(request, "contact/view.html",context)