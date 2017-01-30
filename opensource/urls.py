from django.conf.urls import url
import views

urlpatterns = [
    url(r'^hello$' , views.hello),
    url(r'^(?P<id>[0-9]+)/details$', views.details),
    url(r'^all$' , views.showAllStudents),
]
