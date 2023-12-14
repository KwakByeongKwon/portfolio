from django.urls import path

from . import views

app_name = 'cafe'

urlpatterns = [
    path('',views.index,name='index'),
    path('detail/',views.detail,name='detail'),
    path('preview/<int:id>/',views.preview,name='preview'),
    path('seoul/',views.seoul,name='seoul'),
    
]

