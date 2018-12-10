from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from first_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.index, name='index'),
    url(r'^special/', views.special,name='special'),
    url(r'^first_app/', include('first_app.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
]
