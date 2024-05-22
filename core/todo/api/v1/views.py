from .serializers import Todoserializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from todo.models import Task
from .paginations import DefaultPagination
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
import requests
class GetWeather(APIView):
    @method_decorator(cache_page(20*60))
    def get(self,request):
        response=requests.get("https://api.openweathermap.org/data/2.5/weather?q=tehran&appid=7f5ad6244b2dffe8f996094746afa1fe")
        response=response.json()
        return Response(response)





class TodoListModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = Todoserializer
    pagination_class = DefaultPagination
    model = Task

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)
