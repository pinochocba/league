from django.contrib.auth.models import User, Group
from rest_framework import serializers
from league.models import Competition

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class AreaSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)

class CompetitionSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    code = serializers.CharField(max_length=3)
    area = AreaSerializer()

    class Meta:
        model = Competition
        fields = ['name', 'code', 'area']

    def create(self, validated_data):
        """
        Create and return a new `Competition` instance, given the validated data.
        """
        return Competition.objects.create(**validated_data)