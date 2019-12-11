from django.urls import path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from league import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('import-league/<str:code>', views.CompetitionDetail.as_view()),
    path('total-players/<str:code>', views.TotalPlayers.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)