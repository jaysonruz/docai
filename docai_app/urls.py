from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'docai_app'

urlpatterns = [
    path('', views.DocumentListView.as_view(),name='list'),
    path('create/',views.DocumentCreateView.as_view(),name='create'),
    url(r'^(?P<pk>\d+)/$',views.DocumentDetailView.as_view(),name='detail'),
    url(r'^update/(?P<pk>\d+)/$',views.DocumentDetailView.as_view(),name='update'),
]