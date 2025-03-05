from django.urls import path

from . import views


urlpatterns = [
    path('index/',views.Employee_view,name='employe_index'),
    path('edit/<int:pk>',views.Employee_dashbord_view,name='employe_edit'),
    path('edit_up/',views.Employee_edit_view,name='employe_create'),
    path('edit_up/<int:pk>',views.Employee_edit_view,name='employe_edit_up'),
    
]

