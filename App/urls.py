from django.urls import path


from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    
    path('', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^/(?P<stream_path>(.*?))$',views.dynamic_stream,name="videostream"),  
    url(r'^stream/$',views.indexscreen),
    path('reconocimiento/', views.indexscreen, name="reconocimiento"),
    path('home', views.index, name='home')

]

"""

urlpatterns = [
   
   # Inicio
    #path('', views.index, name='index')
    path('', views.dynamic_stream ,name="videostream"),  
    path(r'^stream/$',views.indexscreen)
 

   # Enlaces pagina
  
]




"""

# Ejemplo para los enlaces pagina
"""
urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('services/', views.services, name="services"),
    path('store/', views.store, name="store"),
    path('contact/', views.contact, name="contact"),
    path('blog/', views.blog, name="blog"),
    path('sample/', views.sample, name="sample"),
]


"""