from django.shortcuts import render, redirect
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            # order.items = cart.objects.all()
            order_id = order.id
            for item in cart:
                OrderItem.objects.create(
                                        item=item['item'],
                                        price=item['price'],
                                        quantity=item['quantity'])

            # clear the cart
            cart.clear()   
            # return render("payment:process",)
            return render(request,
                            # 'payment/dummy.html',
                          'orders/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
        return render(request,
                  'orders/create.html',
                  {'cart': cart, 'form': form})
