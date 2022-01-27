from django.conf.urls import url
from .views import (
    UserViewUpdate, LoginAPIView
)

app_name = 'authentication'

urlpatterns = [
    url(r'^user/?$', UserViewUpdate.as_view()),
    url(r'^login/?$', LoginAPIView.as_view()),
]
