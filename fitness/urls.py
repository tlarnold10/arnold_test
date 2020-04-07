from django.conf.urls import url, include
from rest_framework import routers
from .views import WeightList, WeightCreate, WeightDelete, WeightViewSet, WeightChart

router = routers.DefaultRouter()
router.register(r'chart', WeightViewSet)

urlpatterns = [
	url(r'^weight$',
		WeightList.as_view(),
		name='weight_list'),
	url(r'^weight/weight_create/$',
		WeightCreate.as_view(),
		name='weight_create'),
 	url(r'^weight/(?P<weight_date>[\w\-]+)/delete/$',
 		WeightDelete.as_view(),
 		name='weight_delete'),
    url(r'', include(router.urls)),
    url(r'chart', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^weight/chart/', WeightChart.as_view()),
]