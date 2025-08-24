from django.urls import path
from . import views


urlpatterns = [
    path("test/", views.test, name="test"),
    path('api/get/data/json/', views.get_data_json, name='train-data-json'),
    path('api/get/data/', views.get_data, name='get_data'),
]

