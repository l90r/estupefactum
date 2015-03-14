from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'web.views.home', name='home'),
    url(r'^recent$', 'web.views.recent', name='recent'),
    url(r'^contributors$', 'web.views.contributors', name='contributors'),
    url(r'^submit$', 'web.views.submit', name='submit'),
    url(r'^login$', 'web.views.login', name='login'),
    url(r'^signup$', 'web.views.signup', name='signup'),
    url(r'^logout$', 'web.views.logout', name='logout'),
    url(r'^admin/', include(admin.site.urls)),
)
