"""
URL configuration for test_task project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, re_path
from rest_framework.routers import DefaultRouter

from lesson.views import LessonViewSet
from product.views import ProductViewSet, UserLessonViewSet, UserProductViewSet, StatisticViewSet

router = DefaultRouter()
router.register('Products', ProductViewSet)
router.register('Lesson', LessonViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user-lessons/<int:user_id>/', UserLessonViewSet.as_view({'get': 'list'}), name='user-lessons'),
    path('user-product/<int:user_id>&<int:product_id>/', UserProductViewSet.as_view({'get': 'list'}), name='user-product'),
    path('product-stats/<int:product_id>', StatisticViewSet.as_view({'get': 'list'}), name='product-stats'),
] + router.urls

