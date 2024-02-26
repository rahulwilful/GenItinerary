from rest_framework import serializers
from api.models import User, Department

class UserSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.ReadOnlyField()
    class Meta:
        model = User
        fields = "__all__"


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    dept_id = serializers.ReadOnlyField()
    class Meta:
        model = Department
        fields = "__all__"