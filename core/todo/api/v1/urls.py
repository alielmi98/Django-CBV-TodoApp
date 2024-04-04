from rest_framework.routers import DefaultRouter 
from . import views
app_name="api-v1"

router=DefaultRouter()
router.register('task',views.TodoListModelViewSet,basename='task')
urlpatterns=router.urls