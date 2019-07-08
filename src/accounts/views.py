from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import  LoginForm, RegisterForm, GuestForm
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.models import User
from django.utils.http import is_safe_url
from .models import GuestEmail
from django.views.generic import CreateView, FormView


from .signals import user_logged_in
# Create your views here.
def guest_register_view(request):
	form=GuestForm(request.POST or None)
	
	context= {
		"form": form
	 }
	print("guest entering email ")
	next_= request.GET.get('next')
	next_post= request.POST.get('next')
	redirect_path= next_ or next_post or None
	if form.is_valid():
		print(form.cleaned_data)
		email= form.cleaned_data.get('email')
		print("printing email",email)
		new_guest_email=GuestEmail.objects.create(email=email)
		request.session['guest_email_id']= new_guest_email.id
		
		print("request.session",request.session['guest_email_id'])
		
		if is_safe_url(redirect_path, request.get_host()):
			return redirect(redirect_path)
		else:
			return redirect("/register/")
	
	return redirect("/register/")


 


# def login_page(request):
# 	form=LoginForm(request.POST or None)
	
# 	context= {
# 		"form": form
# 	 }
# 	# print("user logged in ")
# 	next_= request.GET.get('next')
# 	next_post= request.POST.get('next')
# 	redirect_path= next_ or next_post or None
# 	if form.is_valid():
# 		print(form.cleaned_data)
# 		username=form.cleaned_data.get("username")
# 		password=form.cleaned_data.get("password")
# 		user = authenticate( username= username, password= password)    # different for various versions of django
# 		print(user)
# 		# print(request.user.is_authenticated())

# 		if user is not None:
			
# 			login(request, user)
# 			try:
# 				del request.session['guest_email_id']
# 			except:
# 				pass
# 			if is_safe_url(redirect_path, request.get_host()):
# 				return redirect(redirect_path)
# 			# context['form']= LoginForm()
# 			else:
# 				return redirect("/")
# 		else :
# 			print("error")
# 	return render(request, "accounts/login.html",context)
# user= get_user_model()
#=====================================================================
class RegisterView(CreateView):
 	form_class= RegisterForm
 	template_name='accounts/register.html'
 	success_url= '/login/'



class LoginView(FormView):
	
	form_class=LoginForm
	success_url='/'
	template_name= 'accounts/login.html'
 

	def form_valid(self, form):
		request=self.request
		next_= request.GET.get('next')
		next_post= request.POST.get('next')
		redirect_path= next_ or next_post or None
		email=form.cleaned_data.get("email")
		password=form.cleaned_data.get("password")
		user = authenticate(username= email, password= password)    # different for various versions of django
		print("in the authentication function")
		print("user is ",user)
		# print(request.user.is_authenticated())

		if user is not None:
			
			login(request, user)
			user_logged_in.send(user.__class__, instance= user, request= request)
			try:
				del request.session['guest_email_id']
			except:
				pass
			if is_safe_url(redirect_path, request.get_host()):
				return redirect(redirect_path)
			# context['form']= LoginForm()
			else:
				return redirect("/")
		return super(LoginView, self).form_invalid(form)



# def register_page(request):
# 	form=RegisterForm(request.POST or None)
# 	context= {
# 		"form": form
# 	 }
# 	if form.is_valid():
# 		form.save()
# 		# print(form.cleaned_data)
# 		# username=form.cleaned_data.get("username")
# 		# password=form.cleaned_data.get("password")
# 		# email=form.cleaned_data.get("email")
	
# 		# new_User=user.objects.create_user(username,email, password)
# 		# print(new_User)
# 	return render(request, "accounts/register.html",context)
