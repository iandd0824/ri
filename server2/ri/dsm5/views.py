from django.shortcuts import render

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import renderers
from rest_framework import parsers

from dsm5.serializers import AuthCustomTokenSerializer, UserSerializer
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

        print('get')
        print(user)
        
        if user == None:
            print('none')
            user = User()
            user.username = attr['email_or_username']
            user.set_password(attr['password'])
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
            'token': token,
        }

        return Response(content) 

from rest_framework.authentication import TokenAuthentication
from dsm5.authentication import MongoTokenAuthentication
from rest_framework.permissions import IsAuthenticated

class UserList(APIView):
    """
    List all users, or create a new user.
    Authentication is needed for this methods
    """
    authentication_classes = (MongoTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
