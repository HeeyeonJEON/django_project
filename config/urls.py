from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('polls/', include('polls.urls')),
    path('bookmark/', include('bookmark.urls')),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
]
