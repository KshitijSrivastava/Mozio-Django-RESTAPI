from django.contrib import admin
from django.urls import path, include
from mozio.views import index, ProviderDetail, ProviderList, GeoPolygonDetail, GeoPolygonList, query

urlpatterns = [
    path('', index),
    path('new_provider/', ProviderList.as_view()),
    path('provider/<int:pk>/', ProviderDetail.as_view()),
    path('new_polygon/', GeoPolygonList.as_view()),
    path('polygon/<int:pk>/', GeoPolygonDetail.as_view()),
    path('query/', query),
]
