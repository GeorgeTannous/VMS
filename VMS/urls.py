from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from rest_framework import routers
from main import views

router = routers.DefaultRouter()
router.register(r'main', views.VacationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('main/', include('main.urls')),
    url('^api/', include(router.urls)),
    url(r'^main/create$', views.vacation_create, name='vacation_create'),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
