from django.shortcuts import render

def store(request):
	context = {}
	return render(request, 'store/store.html', context)

def cart(request):
	context = {}
	return render(request, 'store/cart.html', context)

def checkout(request):
	context = {}
	return render(request, 'store/checkout.html', context)

def login(request):
	context = {}
	return render(request, 'store/login.html',context)

def register(request):
	context = {}
	return render(request, 'store/register.html',context)