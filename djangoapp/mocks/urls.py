from django.urls import path
from .views import *

urlpatterns = [
    path('qr/', mock_post_view),
    path('action/', mock_post_view)
]
