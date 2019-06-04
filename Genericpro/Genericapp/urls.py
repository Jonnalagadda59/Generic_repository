from django.conf.urls import url
from Genericapp import views


urlpatterns =[
    url(r'^data/$',views.Genericview_List.as_view()),
    url(r'^data/(?P<pk>[0-9]+)/$', views.Genericview_Details.as_view()),
]