from rest_framework import generics

from .models import MockData
from .serializers import MockDataSerializer


class MockDataView(generics.RetrieveAPIView):
    serializer_class = MockDataSerializer
    queryset = MockData.objects.all()