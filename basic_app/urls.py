from django.conf.urls import url
from basic_app import views


app_name = 'basic_app'

urlpatterns =[
    url(r'^$', views.SchoolListView.as_view(), name="list"),
    url(r'^(?P<pk>\d+)/$', views.SchoolDetailView.as_view(), name="detail"),
    url(r'^create/$', views.SchoolCreateView.as_view(), name="create"),
    url(r'^update/(?P<pk>\d+)/$', views.SchoolUpdateView.as_view(), name="update"),
    url(r'^delete/(?P<pk>\d+)/$', views.SchoolDeleteView.as_view(), name="delete"),

    url(r'^student_list/', views.StudentListView.as_view(), name="student_list"),
    url(r'^student/(?P<pk>\d+)/$', views.StudentDetailView.as_view(), name="student_detail"),
    url(r'^student_create/$', views.StudentCreateView.as_view(), name="student_create"),
    url(r'^student_update/(?P<pk>\d+)/$', views.StudentUpdateView.as_view(), name="student_update"),
    url(r'^student_delete/(?P<pk>\d+)/$', views.StudentDeleteView.as_view(), name="student_delete"),
]