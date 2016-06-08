"""imagepipe URLs."""
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from . import settings, views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.render_mashup_index, name='mashup_index'),
    url(r'^mashups$', views.render_mashup_index),
    url(r'^mashup/(?P<mashup_id>\d+)$', views.render_mashup, name='mashup'),
    url(r'^sources$', views.render_src_index, name='src_index'),
    url(r'^source/(?P<src_id>\d+)$', views.render_src, name='src'),
    url(r'^upload$', views.render_upload, name='upload'),
    url(r'^upload/submit$', views.render_upload_submit, name='upload_submit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
