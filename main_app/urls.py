from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('elephants/', views.elephants_index, name='index'),
    path('elephants/<int:elephant_id>/', views.elephants_detail, name='detail'),
    path('elephants/create', views.ElephantCreate.as_view(), name='elephants_create'),
    path('elephants/<int:pk>/update', views.ElephantUpdate.as_view(), name='elephants_update'),
    path('elephants/<int:pk>/delete', views.ElephantDelete.as_view(), name='elephants_delete'),
]