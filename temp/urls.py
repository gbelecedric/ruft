
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('category', views.category),
    path('archive', views.archive),
    path('blog', views.blog),
    path('contact', views.index),
    
]