from rest_framework import serializers
from .models import Business, Shop, Chair, TimeSlot

import clr

class TimeSlotsSerializer(serializers.ModelSerializer):
  class Meta:
    model = TimeSlot

    fields = ('start', 'end', 'id')
class ChairsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Chair

    fields = ('day_rate', 'id')

class ShopsSerializer(serializers.ModelSerializer):
  # chairs = ChairsSerializer()
  class Meta:
    model = Shop

    fields = '__all__'

class BusinessSerializer(serializers.ModelSerializer):
  shops = ShopsSerializer()
  class Meta:
    model = Business

    fields = '__all__'
