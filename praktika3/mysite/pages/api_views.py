from rest_framework import viewsets, permissions, filters
from .models import User, Category, NeuralNetwork, Subscription, Order, OrderItem, Payment, Review
from .serializers import UserSerializer, CategorySerializer, NeuralNetworkSerializer, SubscriptionSerializer, OrderSerializer, OrderItemSerializer, PaymentSerializer, ReviewSerializer

# Пример запрета на POST, PUT, DELETE для User
class ReadOnlyMixin:
    http_method_names = ['get', 'head', 'options']

class UserViewSet(ReadOnlyMixin, viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]# Только админ видит пользователей
    filter_backends = [filters.SearchFilter]
    search_fields = ['email']

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class NeuralNetworkViewSet(viewsets.ModelViewSet):
    queryset = NeuralNetwork.objects.all()
    serializer_class = NeuralNetworkSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['type']

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['status']

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['neuralnetwork__title']

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['status']

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['comment']