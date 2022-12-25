from django.contrib import admin
from django.urls import path, include
from .views import home, create_risk, edit_risk, delete_risk, userRegister, userStatus
from . import views

urlpatterns = [
    path('', home.as_view(), name="home"),
    path('addRisk/', create_risk.as_view(), name="addRisk"),
    path('editRisk/<int:pk>', edit_risk.as_view(), name="editRisk"),
    path('deleteRisk/<int:pk>', delete_risk.as_view(), name="deleteRisk"),
    path('search', views.search, name="search"),
    path('register/', views.userRegister, name="register"),
    path('addstatus/', userStatus.as_view(), name="addstatus")
]
