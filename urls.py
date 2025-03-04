from django.urls import path

from . import views


urlpatterns = [
    path('index/',views.Employee_view,name='employe_index'),
    
]

