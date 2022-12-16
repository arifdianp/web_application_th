from django.urls import path
from .views import home, create_risk, edit_risk, delete_risk
from . import views

urlpatterns = [
    path('', home.as_view(), name="home"),
    path('addRisk/', create_risk.as_view(), name="addRisk"),
    path('editRisk/<int:pk>', edit_risk.as_view(), name="editRisk"),
    path('deleteRisk/<int:pk>', delete_risk.as_view(), name="deleteRisk"),
    path('search', views.search, name="search")
]
