from django.contrib.auth.models import User, Group
from rest_framework import serializers
from league.models import Competition, Team


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = ['id', 'name', 'code', 'area']


class TeamSerializer(serializers.ModelSerializer):
    competition = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Team
        fields = [
            'name',
            'tla',
            'shortName',
            'area',
            'email',
            'competition'
        ]