"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from allauth.account.views import confirm_email
from django.conf.urls import url
from django.conf import settings  
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    ### rest-auth login/logout
    path('api/rest-auth/', include('rest_auth.urls')),
    ### rest-auth signup/
    url('api/rest-auth/signup/', include('rest_auth.registration.urls')),
    # 뒤에 한다.
    path('accounts/', include('allauth.urls')),
    # 이메일인증을 위한거
    url(r'^rest-auth/singup/account-confirm-email/(?P<key>.+)/$', views.ConfirmEmailView.as_view(), name='account_confirm_email'),
    path("api/", include("api.urls"))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
