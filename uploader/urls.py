from django.urls import path
from . import views


urlpatterns = [
    path('upload/', views.UploadFileView.as_view(), name='upload'),
    path('', views.TransactionListView.as_view(), name='list'),
]
