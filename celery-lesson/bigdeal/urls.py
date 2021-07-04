from django.urls import path
from bigdeal import views

urlpatterns = [
    path('', views.func),
    path('<int:id>/', views.check)
]