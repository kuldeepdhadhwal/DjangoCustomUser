from rest_framework import serializers

from .models import Publisher


class PublisherSerializer(serializers.Serializer):
	

	def publisher_subscriber(self):
		data = Subscriber.objects.all()
		return data

	class Meta:
		model = Publisher
		fields = '__all__'