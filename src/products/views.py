from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product
from django.http import Http404
from carts.models import Cart
from analytics.mixins import ObjectViewedMixin




class ProductFeaturedListView(ListView):
	template_name= "products/list.html"
	def get_queryset(self,*args, **kwargs ):
		request=self.request
		return Product.objects.featured()

class ProductFeaturedDetailView(ObjectViewedMixin,DetailView):
	
	template_name= "products/featured-detail.html"

	def get_queryset(self,*args, **kwargs ):
		request=self.request
		return Product.objects.featured()




class ProductListView(ListView):
	# queryset= Product.objects.all()
	template_name= "products/list.html"

	# def get_context_data(self, *args, **kwargs):
	# 	context= super(ProductListView,self).get_context_data(*args, **kwargs)
	# 	print(context)
	# 	return context

	def get_context_data(self, *args, **kwargs):
		context= super(ProductListView, self).get_context_data(*args, **kwargs)
		cart_obj,new_obj= Cart.objects.new_or_get(self.request)
		context['cart']= cart_obj
		return context


	def get_queryset(self,*args, **kwargs ):
		request=self.request
		return Product.objects.all()

def product_list_view(request):
	queryset= Product.objects.all()
	context={
	'object_list':queryset
	}
	return render(request, "products/list.html", context)
# Create your views here.

class ProductDetailSlugView(ObjectViewedMixin,DetailView):
	queryset= Product.objects.all()
	template_name="products/detail.html"
	
	def get_context_data(self, *args, **kwargs):
		context= super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
		cart_obj,new_obj= Cart.objects.new_or_get(self.request)
		context['cart']= cart_obj
		return context



	def get_object(self, *args, **kwargs):
		request= self.request
		slug=self.kwargs.get('slug')



		try:
			instance= Product.objects.get(slug=slug, active=True)
		except Product.DoesNotExist:
			raise Http404("N ot found")
		except Product.MulitipleObjectsReturned:
			qs= Product.objects.filter(slug=slug, active=True)
			instance=qs.first()
		except:
			raise Http404("Uhmmm")

		# object_viewed_signal.send(instance.__class__, instance=instance, request=request)
		return instance


class ProductDetailView(ObjectViewedMixin,DetailView):
	queryset= Product.objects.all()
	template_name= "products/detail.html"

	def get_context_data(self, *args, **kwargs):
		context= super(ProductDetailView,self).get_context_data(*args, **kwargs)
		
		print("context is ",context)
		# context['abc']=123
		return context
	def get_object(self, *args, **kwargs):
		request= self.request
		pk= self.kwargs.get('pk')
		instance =Product.object.get_by_id(pk)
		if instance is None:
			raise Http404("Product doesnt exit")
		return instance

	# def get_queryset(self,*args, **kwargs ):
	# 	request=self.request
	# 	pk= self.kwargs.get('pk')
	# 	return Product.objects.filter(pk=pk)


def product_detail_view(request, pk=None, *args, **Kwargs):
	# instance= Product.objects.get(pk=pk , featured=True)
	# instance= get_object_or_404(Product, pk=pk,featured=True)
	# try:

	# 	instance= Product.objects.get(id=pk)
	# except Product.DoesNotExist:
	# 	print('no product here')
	# 	raise Http404("Product doesnt not exist") 
	# except:
	# 	print ('huh ?')
	instance= Product.objects.get_by_id(pk)
	if instance is None:
		raise Http404("Product doesnt exist")

	# print(instance)

	# qs= Product.objects.filter(id=pk)
	# print(qs)
	# if qs.exists() and qs.count()==1:
	# 	instance= qs.first()
	# else:
	# 	raise Http404("Product doesnt not exist")

	context={
	'object':instance
	}
	return render(request, "products/detail.html", context)
# Create your views here.
 