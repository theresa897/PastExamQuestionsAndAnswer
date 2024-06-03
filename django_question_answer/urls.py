"""
URL configuration for django_question_answer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app import urls as myUrls
<<<<<<< HEAD
=======
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
>>>>>>> b1ce08c1bf083affc37742833f736154ebe11708
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView
# )
from rest_framework.routers import DefaultRouter


urlpatterns = [
<<<<<<< HEAD
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/',  TokenRefreshView.as_view(), name='token_refresh'),
=======
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/',  TokenRefreshView.as_view(), name='token_refresh'),
>>>>>>> b1ce08c1bf083affc37742833f736154ebe11708
    path('', include(myUrls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
