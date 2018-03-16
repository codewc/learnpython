"""learn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views
'''
The tutorial project has just one app, polls. In real Django projects, there might be five, ten, twenty apps or more. How does Django differentiate the URL names between them? For example, the polls app has a detail view, and so might an app on the same project that is for a blog. How does one make it so that Django knows which app view to create for a url when using the {% url %} template tag?

The answer is to add namespaces to your URLconf. In the polls/urls.py file, go ahead and add an app_name to set the application namespace:
like: app_name = 'polls'
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
'''
app_name = 'hello'
urlpatterns = [
    #ex: /hello/
    path('', views.index, name='index'),
    #ex /helllo/5/
    # the 'name' value as called by the {% url %} template tag
    path('<int:querstion_id>/',views.detail,name='detail'),
    path('<int:querstion_id>/results/',views.reslult,name='results'),
    path('<int:querstion_id>/vote/',views.vote,name='vote'),
]
