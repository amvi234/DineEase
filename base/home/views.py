import os
from dotenv import load_dotenv
load_dotenv()

TEST_KEY_ID = os.getenv('RAZORPAY_TEST_KEY_ID')
TEST_KEY_SECRET = os.getenv('RAZORPAY_TEST_KEY_SECRET')


from django.http import JsonResponse
from django.shortcuts import render, redirect
from vege.models import Receipe
import uuid
import time
import razorpay

def update_total(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.method == 'POST':
        receipe_id = request.POST.get('receipe_id')
        action = request.POST.get('action')
        receipe = Receipe.objects.get(id=receipe_id)
        total = request.session.get('total', 0.0)

        if action == 'add':
            total += receipe.receipe_price
        elif action == 'remove':
            total -= receipe.receipe_price

        request.session['total'] = total

        return JsonResponse({'total': total})

def home(request):
    request.session['total'] = 0.0
    queryset = Receipe.objects.all()
    context = {'receipes': queryset, 'total': 0.0}
    return render(request, 'base.html', context)


def create_razorpay_payment_link(request):
    client = razorpay.Client(auth=(TEST_KEY_ID, TEST_KEY_SECRET))

    total_amount = request.session.get('total', 0.0) * 100 
    expire_by = int(time.time()) + (24 * 60 * 60) 
    reference_id = str(uuid.uuid4())[:8]

    payment_link_data = {
        "amount": total_amount,
        "currency": "INR",
        "accept_partial": False,
        "first_min_partial_amount": None,
        "expire_by": expire_by,
        "reference_id": reference_id,
        "description": "Payment for your order",
        "customer": {
            "name": "Amit",
            "email": "amitvikram2341@gmail.com",
            "contact": "9534456949"
        },
        "notify": {
            "sms": True,
            "email": True
        },
        "reminder_enable": True,
        "notes": {
            "policy_name": "Manifest Receipe"
        },
    }
    
    payment_link = client.payment_link.create(data=payment_link_data)
    payment_link_url = payment_link['short_url']
    
    return redirect(payment_link_url)
