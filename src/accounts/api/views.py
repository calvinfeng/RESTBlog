from django.db.models import Q
from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin

from rest_framework.views import APIView
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
    )

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from .serializers import UserCreateSerializer, UserLoginSerializer

User = get_user_model()

class UserCreateAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()

class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serialized_data = UserLoginSerializer(data=data)
        if serialized_data.is_valid(raise_exception=True):
            new_data = serialized_data.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
