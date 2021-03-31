from django.urls import path
app_name='app'
from app import views
urlpatterns=[
    path('him/',views.hai,name='him'),
    path('singh/',views.hello,name='singh'),
    path('singh1/',views.htmlfile,name='singh1'),
]
