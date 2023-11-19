from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
     path("",views.index),
     path('ingest/', views.ingest_log, name='ingest_log'),
     path('logs/', views.LogList.as_view(), name='log-list'),
     path('logs/<int:pk>/', views.LogDetail.as_view(), name='log-detail'),

]
