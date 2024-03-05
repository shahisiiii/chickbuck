"""
URL configuration for chickbuck project.

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
from django.urls import path,include
from acounts.views import Register, Login
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
from chickbuck_api.views import CategoryView,ItemsView,CategoryReadOnlyView,ItemReadOnlyView,CartItemViewSet

router = DefaultRouter()
router.register(r'categories', CategoryView)
router.register(r'categoriesuser', CategoryReadOnlyView)
router.register(r'addtocart', CartItemViewSet)

router.register(r'itemsuser', ItemReadOnlyView)
router.register(r'items', ItemsView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),   
    path('', include(router.urls)),
]



