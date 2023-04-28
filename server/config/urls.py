from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'Invite People'
admin.site.site_title = 'Invite People Admin Panel'
admin.site.index_title = 'Invite People Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include([
        path('auth/', include('djoser.urls')),
        path('auth/', include('djoser.urls.jwt')),
        path('users/', include('users.api.urls', namespace='users')),
    ]))
]
