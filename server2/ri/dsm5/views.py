from django.shortcuts import render

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import renderers
from rest_framework import parsers

from dsm5.serializers import AuthCustomTokenSerializer
from rest_framework.authtoken.models import Token


#class ObtainMongoAuthToken(APIView):
#    model = MongoToken

#    def post(self, request):
#        serializer = self.serializer_class(data=request.DATA)
#        if serializer.is_valid():
#            token, created = self.model.objects.get_or_create(user=serializer.object['user'])
#            return Response({'token': token.key})
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#obtain_mongo_auth_token = ObtainMongoAuthToken.as_view()


from dsm5.models import MongoToken, User

# Create your views here.

class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (
        parsers.FormParser,
        parsers.MultiPartParser,
        parsers.JSONParser,
    )

    renderer_classes = (renderers.JSONRenderer,)

    def get_or_create(self, attr):

        user = attr['user']
        token = MongoToken()
        
        if user is None:
            user = User()
            user.username = attr['email_or_username']
            user.password = attr['password']
            user.save()

            token.key = token.generate_key()
            token.user = user
            token.save()
        else :
            token = MongoToken.objects.get(user=user)

        return (token.key, token.created)


    def post(self, request):
        serializer = AuthCustomTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        attr = serializer.validated_data

        print(attr)

        #if user is None :
        #    token = Token.objects.create(user=user)
        #    print(token.key)

        #print(user)

        token, created = self.get_or_create(attr)

        print(token)

        content = {
        #    'token': unicode(token.key),
            'token': 'ttest',
        }

        return Response(content) 