from django.urls import path
from . import views
from .views import feedback

urlpatterns = [
    path('', views.homepage, name='home'),
    path('members/', views.members, name='members'),
    path('members/details/<slug:slug>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    path('feedback', feedback),
]
