from django.urls import path
from .views import *

urlpatterns = [
    path('buttons/<int:pk>/', MockDataView.as_view()),
    path('form/<int:pk>/', MockDataView.as_view()),
]
