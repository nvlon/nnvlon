from django . urls import path
from . import views

urlpatterns=[
    path('', views.CarListView.as_view(), name = 'car_list'),
    path('car_list/<int:id>/', views.CarDetailView.as_view(),name='car_detail'),
    path('car_list/<int:id>/update/' , views.CarUpdateView.as_view, name='update'),
    path('car_list/<int:id>/delete/', views.CarDeleteView.as_view(), name='delete'),

    path('create_car/', views.CreateCarView.as_view(), name= 'create'),
    path('search/' , views.Search.as_view(), name= 'search'),
]