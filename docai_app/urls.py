from django.urls import path
from . import views


app_name = 'docai_app'

urlpatterns = [
    path('', views.DocumentListView.as_view(),name='list'),
]