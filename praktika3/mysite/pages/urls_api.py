from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import api_views


router = DefaultRouter()
router.register(r'users', api_views.UserViewSet)
router.register(r'categories', api_views.CategoryViewSet)
router.register(r'networks', api_views.NeuralNetworkViewSet)
router.register(r'subscriptions', api_views.SubscriptionViewSet)
router.register(r'orders', api_views.OrderViewSet)
router.register(r'orderitems', api_views.OrderItemViewSet)
router.register(r'payments', api_views.PaymentViewSet)
router.register(r'reviews', api_views.ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]