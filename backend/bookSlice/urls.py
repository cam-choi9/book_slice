from django.urls import path
from .views import *

urlpatterns = [
    path('', main),
    path('home', main, name="home"),
    path('upload', upload, name='upload_image'),
    path('view', view, name='view_image'),
]