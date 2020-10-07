from django.conf.urls import url

from .views import EmotionList, EmotionCreate, VerseCreate, VerseDetail, VerseList, VerseUpdate, VerseDelete

urlpatterns = [
	url(r'^$',
		EmotionList.as_view(),
		name='emotion_list'),
	url(r'^create/$',
		EmotionCreate.as_view(),
		name='emotion_create'),
	url(r'^verse/create$',
		VerseCreate.as_view(),
		name='verse_create'),
	url(r'^verse/(?P<slug>[\w\-]+)/$',
		VerseDetail.as_view(),
		name='verse_detail'),
 	url(r'^(?P<emotion>[\w\-]+)/$',
 		VerseList.as_view(),
 		name='verse_list'),
 	url(r'^verse/(?P<slug>[\w\-]+)/update/$',
 		VerseUpdate.as_view(),
 		name='verse_update'),
 	url(r'^verse/(?P<slug>[\w\-]+)/delete/$',
 		VerseDelete.as_view(),
 		name='verse_delete'),
]