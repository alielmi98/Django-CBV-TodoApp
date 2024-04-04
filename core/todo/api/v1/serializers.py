from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from todo.models import Task


class Todoserializer(serializers.ModelSerializer):
    absolute_url=serializers.SerializerMethodField()
    class Meta:
        model=Task
        fields=['id','user','title','complete','absolute_url','created_date','updated_date']

    def get_absolute_url(self,obj):
        request=self.context.get('request')
        return request.build_absolute_uri(obj.pk)
                

        



            