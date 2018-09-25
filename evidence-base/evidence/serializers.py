from rest_framework import serializers
from django.db import models
from . models import Evidence
from django.db.models import Count, Avg, IntegerField, F

class EvidenceSerializers(serializers.ModelSerializer):

    class Meta:
        model = Evidence
        fields = 'evrating'
