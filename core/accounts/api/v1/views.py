from rest_framework import generics,status
from rest_framework.response import Response
from .serializers import RegisterationSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
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



