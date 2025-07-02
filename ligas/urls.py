
from rest_framework.routers import DefaultRouter
from .views import DeporteViewSet, FederacionViewSet, LigaViewSet

router = DefaultRouter()
router.register(r'deportes', DeporteViewSet)
router.register(r'federaciones', FederacionViewSet)
router.register(r'ligas', LigaViewSet)

urlpatterns = router.urls
