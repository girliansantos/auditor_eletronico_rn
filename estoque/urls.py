from django.urls import path
from estoque import views

urlpatterns = [
    path('', views.estoques)
]