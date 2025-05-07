from django.shortcuts import render

def page_one(request):
    return render(request, 'pages/page_one.html')

def page_two(request):
    return render(request, 'pages/page_two.html')
from django.shortcuts import render, redirect
from .models import User, Category, NeuralNetwork, Subscription, Order, OrderItem, Payment, Review
from .forms import UserForm, CategoryForm, NeuralNetworkForm, SubscriptionForm, OrderForm, OrderItemForm, PaymentForm, ReviewForm

# -------------------- Страницы со списками --------------------

def user_list(request):
    users = User.objects.all()
    return render(request, 'pages/user_list.html', {'users': users})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'pages/category_list.html', {'categories': categories})

def neuralnetwork_list(request):
    networks = NeuralNetwork.objects.all()
    return render(request, 'pages/neuralnetwork_list.html', {'networks': networks})

def subscription_list(request):
    subs = Subscription.objects.all()
    return render(request, 'pages/subscription_list.html', {'subs': subs})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'pages/order_list.html', {'orders': orders})

def orderitem_list(request):
    items = OrderItem.objects.all()
    return render(request, 'pages/orderitem_list.html', {'items': items})

def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'pages/payment_list.html', {'payments': payments})

def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'pages/review_list.html', {'reviews': reviews})

# -------------------- Формы создания записей --------------------

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'pages/create_user.html', {'form': form})

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'pages/create_category.html', {'form': form})

def create_neuralnetwork(request):
    if request.method == 'POST':
        form = NeuralNetworkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('neuralnetwork_list')
    else:
        form = NeuralNetworkForm()
    return render(request, 'pages/create_neuralnetwork.html', {'form': form})

def create_subscription(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subscription_list')
    else:
        form = SubscriptionForm()
    return render(request, 'pages/create_subscription.html', {'form': form})

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'pages/create_order.html', {'form': form})

def create_orderitem(request):
    if request.method == 'POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orderitem_list')
    else:
        form = OrderItemForm()
    return render(request, 'pages/create_orderitem.html', {'form': form})

def create_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
    else:
        form = PaymentForm()
    return render(request, 'pages/create_payment.html', {'form': form})

def create_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review_list')
    else:
        form = ReviewForm()
    return render(request, 'pages/create_review.html', {'form': form})

# ---------- РЕДАКТИРОВАНИЕ И УДАЛЕНИЕ ----------

from django.shortcuts import get_object_or_404

# Пользователь
def edit_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'pages/edit_user.html', {'form': form})

def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'pages/delete_user.html', {'user': user})

# Категория
def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'pages/edit_category.html', {'form': form})

def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'pages/delete_category.html', {'category': category})

# Нейросеть
def edit_neuralnetwork(request, pk):
    network = get_object_or_404(NeuralNetwork, pk=pk)
    if request.method == 'POST':
        form = NeuralNetworkForm(request.POST, instance=network)
        if form.is_valid():
            form.save()
            return redirect('neuralnetwork_list')
    else:
        form = NeuralNetworkForm(instance=network)
    return render(request, 'pages/edit_neuralnetwork.html', {'form': form})

def delete_neuralnetwork(request, pk):
    network = get_object_or_404(NeuralNetwork, pk=pk)
    if request.method == 'POST':
        network.delete()
        return redirect('neuralnetwork_list')
    return render(request, 'pages/delete_neuralnetwork.html', {'network': network})

# Подписка
def edit_subscription(request, pk):
    sub = get_object_or_404(Subscription, pk=pk)
    if request.method == 'POST':
        form = SubscriptionForm(request.POST, instance=sub)
        if form.is_valid():
            form.save()
            return redirect('subscription_list')
    else:
        form = SubscriptionForm(instance=sub)
    return render(request, 'pages/edit_subscription.html', {'form': form})

def delete_subscription(request, pk):
    sub = get_object_or_404(Subscription, pk=pk)
    if request.method == 'POST':
        sub.delete()
        return redirect('subscription_list')
    return render(request, 'pages/delete_subscription.html', {'sub': sub})

# Заказ
def edit_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'pages/edit_order.html', {'form': form})

def delete_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(request, 'pages/delete_order.html', {'order': order})

# Элемент заказа
def edit_orderitem(request, pk):
    item = get_object_or_404(OrderItem, pk=pk)
    if request.method == 'POST':
        form = OrderItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('orderitem_list')
    else:
        form = OrderItemForm(instance=item)
    return render(request, 'pages/edit_orderitem.html', {'form': form})

def delete_orderitem(request, pk):
    item = get_object_or_404(OrderItem, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('orderitem_list')
    return render(request, 'pages/delete_orderitem.html', {'item': item})

# Платеж
def edit_payment(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    if request.method == 'POST':
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
    else:
        form = PaymentForm(instance=payment)
    return render(request, 'pages/edit_payment.html', {'form': form})

def delete_payment(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    if request.method == 'POST':
        payment.delete()
        return redirect('payment_list')
    return render(request, 'pages/delete_payment.html', {'payment': payment})

# Отзыв
def edit_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('review_list')
    else:
        form = ReviewForm(instance=review)
    return render(request, 'pages/edit_review.html', {'form': form})

def delete_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        review.delete()
        return redirect('review_list')
    return render(request, 'pages/delete_review.html', {'review': review})

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_list')
    else:
        form = RegisterForm()
    return render(request, 'pages/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('user_list')
    else:
        form = LoginForm()
    return render(request, 'pages/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')




import json

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, product_id, quantity=1):
        product_id = str(product_id)
        if product_id in self.cart:
            self.cart[product_id] += quantity
        else:
            self.cart[product_id] = quantity
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        self.session['cart'] = {}
        self.save()



@login_required
def cart_view(request):
    cart = Cart(request)
    cart_items = []
    for product_id, quantity in cart.cart.items():
        product = NeuralNetwork.objects.get(id=product_id)
        cart_items.append({'product': product, 'quantity': quantity})
    return render(request, 'pages/cart.html', {'cart_items': cart_items})

from django.shortcuts import redirect
@login_required
def add_to_cart(request, item_id):  # ← добавляем item_id
    cart = request.session.get('cart', {})
    cart[str(item_id)] = cart.get(str(item_id), 0) + 1
    request.session['cart'] = cart
    return redirect('cart')


from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def cart(request):
    cart = request.session.get('cart', {})
    return render(request, 'pages/cart.html', {'cart': cart})


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import NeuralNetwork  # или какой каталог показываешь

@login_required
def catalog(request):
    networks = NeuralNetwork.objects.all()
    return render(request, 'pages/catalog.html', {'networks': networks})


from django.shortcuts import render, redirect
from datetime import date, timedelta
from .forms import CheckoutForm
from .models import Order, OrderItem, NeuralNetwork  # или твоя модель товаров
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from .models import User as CustomUser  # твоя модель User

@login_required
def checkout(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0

    for item_id, quantity in cart.items():
        item = NeuralNetwork.objects.get(id=item_id)
        items.append({'item': item, 'quantity': quantity, 'subtotal': item.price * quantity})
        total += item.price * quantity

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            delivery_type = form.cleaned_data['delivery_type']
            delivery_date = date.today() if delivery_type == 'today' else date.today() + timedelta(days=1)

            # ✅ здесь исправляем поиск
            try:
                db_user = CustomUser.objects.get(email=request.user.email)
            except CustomUser.DoesNotExist:
                return redirect('catalog')  # или вывод ошибки

            order = Order.objects.create(user=db_user, created_at=date.today(), status='Ожидание')

            for item_data in items:
                OrderItem.objects.create(order=order, neuralnetwork=item_data['item'], quantity=item_data['quantity'])

            request.session['cart'] = {}  # очищаем корзину
            return redirect('my_orders')
    else:
        form = CheckoutForm()

    return render(request, 'pages/checkout.html', {'form': form, 'items': items, 'total': total})


@login_required
def my_orders(request):
    db_user = User.objects.get(pk=request.user.pk)  # ← добавляем эту строку
    orders = Order.objects.filter(user=db_user).order_by('-created_at')
    return render(request, 'pages/my_orders.html', {'orders': orders})


