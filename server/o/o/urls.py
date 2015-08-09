from django.conf.urls import patterns, include, url
from django.contrib import admin
#from polls.views import LadyList
from polls import views

# Toturial 2
from rest_framework.urlpatterns import format_suffix_patterns

admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'o.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^mongonaut/', include('mongonaut.urls')),
	#url(r'^lady/', LadyList.as_view(), name='lady-list'),
    #url(r'^', include('polls.urls')),
	
	#Tutorial 1, 2
	#url(r'^snippets/$', views.snippet_list),
	#url(r'^snippets/(?P<pk>[A-Za-z0-9]+)/$', views.snippet_detail),

	# Tutorial 3
	url(r'^snippets/$', views.SnippetList.as_view()),
	url(r'^snippets/(?P<pk>[A-Za-z0-9]+)/$', views.SnippetDetail.as_view()),

	url(r'^signup-email/', 'polls.views.signup_email'),
    url(r'^email-sent/', 'polls.views.validation_sent'),
    url(r'^login/$', 'polls.views.home'),
    url(r'^done/$', 'polls.views.done', name='done'),
    url(r'^email/$', 'polls.views.require_email', name='require_email'),
    url(r'', include('social.apps.django_app.urls', namespace='social')),

    url(r'^users/$', views.UserList.as_view()),

)

#urlpatterns = format_suffix_patterns(urlpatterns)
