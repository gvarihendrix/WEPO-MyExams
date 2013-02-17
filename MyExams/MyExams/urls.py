from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import DetailView
from myexams.models import ExamsTaken
from django.contrib.auth.decorators import login_required
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
    url(r'^course/newexam/(?P<course_id>\d+)/$',   'new'),
    url(r'^create/',   'create'),
    url(r'^course/(?P<exam_id>\d+)/submit/$', 'submit'),
    url(r'^(?P<pk>\d+)/result/$', login_required(DetailView.as_view(model=ExamsTaken,
                        template_name='myexams/result.html')), name='exam_result'),
    url(r'^admin/', include(admin.site.urls)),
)
