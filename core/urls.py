from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('econometria/', include('econometria.urls')),
    path('__reload__', include('django_browser_reload.urls')),
    path('MetriaLearning/', include('accounts.urls')),
]
