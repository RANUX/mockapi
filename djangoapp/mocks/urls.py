from django.urls import path
from .views import *

urlpatterns = [
    path('request/', mock_post_request_view)
]
