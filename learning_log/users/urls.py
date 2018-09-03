from django.conf.urls import url
from django.contrib.auth.views import login

from . import views


"""定义users的url模式"""
urlpatterns = [
    # 登录页面
    url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
]