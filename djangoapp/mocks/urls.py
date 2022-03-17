from django.urls import path
from .views import *

urlpatterns = [
    path('scanner/scanned_code.php', mock_post_request_view)
]
