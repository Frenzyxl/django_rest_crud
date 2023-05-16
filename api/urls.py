from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('add/', views.addData),
    path('update/<int:id>/', views.updateData),
    path('delete/<int:id>/', views.deleteData),
]