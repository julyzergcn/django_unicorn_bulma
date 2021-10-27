from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('load-more', views.load_more, name='load_more'),
    path('users/<int:user_id>/delete/', views.delete_user, name='delete_user'),
]
