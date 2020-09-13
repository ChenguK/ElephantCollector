from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('elephants/', views.elephants_index, name='index'),
    path('elephants/<int:elephant_id>/', views.elephants_detail, name='detail'),
    path('elephants/<int:elephant_id>/add_care/', views.add_care, name='add_care'),
    path('elephants/<int:elephant_id>/add_photo/', views.add_photo, name='add_photo'),
    path('elephants/<int:elephant_id>/assoc_trainer/<int:trainer_id>', views.assoc_trainer, name='assoc_trainer'),
    path('elephants/<int:elephant_id>/unassoc_trainer/<int:trainer_id>', views.unassoc_trainer, name='unassoc_trainer'),
    path('elephants/create/', views.ElephantCreate.as_view(), name='elephants_create'),
    path('elephants/<int:pk>/update/', views.ElephantUpdate.as_view(), name='elephants_update'),
    path('elephants/<int:pk>/delete/', views.ElephantDelete.as_view(), name='elephants_delete'),
    path('trainers/', views.trainers_index, name='trainers_index'),
    path('trainers/<int:trainer_id>/', views.trainers_detail, name='trainers_detail'),
    path('trainers/create/', views.TrainerCreate.as_view(), name='trainers_create'),
    path('trainers/<int:pk>/update/', views.TrainerUpdate.as_view(), name='trainers_update'),
    path('trainers/<int:pk>/delete/', views.TrainerDelete.as_view(), name='trainers_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)