"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.contrib.auth.views import LogoutView

# from django.conf.urls import url, include
# from django.contrib import admin

# from django.conf import settings
# from django.conf.urls.static import static
# from .views import home_page, about_page, contact_page
# from django.views.generic import TemplateView
from carts.views import cart_home
from accounts.views import LoginView, RegisterView, guest_register_view

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import logout   # logout | login ---depricated in django 1.11
from django.views.generic import TemplateView, RedirectView
from .views import home_page, about_page, contact_page
from addresses.views import checkout_address_create_view, checkout_address_reuse_view
from carts.views import cart_detail_api_view
from billing.views import payment_method_view, payment_method_createview
urlpatterns = [
    url(r'^$', home_page,name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^home/', home_page, name='home'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^register/guest$', guest_register_view, name='guest_register'),
    url(r'^checkout/address/create/$', checkout_address_create_view, name='checkout_address_create'),
    url(r'^checkout/address/reuse/$', checkout_address_reuse_view, name= 'checkout_address_reuse'),
    
    url(r'^cart/',include("carts.urls", namespace='cart')),
    url(r'^logout/$',logout, name='logout'),
    url(r'^api/cart/$',cart_detail_api_view, name='api-cart'),
    url(r'^register/', RegisterView.as_view(), name='register'),
    url(r'^billing/payment_method', payment_method_view, name='billing_payment_method'),
    url(r'^billing/payment_method/create', payment_method_createview, name='billing_payment_method_endpoint'),

    url(r'^bootstrap/$',TemplateView.as_view(template_name='bootstrap/example.html')),
    url(r'^products/',include("products.urls", namespace='products')),
    url(r'^search/',include("search.urls", namespace='search')),
    url(r'^about/', about_page, name='about'),
    url(r'^contact/', contact_page, name='contact'),


]



if settings.DEBUG:
	urlpatterns= urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns= urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)