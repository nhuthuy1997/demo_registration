from django.conf.urls import url
from first_app import views

# SET THE NAMESPACE!
app_name = 'first_app'

urlpatterns=[
    url(r'^register/$', views.register,name='register'),
    url(r'^user_login/$', views.user_login,name='user_login'),
]
