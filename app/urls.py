from django.urls import path
from . import views
urlpatterns = [
    path('', views.ProductListView.as_view(), name='main-page'),
    path('create_product', views.ProductCreateView.as_view(), name='create-product'),
]