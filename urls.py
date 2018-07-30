from django.conf.urls import url
from webapp import views


urlpatterns = [
    url(r'^streak/(?P<student_id>[A-Za-z0-9_.-]+)/$', views.streak.as_view(), name='streak'),
]
