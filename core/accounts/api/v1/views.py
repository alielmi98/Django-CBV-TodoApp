from rest_framework import generics,status
from rest_framework.response import Response
from .serializers import RegisterationSerializer,ChangePasswordSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
class RgistrationApiView(generics.GenericAPIView):
    serializer_class=RegisterationSerializer
    
    def post(self,request,*args,**kwargs):
        serializer=RegisterationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data={
                'message' : serializer.validated_data['username'] + ' created successfully'
            }

            return Response(data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)


class CustomDiscardAuthToken(APIView):
        permission_classes = [IsAuthenticated]
        def post(self,request):
            request.user.auth_token.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class ChangePasswordApiView(generics.GenericAPIView):
    model = User
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response(
                    {"old_password": ["Wrong password."]},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response(
                {"details": "password changed successfully"},
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


