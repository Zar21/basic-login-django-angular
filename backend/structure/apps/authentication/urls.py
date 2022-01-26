from django.conf.urls import include, url
from .views import (
    UserViewSet, LoginAPIView
)

app_name = 'authentication'

urlpatterns = [
    url(r'^user/?$', UserViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    url(r'^login/?$', LoginAPIView.as_view()),
]
