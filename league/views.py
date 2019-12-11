from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from league.serializers import UserSerializer, GroupSerializer, \
    CompetitionSerializer, TeamSerializer
from league.models import Competition

import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CompetitionDetail(APIView):
    """
    List all competitions
    """
    _api_key = '4cb19628e52a4a3992ba1271e70ed174'
    _headers = {'X-Auth-Token': _api_key}
    _base_url = 'http://api.football-data.org/v2/'
    _messages = {
        status.HTTP_201_CREATED: "Successfully imported",
        status.HTTP_400_BAD_REQUEST: "Bad request",
        status.HTTP_404_NOT_FOUND: "Not found",
        status.HTTP_409_CONFLICT: "League already imported",
        status.HTTP_504_GATEWAY_TIMEOUT: "Server Error",
    }

    def get_competition(self, url):
        req = requests.get(self._base_url + url, headers=self._headers)
        if req.status_code == requests.codes.ok:
            data = req.json()
            data['area'] = data['area']['name']
            serializer = CompetitionSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                response = status.HTTP_201_CREATED
            else:
                response = status.HTTP_400_BAD_REQUEST
        elif req.status_code == 404:
             response = status.HTTP_404_NOT_FOUND
        else:
            response =  status.HTTP_504_GATEWAY_TIMEOUT
        return response
    
    def get_teams(self, url):
        req = requests.get(self._base_url + url, headers=self._headers)
        if req.status_code == requests.codes.ok:
            data = req.json()
            for team in data['teams']:
                team['area'] = team['area']['name']
                team['competition'] = data['competition']['id']
                print(team)
                serializer = TeamSerializer(data=team)
                if serializer.is_valid():
                    serializer.save()
                    response = status.HTTP_201_CREATED
                else:
                    response = status.HTTP_400_BAD_REQUEST
        elif req.status_code == 404:
             response = status.HTTP_404_NOT_FOUND
        else:
            response =  status.HTTP_504_GATEWAY_TIMEOUT
        return response
    
    def get(self, request, code, format=None):
        try:
            competition = Competition.objects.get(code=code)
            serializer = CompetitionSerializer(competition)
            return Response(serializer.data, status=status.HTTP_409_CONFLICT)
        except Competition.DoesNotExist:
            response = self.get_competition('competitions/{code}'.format(code=code))
            if response == status.HTTP_201_CREATED:
                response = self.get_teams('competitions/{code}/teams'.format(code=code))
            return Response({'message': self._messages[response]}, status=response)

    def get_object(self, code):
        try:
            return Competition.objects.get(code=code)
        except Competition.DoesNotExist:
            raise Http404

    def delete(self, request, code, format=None):
        print(code)
        competition = self.get_object(code)
        competition.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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
