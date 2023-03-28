from django . urls import path
from . import views

urlpatterns=[
    path('car_list/', views.car_list_view, name = 'car_list'),
    path('car_list/<int:id>/', views.car_detail_view,name='car_detail'),
    path('car_list/<int:id>/update/' , views.update_car_view, name='update'),
    path('car_list/<int:id>/delete/', views.update_car_view, name='delete'),

    path('car_list/', views.create_car_views, name= 'create'),
]