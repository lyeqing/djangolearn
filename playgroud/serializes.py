from rest_framework import serializers
from playgroud.modelss import Activities, Persons

class PersonSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Persons
		fields = '__all__'
class ActivitySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Activities
		fields = '__all__'