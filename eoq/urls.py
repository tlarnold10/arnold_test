from django.conf.urls import url
from .views import upload_file

urlpatterns = [
	url(r'^$',
		upload_file,
		name='csv_upload'),
]