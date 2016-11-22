from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import list_route
from django.db.models import Q
from django.contrib.auth.models import User

from .serializers import TaskSerializer, UserSerializer, UserRegistrationSerializer, UserLoginSerializer
from .models import Task


class UserSignup(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()

    @list_route(methods=['post'])
    def register(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_serializer = UserSerializer(data=serializer.data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        Token.objects.create(user=user)
        return Response(user_serializer.data)


class UserLogin(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()

    @list_route(methods=['post'])
    def verify(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(username=serializer.data['username'])
        token = Token.objects.get(user=user)
        return Response({'user_id': user.pk, 'username': user.username, 'token': token.key})


class RetrieveUpdateUserAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(pk=self.kwargs['pk'])


class ListCreateTasksAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer

    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.pk
        return super().create(request, *args, **kwargs)

    def get_queryset(self):
        return Task.objects.filter(user=self.kwargs['pk'])


class RetrieveUpdateDestroyTaskAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(Q(user=self.kwargs['user']) & Q(pk=self.kwargs['pk']))


class TaskSearch(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer
    lookup_field = 'name'

    def get_queryset(self):
        queryset = Task.objects.all()
        name = self.request.query_params.get('name', None)
        date = self.request.query_params.get('date', None)
        if name is not None:
            queryset = queryset.filter(Q(name__contains=name) & Q(user=self.request.user.pk))
        elif date is not None:
            queryset = queryset.filter(Q(due_date__contains=date) & Q(user=self.request.user.pk))
        else:
            queryset = queryset.filter(Q(name__contains=name) & Q(due_date__contains=date) & Q(user=self.request.user.pk))
        return queryset


class TaskSearchDate(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer
    lookup_field = 'due_date'

    def get_queryset(self):
        queryset = Task.objects.all()
        date = self.request.query_params.get('date', None)
        if date is not None:
            queryset = queryset.filter(Q(due_date__contains=date) & Q(user=self.request.user.pk))
        return queryset


class TaskSearchBoth(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.all()
        name = self.request.query_params.get('name', None)
        date = self.request.query_params.get('date', None)
        if name and date is not None:
            queryset = queryset.filter(Q(name__contains=name) & Q(due_date__contains=date) & Q(user=self.request.user.pk))
        return queryset

