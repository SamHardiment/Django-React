from django.shortcuts import render
from .models import Lead
from .serializers import LeadSerializer
from rest_framework import generics
# Create your views here.
# adoption/views.py

def home(req):
    # context = { 'contacts': Lead.Objects.all()}
    return render(req, 'leads/index.html')

def about(req):
    return render(req, 'leads/about.html')

class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
