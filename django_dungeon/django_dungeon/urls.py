from django.conf.urls import include, url
from dungeon import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_dungeon.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'dungeon.views.home_page', name='home'),
]
