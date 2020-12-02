from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/done', views.done, name='done'),
    path('<int:id>/delete', views.delete, name='delete'),
]
