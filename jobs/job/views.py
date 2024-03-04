from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .serializer import JobApplySerializer,JobSerializer
from .models import Job,JobApply
from.filters import JobFilter


class JobListCreateAPI(generics.ListCreateAPIView):
    queryset =  Job.objects.all()
    serializer_class =  JobSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_class = JobFilter

class JobDetailUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class =  JobSerializer







