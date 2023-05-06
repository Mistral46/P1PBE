from rest_framework.routers import DefaultRouter
from lada.api.views import LadaApiViewSet

router_post = DefaultRouter()

router_post.register(prefix= 'post', basename= 'post', viewset=LadaApiViewSet)