from django.urls import path
from basic_app import views

#  Template Tagging

app_name='basic_app'

urlpatterns=[
    path('relative_urls/',views.relative_urls,name='relative_urls'),
    path('other/',views.other,name='other'),
]
