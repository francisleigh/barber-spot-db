# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Business, Shop, Chair, TimeSlot
from .serializers import BusinessSerializer, ShopsSerializer, ChairsSerializer, TimeSlotsSerializer

import clr

def get_status(s):
  if s == 'UPDATED':
    return status.HTTP_202_ACCEPTED
  elif s == 'CREATED':
    return status.HTTP_201_CREATED
  elif s == 'DELETED':
    return status.HTTP_204_NO_CONTENT
  elif s == 'ERROR':
    return status.HTTP_400_BAD_REQUEST
  else:
    return status.HTTP_200_OK



class BusinessView(APIView):

  def get(self, request):
    b = Business.objects.all()
    serializer = BusinessSerializer(b, many=True)

    return Response(serializer.data)

# Shop
class ShopsView(APIView):

  def get(self, request):
    ss = Shop.objects.all()
    serializer = ShopsSerializer(ss, many=True)

    return Response(serializer.data)

  def post(self, request):
    serializer = ShopsSerializer(data=request.data)

    if serializer.is_valid():
      serializer.save()

      return Response(serializer.data, status=get_status('CREATED'))

    return Response(serializer.errors, status=get_status('ERROR'))

class ShopView(APIView):

  def get(self, request, shop_id):
    s = Shop.objects.filter(id=shop_id).first()
    serializer = ShopsSerializer(s)

    return Response(serializer.data)

  def put(self, request, shop_id):
    s = Shop.objects.filter(id=shop_id).first()
    serializer = ShopsSerializer(s, data=request.data)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=get_status('UPDATED'))

    return Response(serializer.errors, status=get_status('ERROR'))

  def delete(self, request, shop_id):
    shopToDelete = Shop.objects.filter(id=shop_id).first()
    shopToDelete.delete()

    return Response(status=get_status('DELETED'))

# Chair
class ChairsView(APIView):

  def get(self, request, shop_id=False):
    if shop_id is False:
      cs = Chair.objects.all()
    else:
      cs = Chair.objects.filter(shop_id=shop_id)

    serializer = ChairsSerializer(cs, many=True)

    return Response(serializer.data)

  def post(self, request, shop_id=False):
    serializer = ChairsSerializer(data=request.data)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=get_status('CREATED'))

    return Response(serializer.errors, status=get_status('ERROR'))

class ChairView(APIView):
  def get(self, request, shop_id=False, chair_id=False):
    if chair_id and shop_id:
      c = Chair.objects.filter(shop_id=shop_id, id=chair_id).first()
    elif chair_id and shop_id is False:
      c = Chair.objects.filter(id=chair_id).first()

    serializer = ChairsSerializer(c)

    return Response(serializer.data)

  def put(self, request, shop_id=False, chair_id=False):
    editedData = request.data
    chairToEdit = Chair.objects.filter(id=chair_id).first()
    serializer = ChairsSerializer(chairToEdit, data=editedData)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=get_status('UPDATED'))

    return Response(serializer.errors, status=get_status('ERROR'))

  def delete(self, request, shop_id=False, chair_id=False):
    chairToDelete = Chair.objects.filter(id=chair_id).first()
    chairToDelete.delete()

    return Response(status=get_status('DELETED'))

class TimeSlotsView(APIView):
  def get(self, request, chair_id=False):
    if chair_id is False:
      tss = TimeSlot.objects.all()
    else:
      tss = TimeSlot.objects.filter(chair_id=chair_id)

    serializer = TimeSlotsSerializer(tss, many=True)

    return Response(serializer.data)

class TimeSlotView(APIView):
  def get(self, request, slot_id):
    ts = TimeSlot.objects.filter(id=slot_id).first()
    serializer = TimeSlotsSerializer(ts, context={'show_chair': True})

    return Response(serializer.data)

  def put(self, request, slot_id):
    editedData = request.data
    slotToEdit = TimeSlot.filter(id=slot_id).first()
    serializer = TimeSlotsSerializer(slotToEdit, data=editedData)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=get_status('UPDATED'))

    return Response(serializer.errors, status=get_status('ERROR'))

  def delete(self, request, slot_id):
    slotToDelete = TimeSlot.objects.filter(id=slot_id).first()
    slotToDelete.delete()

    return Response(status=get_status('DELETED'))

  def post(self, request, chair_id):
    serializer = TimeSlotsSerializer(data=request.data)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=get_status('CREATED'))

    return Response(serializer.errors, status=get_status('ERROR'))
