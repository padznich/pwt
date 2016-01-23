"""mvc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from startpage.views import test1
from home.views import show_db, show_db_id, p_info, p_list, test2, hw1

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^startpage/info/$', test1),

    url(r'^home/$', p_list),
    url(r'^home/([0-9]+)/$', p_info),
    url(r'^home/showdb/$', show_db),
    url(r'^home/showdb/([0-9]+)/$', show_db_id),
    url(r'^home/players_info/$', test2),
    url(r'^home/hw1/$', hw1),
]
