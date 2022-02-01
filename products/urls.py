from rest_framework.routers import DefaultRouter

from products.views import ProductView


router = DefaultRouter()
router.register("products", ProductView, basename="products")

urlpatterns = router.urls