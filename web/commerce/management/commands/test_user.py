'''
Created on 28/1/2015

@author: E457035
'''
from django.core.management.base import NoArgsCommand
from django.contrib.auth.models import User

class Command(NoArgsCommand):
    help = "Print a cliche to the console."

    def handle_noargs(self, **options):
        #usuario de prueba
        print "Creando usuario de prueba..."
        User.objects.create_user(username='usuario', email=None, password='password')
        if User.objects.filter(username='usuario').filter(password='password') is not None:
            print 'Usuario de prueba creado'
        else:
            print 'Error al crear usuario de prueba'