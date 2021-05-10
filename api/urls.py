
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import EntryViewSet, ParticipantViewSet, EntryYesViewSet, EntryNoViewSet, ResultViewSet, SurveyViewSet

router = routers.DefaultRouter()
router.register('entry', EntryViewSet)
router.register('entry-yes', EntryYesViewSet)
router.register('entry-no', EntryNoViewSet)
router.register('participant', ParticipantViewSet)
router.register('result', ResultViewSet)
router.register('survey', SurveyViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
