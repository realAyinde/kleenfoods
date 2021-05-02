from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from core.models import Item
from .cart import Cart
from .forms import CartAddItemForm
from django.http import JsonResponse

def ajax_cart_add(request):
    cart = Cart(request)
    item_id = request.GET.get('item_id')
    quantity = int(request.GET.get('quantity'))
    item = get_object_or_404(Item, id=item_id)
    if quantity!=None:
        cart.add(item=item, quantity=quantity)
    else:
        cart.add(item=item)
    # form = CartAddItemForm(request.POST)
    # if form.is_valid():
    #     cd = form.cleaned_data
    #     cart.add(item=item,
    #              quantity=cd['quantity'],
    #              override_quantity=cd['override'])

    return JsonResponse({'success': 'Sucessfully Added'})

def ajax_cart_remove(request):
    cart = Cart(request)
    item_id = request.GET.get('item_id')
    item = get_object_or_404(Item, id=item_id)
    cart.remove(item)
    return JsonResponse({'success': True})

@require_POST
def cart_add(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)
    form = CartAddItemForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(item=item,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'])
    return redirect('cart:cart_detail')

@require_POST
def cart_remove(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)
    cart.remove(item)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for each in cart:
        each['update_quantity_form'] = CartAddItemForm(initial= {'quantity': each['quantity'], 'override': True})
    return render(request, 'cart/detail.html', {'cart': cart})
