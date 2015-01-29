from commerce.models import producto, subcategoria, categoria
from django.contrib.auth import (authenticate, login as auth_login, logout)
from django.contrib.auth.models import User
from django.shortcuts import render
from django.core.context_processors import csrf
from web.forms import LoginForm
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.decorators import login_required

HOME = 'login.html'

def lista_producto(request):
	productos = producto.objects.all()
	return render(request, 'lista_producto.html', {'lista':productos})

def login(request):
	args = {}
	args.update(csrf(request))
	if request.user is None or not request.user.is_authenticated():
		if request.POST:
			form = LoginForm(request.POST)
			# if (form.is_valid()): #valida que exista en la base
			un = request.POST.get('username')
			pw = request.POST.get('password')
			user = authenticate(username=un, password=pw); 
			if user is not None:
				auth_login(request, user)
				return perfil(request)
			else:
				args['msg'] = 'Datos de acceso incorrectos!!!'
			# else:
				# print 'faltan datos'
	else:
		return perfil(request)
	
	return render(request, HOME, args)

@login_required(login_url='/login/')
def perfil(request):
	args = {}
	args.update(csrf(request))
	args['usuario'] = request.user
	return render(request, 'perfil.html', args)

def salir(request):
	args = {}
	args.update(csrf(request))
	if request.user is not None and request.user.is_authenticated():
		logout(request)
		
	return render(request, HOME, args)