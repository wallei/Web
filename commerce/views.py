from commerce.models import producto, subcategoria, categoria
from django.template import RequestContext
from django.shortcuts import render_to_response

def lista_producto(request):
	productos = producto.objects.all()
	return render_to_response('lista_producto.html',{'lista':productos}, context_instance=RequestContext(request))
