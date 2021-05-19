from django.shortcuts import render
from django.http import JsonResponse
from django.utils.http import is_safe_url
# Create your views here.
import stripe 

stripe.api_key= "---"

STRIPE_PUB_KEY= "---"
def payment_method_view(request):
	next_url=None
	next_= request.GET.get('next')
	if is_safe_url(next_, request.get_host()):
		next_url= next_
	
	return render(request, 'billing/payment-method.html',
							{"publish_key":STRIPE_PUB_KEY,
							"next_url": next_url} )



def payment_method_createview(request):
	if request.method== "POST":
		print(request.POST)
		return JsonResponse({"message": "success! Your card was added"})

	return HttpResponse("error", status_code=401)
