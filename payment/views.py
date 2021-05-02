# import braintree
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from orders.models import Order
from .models import DeditCard


def payment_done(request):
    return render(request, 'payment/done.html')
def payment_canceled(request):
    return render(request, 'payment/canceled.html')

def index(request):
    return render(request, 'payment/index.html')


def payment_process(request):
    debit_card = DeditCard(request)
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    total_cost = order.get_total_cost()
    if request.method == 'POST':
        # retrieve nonce
        nonce = request.POST.get('payment_method_nonce', None)
        # create and submit transaction
        result = None

        if result.is_success:
            # mark the order as paid
            order.paid = True
            # store the unique transaction id
            # order.braintree_id = result.transaction.id
            order.save()
            return redirect('payment:done')
        else:
            return redirect('payment:canceled')
    else:
        # generate token
        # client_token = gateway.client_token.generate()
        return render(request,
                      'payment/process.html',
                      {'order': order,
                    #    'client_token': client_token
                    })