from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.home,name = 'welcome'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^profil/(\d+)', views.profil, name='profil'),
    url(r'^image/', views.image, name='image'),
    url(r'^comments/', views.comments, name='comments'),
    url(r'^images/(\d+)',views.images,name ='images'),
    url(r'^description/(\d+)',views.description,name ='description')

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
