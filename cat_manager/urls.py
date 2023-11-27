"""
URL configuration for cat_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include
from cats.views import *
from cat_manager.settings import DEBUG, MEDIA_URL, MEDIA_ROOT, STATIC_URL, STATIC_ROOT
from  django.views.static import serve as mediaserve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cats.urls'))
]

handler404 = page_not_found

if DEBUG:

    import mimetypes

    mimetypes.add_type("application/javascript", ".js", True)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

else:
    urlpatterns += [
        url(f'^{MEDIA_URL.lstrip("/")}(?P<path>.*)$',
            mediaserve, {'document_root': MEDIA_ROOT}),
        url(f'^{STATIC_URL.lstrip("/")}(?P<path>.*)$',
            mediaserve, {'document_root': STATIC_ROOT}),
    ]
