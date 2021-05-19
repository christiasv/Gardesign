from rest_framework import routers

from app_administracion.api.views import ListServiceViewSet, ListServiceApiViewSet, ListProductApiViewSet, \
    DetailProductApiViewSet, CreateContactoApiViewSet, ListBlogApiViewSet

app_name = 'app_api'

router = routers.DefaultRouter()
router.register(r'list-service', ListServiceViewSet, basename='list-service')
router.register(r'list-blogs', ListBlogApiViewSet, basename='list-blogs')
router.register(r'list-api-service', ListServiceApiViewSet, basename='list-api-service')
router.register(r'list-product', ListProductApiViewSet, basename='list-api-producto')
router.register(r'detail-product', DetailProductApiViewSet, basename='detail-api-producto')
router.register(r'create-contact', CreateContactoApiViewSet, basename='create-api-contact')

urlpatterns = router.urls
