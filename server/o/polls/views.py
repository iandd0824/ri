from django.shortcuts import render
from rest_framework import generics
#from rest_framework_mongoengine import generics

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


# Create your views here.
from polls.models import Poll, Choice, Lady, User
from polls.serializers import LadySerializer, UserSerializer

#poll = Poll.objects(question__contains="What").first()
#choice = Choice(choice_text="I'm at DjangoCon.fi", votes=23)
#poll.choices.append(choice)
#poll.save()

#ross = Lady(firstname='Danny', lastname='Ross').save()

#print poll.question

#user = authenticate(username=username, password=password)
#assert isinstance(user, mongoengine.django.auth.User)

#class LadyList(generics.ListCreateAPIView):

#    serializer_class = LadySerializer

#    def get_queryset(self):
#        return Lady.objects


# Tutorial 1

#class JSONResponse(HttpResponse):

#	def __init__(self, data, **kwargs):
#		content = JSONRenderer().render(data)
#		kwargs['content_type'] = 'application/json'
#		super(JSONResponse, self).__init__(content, **kwargs)

#@csrf_exempt
#def snippet_list(request):
#    """
#    List all code snippets, or create a new snippet.
#    """
#    if request.method == 'GET':
#        ladys = Lady.objects.all()
#        serializer = LadySerializer(ladys, many=True)
#        return JSONResponse(serializer.data)

#    elif request.method == 'POST':
#        data = JSONParser().parse(request)
#        serializer = LadySerializer(data=data)
#        if serializer.is_valid():
#            serializer.save()
#            return JSONResponse(serializer.data, status=201)
#        return JSONResponse(serializer.errors, status=400)


# @csrf_exempt
# def snippet_detail(request, pk):
# 	"""
# 	Retrieve, update or delete a code snippet.
# 	"""
# 	try:
# 		lady = Lady.objects.get(pk=pk)
# 	except Lady.DoesNotExist:
# 		return HttpResponse(status=404)

# 	if request.method == 'GET':
# 		serializer = LadySerializer(lady)
# 		return JSONResponse(serializer.data)

# 	elif request.method == 'PUT':
# 		data = JSONParser().parse(request)
# 		serializer = LadySerializer(lady, data=data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return JSONResponse(serializer.data)
# 		return JSONResponse(serializer.errors, status=400)

# 	elif request.method == 'DELETE':
# 		lady.delete()
# 		return HttpResponse(status=204)

# Tutorial 2

# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# @api_view(['GET', 'POST'])
# def snippet_list(request, format=None):
# 	"""
# 	List all snippets, or create a new snippet.
# 	"""
# 	if request.method == 'GET':
# 		ladys = Lady.objects.all()
# 		serializer = LadySerializer(ladys, many=True)
# 		return Response(serializer.data)

# 	elif request.method == 'POST':
# 		serializer = LadySerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, pk, format=None):
# 	"""
# 	Retrieve, update or delete a snippet instance.
# 	"""
# 	try:
# 		lady = Lady.objects.get(pk=pk)
# 	except Lady.DoesNotExist:
# 		return Response(status=status.HTTP_404_NOT_FOUND)

# 	if request.method == 'GET':
# 		serializer = LadySerializer(lady)
# 		return Response(serializer.data)

# 	elif request.method == 'PUT':
# 		serializer = LadySerializer(lady, data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 	elif request.method == 'DELETE':
# 		lady.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)

# Tutorial 3

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Permission

from rest_framework import permissions

class UserList(APIView):
	"""
	List all snippets, or create a new snippet.
	"""
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

class SnippetList(APIView):
	"""
	List all snippets, or create a new snippet.
	"""
	def get(self, request, format=None):
		ladys = Lady.objects.all()
		serializer = LadySerializer(ladys, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = LadySerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	permission_classes = (permissions.IsAuthenticated,)

class SnippetDetail(APIView):
	"""
	Retrieve, update or delete a snippet instance.
	"""
	def get_object(self, pk):
		try:
			return Lady.objects.get(pk=pk)
		except Lady.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		lady = self.get_object(pk)
		serializer = LadySerializer(lady)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		lady = self.get_object(pk)
		serializer = LadySerializer(lady, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		lady = self.get_object(pk)
		lady.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

# Tutorial 3.1 Using mixins

# from rest_framework import mixins
# from rest_framework import generics

# class SnippetList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
# 	queryset = Lady.objects.all()
# 	serializer_class = LadySerializer

# 	def get(self, request, *args, **kwargs):
# 		return self.list(request, *args, **kwargs)

# 	def post(self, request, *args, **kwargs):
# 		return self.create(request, *args, **kwargs)

# class SnippetDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
# 	queryset = Lady.objects.all()
# 	serializer_class = LadySerializer

# 	def get(self, request, *args, **kwargs):
# 		return self.retrieve(request, *args, **kwargs)

# 	def put(self, request, *args, **kwargs):
# 		return self.update(request, *args, **kwargs)

# 	def delete(self, request, *args, **kwargs):
# 		return self.destroy(request, *args, **kwargs)

# Tutorial 3.2 Using generic class based views

# from rest_framework import generics

# class SnippetList(generics.ListCreateAPIView):
# 	queryset = Lady.objects.all()
# 	serializer_class = LadySerializer


# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
# 	queryset = Lady.objects.all()
# 	serializer_class = LadySerializer

# Mongoengine example
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect

def home(request):
    """Home view, displays login mechanism"""
    if request.user.is_authenticated():
        return redirect('done')
    return render_to_response('home.html', {}, RequestContext(request))


@login_required
def done(request):
    """Login complete view, displays user data"""
    return render_to_response('done.html', {'user': request.user},
                              RequestContext(request))


def signup_email(request):
    return render_to_response('email_signup.html', {}, RequestContext(request))


def validation_sent(request):
    return render_to_response('validation_sent.html', {
        'email': request.session.get('email_validation_address')
    }, RequestContext(request))


def require_email(request):
    if request.method == 'POST':
        request.session['saved_email'] = request.POST.get('email')
        backend = request.session['partial_pipeline']['backend']
        return redirect('social:complete', backend=backend)
    return render_to_response('email.html', RequestContext(request))