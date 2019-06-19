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
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import home_page, about_page, contact_page, login_page , register_page 
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', home_page, name='home'),
    url(r'^login/', login_page, name='login_page'),
    url(r'^register/', register_page, name='register _page'),

    url(r'^$', home_page),
    url(r'^about/', about_page, name='about'),
    url(r'^contact/', contact_page, name='contact'),


]
if settings.DEBUG:
	urlpatterns= urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns= urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)