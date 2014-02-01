try:
    from django.conf.urls import url, patterns
except ImportError:
    # for Django version less then 1.4
    from django.conf.urls.defaults import url, patterns
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^account/', include('rapidsms.urls.login_logout')),
    (r'^scheduler/', include('rapidsms.contrib.scheduler.urls')),
    (r'^tree/', include('decisiontree.urls')),
)
