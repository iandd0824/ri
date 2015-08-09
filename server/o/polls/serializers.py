from rest_framework import serializers
from mongoengine import *
from polls.models import Lady, User
from django.forms import widgets

#class LadySerializer(serializers.Serializer):

#    firstname = serializers.CharField(max_length=50)
#    lastname = serializers.CharField(max_length=50)

#    def restore_object(self,attrs,instance=None):
#        if instance:
#            instance.firstname = attrs.get('firstname', instance.firstname)
#            instance.lastname = attrs.get('lastname', instance.lastname)
#            return instance
#        return Lady(**attrs)


# from rest_framework_mongoengine.serializers import DocumentSerializer

# class LadySerializer(DocumentSerializer):
# 	class Meta:
# 		model = Lady
# 		depth = 1

class LadySerializer(serializers.Serializer):
	pk = serializers.CharField(read_only=True)
	firstname = serializers.CharField(max_length=50)
	lastname = serializers.CharField(max_length=50)

	def create(self, validated_data):
		return Lady.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.firstname = validated_data.get('firstname', instance.firstname)
		instance.lastname = validated_data.get('lastname', instance.lastname)
		instance.save()
		return instance

#class LadySerializer(serializers.ModelSerializer):
#	class Meta:
#		model = Lady
#		fields = ('firstname', 'lastname')


# Toturial 4 

# from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):
	pk = serializers.CharField(read_only=True)
	username = serializers.CharField(max_length=50)
	email = serializers.CharField(max_length=150)



	