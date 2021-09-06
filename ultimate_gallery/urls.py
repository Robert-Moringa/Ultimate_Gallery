from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns=[
    url('^$',views.landing,name = 'landing'),
    url(r'^home/',views.home,name = 'home'),
    url(r'^details/(?P<image_id>\d+)',views.photo_details,name ='photo_details'),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^search/', views.search_results, name='search_results')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)