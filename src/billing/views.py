from django.shortcuts import render
from django.http import JsonResponse
from django.utils.http import is_safe_url
# Create your views here.
import stripe 

stripe.api_key= "sk_test_V71rYXMxaIj2PzbbrcXERB2L00jlR3Sodn"

STRIPE_PUB_KEY= "pk_test_kBxDy3i9kU4ir6LiN6Ajtna900zDrbQNwE"
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