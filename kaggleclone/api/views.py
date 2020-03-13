from django.shortcuts import render
from .models import Publisher
from .serializers import PublisherSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework import status, viewsets

# Create your views here.

class PublishViewSet(viewsets.GenericViewSet):

	serializer_class = PublisherSerializer
	
	@action(methods=['get'], detail=False)
	def publisher_subscriber(self,request):
		serializer = PublisherSerializer(many=True)
		serialize_data = serializer.publisher_subscriber()
		return Response(serialize.data,status=200)
