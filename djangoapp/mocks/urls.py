from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/scanner/scanned_code.php/', mock_post_request_view)
]
