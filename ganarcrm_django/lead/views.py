from django.shortcuts import render

from rest_framework import viewsets


from .models import Lead
from .serializers import LeadSerializer


class LeadViewSet(viewsets.ModelViewSet):
    # todo: create serializers (video is on 1:11:57 minute)
    pass