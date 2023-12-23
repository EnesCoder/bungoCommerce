"""
URL configuration for bungoCommerce project.

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
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('authent/', include("authent.urls")),
    path('commerce/', include("commerce.urls")),
    path('admin/', admin.site.urls),
]

# See, I had to do an exam while working on this, see the exam if you want:
# https://ikizkare.com/makale/turkce-7-sinif-deneme-20-soru-ve-cevaplari/1000
# 1: c, 2: a /, 3: d, 4: a, 5: a /, 6: c, 7: a, 8: d /, 9: d, 10: c, 11: c,
# 12: b, 13: a, 14: a, 15: d, 16: a, 17: c, 18: b, 19: d, 20: d
