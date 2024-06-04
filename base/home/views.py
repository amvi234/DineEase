from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from vege.models import Receipe

def upi_id(request):
    return HttpResponse('UPI id: amitv234ks@okicici')

def update_total(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.method == 'POST':
        receipe_id = request.POST.get('receipe_id')
        action = request.POST.get('action')
        receipe = Receipe.objects.get(id=receipe_id)
        total = request.session.get('total', 0.0)
        reset = request.session.get('reset')

        if action == 'add':
            total += receipe.receipe_price
        elif action == 'remove':
            total -= receipe.receipe_price

        request.session['total'] = total

        return JsonResponse({'total': total})

def home(request):
    queryset = Receipe.objects.all()
    total = request.session.get('total', 0.0)
    context = {'receipes': queryset, 'total': total}
    return render(request, 'base.html', context)
