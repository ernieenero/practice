from django.conf.urls import url
from . import views

# template for URLs
app_name = 'lvl_app'


urlpatterns = [
    url(r'^register/$', views.register, name='registration'),
    url(r'^login/$', views.user_login, name='login')
]
