
from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.page_one, name='page_one'),
    path('page-two/', views.page_two, name='page_two'),
    path('users/', views.user_list, name='user_list'),
    path('categories/', views.category_list, name='category_list'),
    path('networks/', views.neuralnetwork_list, name='neuralnetwork_list'),
    path('subscriptions/', views.subscription_list, name='subscription_list'),
    path('orders/', views.order_list, name='order_list'),
    path('order-items/', views.orderitem_list, name='orderitem_list'),
    path('payments/', views.payment_list, name='payment_list'),
    path('reviews/', views.review_list, name='review_list'),
]

urlpatterns += [
    path('users/create/', views.create_user, name='create_user'),
    path('categories/create/', views.create_category, name='create_category'),
    path('networks/create/', views.create_neuralnetwork, name='create_neuralnetwork'),
    path('subscriptions/create/', views.create_subscription, name='create_subscription'),
    path('orders/create/', views.create_order, name='create_order'),
    path('order-items/create/', views.create_orderitem, name='create_orderitem'),
    path('payments/create/', views.create_payment, name='create_payment'),
    path('reviews/create/', views.create_review, name='create_review'),



    # Пользователи
    path('users/edit/<int:pk>/', views.edit_user, name='edit_user'),
    path('users/delete/<int:pk>/', views.delete_user, name='delete_user'),

    # Категории
    path('categories/edit/<int:pk>/', views.edit_category, name='edit_category'),
    path('categories/delete/<int:pk>/', views.delete_category, name='delete_category'),

    # Нейросети
    path('networks/edit/<int:pk>/', views.edit_neuralnetwork, name='edit_neuralnetwork'),
    path('networks/delete/<int:pk>/', views.delete_neuralnetwork, name='delete_neuralnetwork'),

    # Подписки
    path('subscriptions/edit/<int:pk>/', views.edit_subscription, name='edit_subscription'),
    path('subscriptions/delete/<int:pk>/', views.delete_subscription, name='delete_subscription'),

    # Заказы
    path('orders/edit/<int:pk>/', views.edit_order, name='edit_order'),
    path('orders/delete/<int:pk>/', views.delete_order, name='delete_order'),

    # Элементы заказов
    path('orderitems/edit/<int:pk>/', views.edit_orderitem, name='edit_orderitem'),
    path('orderitems/delete/<int:pk>/', views.delete_orderitem, name='delete_orderitem'),

    # Платежи
    path('payments/edit/<int:pk>/', views.edit_payment, name='edit_payment'),
    path('payments/delete/<int:pk>/', views.delete_payment, name='delete_payment'),

    # Отзывы
    path('reviews/edit/<int:pk>/', views.edit_review, name='edit_review'),
    path('reviews/delete/<int:pk>/', views.delete_review, name='delete_review'),


    # path('login/', views.login_view, name='login'),
    # path('register/', views.register_view, name='register'),

    path('cart/', views.cart_view, name='cart_view'),

    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('catalog/', views.catalog, name='catalog'),
    path('cart/', views.cart, name='cart'),
    path('add-to-cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),

    path('checkout/', views.checkout, name='checkout'),
    path('my-orders/', views.my_orders, name='my_orders'),

    path('api/', include('pages.urls_api')),
]
