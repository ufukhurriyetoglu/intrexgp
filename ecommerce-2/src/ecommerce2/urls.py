from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from newsletter import views as news_views
from . import views as commerce_views

urlpatterns = [
    # Examples:
    url(r'^$', news_views.home, name='home'),
    url(r'^contact/$', news_views.contact , name='contact'),
    url(r'^about/$', commerce_views.about , name='about'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^products/', include('products.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
