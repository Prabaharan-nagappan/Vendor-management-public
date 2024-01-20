# vendors/urls.py
from rest_framework import routers
from .views import VendorViewSet, PurchaseOrderViewSet

router = routers.DefaultRouter()
router.register(r'vendors', VendorViewSet)
router.register(r'purchase_orders', PurchaseOrderViewSet)

urlpatterns = router.urls
