from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
<<<<<<< HEAD
    ]
=======
]
>>>>>>> ce5e3c2afc21a308ba87025f6a51b89f31950ab4
