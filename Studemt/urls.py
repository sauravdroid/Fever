from django.conf.urls import url
from . import views

app_name = 'student'

urlpatterns = [
    url(r'^register$', views.register, name='index'),
    url(r'^application$', views.application, name='application'),
    url(r'^login$', views.user_login, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^$', views.student_list, name='student_list')
]
