
# from rest_framework import viewsets
from rest_framework import generics

from users.models import User
from users.serializers import UserSerializer


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#

# class UserUpdateView(generics.UpdateAPIView):
#     queryset = queryset = User.objects.all()
#     serializer_class = UserSerializer

