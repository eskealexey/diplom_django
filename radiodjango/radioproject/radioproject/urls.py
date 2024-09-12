"""radioproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.template.defaulttags import url

from django.urls import path, include # new
from django.conf.urls.static import static # new
from app.views import index_app, transistor_app, transistor_app_id, transistor_forma_add
from users.views import register, LoginUser

from users.views import loguot_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_app, name='home'),
    path('transistor/', transistor_app, name='transistorlist'),
    path('transistor/<int:id_tr>/', transistor_app_id, name='transistorview'),
    path('transistor/formadd/', transistor_forma_add, name='transistoradd'),
    path('registration/', register, name='registration'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', loguot_user, name='logout')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)