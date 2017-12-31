from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from quickstart import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^pflege/$',views.PflegeView.as_view()),
    #url(r'^(?ide=\d+)/Pflege/$',views.PflegeView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
