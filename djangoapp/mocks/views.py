from textwrap import indent
from unittest import mock
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json

from .models import MockData
from .serializers import (
    MockDataSerializer, 
)

@api_view(['POST'])
def mock_post_request_view(request, *args, **kwargs):
    mock_data, created = MockData.objects.get_or_create(status='ok', request_data=request.data)
    if created:
        mock_data.message = f'MockData #{mock_data.id} created'
        mock_data.save()

    serializer = MockDataSerializer(mock_data)
    return Response(serializer.data)
