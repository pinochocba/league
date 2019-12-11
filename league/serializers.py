from django.contrib.auth.models import User, Group
from rest_framework import serializers
from league.models import Competition, Team, Player


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
    class Meta:
        model = Team
        fields = [
            'id',
            'name',
            'tla',
            'shortName',
            'area',
            'email',
            'code'
        ]

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = [
            'name',
            'position',
            'dateOfBirth',
            'countryOfBirth',
            'nationality',
            'team_id',
        ]