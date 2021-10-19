from django.urls import path
from . import views

urlpatterns = [
    path('', views.sales, name='sales'),
    path('saleslist', views.SalesListView.as_view(), name='saleslist')
]