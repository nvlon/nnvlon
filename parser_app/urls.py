from django. urls import path
from  . import views

urlpatterns= [
    path('sausage_list/', views.ParserFormView.as_view(), name='sausage_list'),
    path('parser_sausage/', views.ParserFormView.as_view(), name='start_parsing'),
]