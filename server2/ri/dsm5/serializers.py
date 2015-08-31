from rest_framework import serializers
from mongoengine import *
from dsm5.models import User
from django.contrib.auth import authenticate


#Obtain auth token using email instead username
class AuthCustomTokenSerializer(serializers.Serializer):
	
    email_or_username = serializers.CharField()
    password = serializers.CharField()

    def validateEmail(self,email):
	    from django.core.validators import validate_email
	    from django.core.exceptions import ValidationError
	    try:
	        validate_email( email )
	        return True
	    except ValidationError:
	        return False

    def get_object_or_404(self, klass, *args, **kwargs):
	    try:
	        return klass.objects.get(*args, **kwargs)
	    except klass.DoesNotExist:
	        raise Http404


    def validate(self, attrs):
        email_or_username = attrs.get('email_or_username')
        password = attrs.get('password')

        if email_or_username and password:
            # Check if user sent email
            if self.validateEmail(email_or_username):
                user_request = self.get_object_or_404(User,email=email_or_username)

                email_or_username = user_request.username

            user = authenticate(username=email_or_username, password=password)

            print(user)

	        #if user:
	            #if not user.is_active:
	                #msg = _('User account is disabled.')
	                #raise exceptions.ValidationError(msg)
	        #else:
	            #msg = _('Unable to log in with provided credentials.')
	            #raise exceptions.ValidationError(msg)
	    #else:
	        #msg = _('Must include "email or username" and "password"')
	        #raise exceptions.ValidationError(msg)

        attrs['user'] = user
        return attrs