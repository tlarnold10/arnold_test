from django.conf.urls import url
from .views import upload_file

urlpatterns = [
	url(r'^$',
		upload_file,
		name='csv_upload'),
# 	url(r'^api/sales_chart', 
# 		sales_chart, 
# 		name='sales_chart')
]