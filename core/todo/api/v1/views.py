from .serializers import Todoserializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from todo.models import Task

class TodoListModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class=Todoserializer
    model=Task
    
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)
