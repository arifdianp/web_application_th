from django.urls import path
from .views import home, create_risk

urlpatterns = [
    path('', home.as_view(), name="home"),
    path('addRisk/', create_risk.as_view(), name="addRisk")
]
