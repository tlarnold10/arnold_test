from django.conf.urls import url
from .views import WeightList, WeightCreate
urlpatterns = [
	url(r'^$',
		WeightList.as_view(),
		name='weight_list'),
	url(r'^weight_create/$',
		WeightCreate.as_view(),
		name='weight_create'),
]