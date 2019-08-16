from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if 'total_spent' not in request.session or 'total_items' not in request.session:
        print('hi')
        request.session['total_spent'] = 0
        request.session['total_items'] = 0
        request.session['last_sale'] = 0
    return render(request, 'amadon_app/index.html')

def process_sale(request):
    products =  {
        'shirt' : 19.99,
        'sweater' : 29.99,
        'cup' : 4.99,
        'book' : 49.99
    }
    request.session['total_items'] += int(request.POST['quantity'])
    request.session['last_sale'] = products[request.POST['product']] * int(request.POST['quantity'])
    request.session['last_sale'] = round(request.session['last_sale'], 2)
    request.session['total_spent'] += request.session['last_sale']
    request.session['total_spent'] = round(request.session['total_spent'], 2)
    return redirect('/amadon/checkout')

def checkout(request):
    context = {
        'cur_transaction' : request.session['last_sale'],
        'total_items' : request.session['total_items'],
        'total_spent' : request.session['total_spent'],
    }
    return render(request, 'amadon_app/checkout.html', context)