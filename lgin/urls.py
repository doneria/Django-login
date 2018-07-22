from django.conf.urls import url,include
from lgin import views as lgin_views
from register import views as register_views
urlpatterns = [

url(r'^login/$',lgin_views.login_form, name='log'),
url(r'^register$',register_views.register_form, name='reg'),
]