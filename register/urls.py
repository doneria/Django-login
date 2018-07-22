from django.conf.urls import url
from register import views as register_views
from lgin import views as login_views

urlpatterns = [

url(r'^register/$',register_views.register_form.as_view(), name='reg'),
url(r'^login/$',login_views.login_form.as_view(), name='log'),

]