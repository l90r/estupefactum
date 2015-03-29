from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'web.views.home', name='home'),
    url(r'^recent$', 'web.views.recent', name='recent'),
    url(r'^contributors$', 'web.views.contributors', name='contributors'),
    url(r'^submit$', 'web.views.submit', name='submit'),
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^signup$', 'web.views.signup', name='signup'),
    url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page':'/'}, name='logout'),
    url(r'^admin/', include(admin.site.urls)),
)
