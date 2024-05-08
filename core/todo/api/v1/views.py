from .serializers import Todoserializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from todo.models import Task
from .paginations import DefaultPagination
from .permissions import IsOwnerOrReadOnly


# Example for ViewSet in CBV
class TodoListModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = Todoserializer
    pagination_class = DefaultPagination
    model = Task

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)
