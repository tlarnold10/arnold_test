from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from .views import JavaScript, HomeView, BookViewSet

router = routers.DefaultRouter()
router.register(r'apitest', BookViewSet)

urlpatterns = [
    url(r'^api/chart/data/$', JavaScript.as_view()),
    url(r'^data/', HomeView.as_view()),
    url(r'', include(router.urls)),
    url(r'apitest', include('rest_framework.urls', namespace='rest_framework'))
]