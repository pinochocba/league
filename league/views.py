from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from league.serializers import UserSerializer, GroupSerializer, CompetitionSerializer
from league.models import Competition

import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CompetitionDetail(APIView):
    """
    List all competitions
    """

    def get(self, request, code, format=None):
        apikey = '4cb19628e52a4a3992ba1271e70ed174'
        headers = {'X-Auth-Token': apikey}
        BASE_URL = 'http://api.football-data.org/v2/'
        try:
            competition = Competition.objects.get(code=code)
            serializer = CompetitionSerializer(competition)
            return Response(serializer.data)
        except Competition.DoesNotExist:
            url = 'competitions/{code}'.format(code=code)
            req = requests.get(BASE_URL + url, headers=headers)
            data = req.json()
            serializer = CompetitionSerializer(data=data)
            #print(serializer.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
