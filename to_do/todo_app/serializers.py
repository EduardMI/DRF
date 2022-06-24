from rest_framework.serializers import ModelSerializer, StringRelatedField

from .models import Project, ToDo
from user_app.serializers import UserModelSerializer


class ProjectModelSerializer(ModelSerializer):

    users = StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = '__all__'


class ToDoModelSerializer(ModelSerializer):

    project = ProjectModelSerializer()
    author = UserModelSerializer()

    class Meta:
        model = ToDo
        # exclude = ['is_active']
        fields = '__all__'
