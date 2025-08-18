from django.urls import path
from . import views

urlpatterns = [
    path("test/", views.test, name="test"),
    path('api/get/data/', views.get_data, name='get_data'),
]
