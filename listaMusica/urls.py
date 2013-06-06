from django.conf.urls import patterns, include, url
from generador.views import Home, Registro, Ingreso

urlpatterns = patterns('',
    url(r'^$',Home,name="inicio"),
    url(r'^registro/$', Registro.as_view(), name="registro"),
    url(r'^ingreso/$', Ingreso, name="ingreso"),
    # Examples:
    # url(r'^$', 'listaMusica.views.home', name='home'),
    # url(r'^listaMusica/', include('listaMusica.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
