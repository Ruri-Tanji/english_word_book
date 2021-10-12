from django.urls import path
from . import views

urlpatterns = [
    path('', views.top, name='top'),
    path('index/', views.index, name='index'),
    path('detail/<int:vocab_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('about/', views.about, name='about'),
    # path('edit/<int:vocab_id>/', views.edit, name='edit')
]
