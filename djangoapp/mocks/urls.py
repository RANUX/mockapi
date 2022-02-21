from django.urls import path
from .views import *

urlpatterns = [
    path('buttons/<int:pk>/', MockDataView.as_view()),
]
