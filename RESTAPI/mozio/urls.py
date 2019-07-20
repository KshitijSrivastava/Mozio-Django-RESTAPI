from django.contrib import admin
from django.urls import path, include
from mozio.views import index, ProviderDetail, ProviderList

urlpatterns = [
    path('', index),
    path('new_provider/', ProviderList.as_view()),
    path('provider/<int:pk>/', ProviderDetail.as_view()),
]
