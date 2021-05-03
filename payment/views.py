# import braintree
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from orders.models import Order
from .models import DeditCard
from .forms import DeditCardCreateForm


def payment_done(request):
    return render(request, 'payment/done.html')
def payment_canceled(request):
    return render(request, 'payment/canceled.html')

def index(request):
    return render(request, 'payment/index.html')


def payment_process(request):
    # if request.method == 'GET':
    #     form = DeditCardCreateForm()
    #     return render(request, 'payment/dummy.html', {'form':form})

    if request.method == 'POST':
        form = DeditCardCreateForm(request.POST)
        print(order_id)
        if form.is_valid():
            print(form)
            number = form.cleaned_data["number"]
            expiry_month = form.cleaned_data["expiry_month"]
            expiry_year = form.cleaned_data["expiry_year"]
            pin = form.cleaned_data["pin"]
            cvv = form.cleaned_data["cvv"]
            try:
                 dedit_card = DeditCard.objects.get(
                     number = number,
                     expiry_month = expiry_month,
                     expiry_year = expiry_year,
                     pin = pin,
                     cvv = cvv
                     )
                 return render(request,"payment/done.html",
                       {"debit_card":dedit_card})

            except DeditCard.DoesNotExist:
                return render(request, "payment/canceled.html", {"form":form})
        # order_id = request.session.get('order_id')
        # order = get_object_or_404(Order, id=order_id)
        # total_cost = order.get_total_cost()
        # # retrieve nonce
        # nonce = request.POST.get('payment_method_nonce', None)
        # # create and submit transaction
        # result = None

        # if result.is_success:
        #     order.paid = True
        #     order.save()
        #     return redirect('payment:done')
        # else:
        #     return redirect('payment:canceled')
    else:
        return render(request, 'payment/dummy.html')
