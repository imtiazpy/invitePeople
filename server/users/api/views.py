from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.shortcuts import redirect
import requests
from .serializers import UserActivationSerializer


class UserActivationView(generics.GenericAPIView):
    
    permission_classes =[AllowAny]

    serializer_class = UserActivationSerializer

    def get(self, request, uid, token, format=None):
        payload = {'uid': uid, 'token': token}

        url = 'http://127.0.0.1:8000/api/v1/auth/users/activation/'

        requests.post(url, data=payload)

        return redirect('http://127.0.0.1:8000/admin/')

