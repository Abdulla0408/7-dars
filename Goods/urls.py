from django.urls import path, include
from Goods import views

urlpatterns = [
    path('', views.banner, name='banner'),
    path('authentication/', include('Goods.authentication.urls')),
    path('back-office/', include('Goods.back-office.urls')),
    path('list/', views.list, name='list_product_enter'),
    path('create/', views.create, name='create_product_enter'),
    path('update/<int:pk>/', views.update, name='update_product_enter'),
    path('delete/<int:pk>/', views.delete, name='delete_product_enter'),
]