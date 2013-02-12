from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.contrib.auth.views import login, logout
admin.autodiscover()



urlpatterns = patterns('myexams.views',
    # Example:
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', TemplateView.as_view(template_name='base.html')),
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout),
    url(r'^$',    'index'),
    url(r'^student/$', 'student'),
    url(r'^teacher/$', 'teacher'),
    url(r'^course/(?P<course_id>\d+)/$', 'course'),
    url(r'^exams/(?P<exam_id>\d+)/$',    'exams'),
    #url(r'^/(?P<exam_id>\d+)/$', 'myexams.views.detail'),
    #url(r'^MyExams/(?P<exam_id>\d+)/results/$', 'myexams.views.results'),
    #url(r'^MyExams/(?P<exam_id>\d+)/score/$', 'myexams.views.score'),
    url(r'^admin/', include(admin.site.urls)),
)


