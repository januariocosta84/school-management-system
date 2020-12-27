from django.conf.urls import url
from django.urls import path
from . import views

app_name ='school_app'

urlpatterns=[
    #path('', views.index, name='index'),
    path('', views.SchoolListView.as_view(), name='list' ),
    path('<pk>', views.SchoolDetailView.as_view(), name='details')
]