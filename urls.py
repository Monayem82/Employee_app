from django.urls import path

from . import views


urlpatterns = [
    path('index/',views.Employee_view,name='employe_index'),
    path('edit/<int:pk>',views.Employee_edit_view,name='employe_edit'),
    
]

