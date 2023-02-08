from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Invernadero, TomateCosecha, CosechaCampokg, CosechaCampo, EmpacadorEmpaque,  TransporteInvernadero, TransporteEmpaque,CalidadRecepcion, ChileminiEmpaque, ChileminiCosecha, CadenaFrio,   TomateCosecha,TomateEmpaque

from django.views.generic.edit import DeleteView
from django.urls import reverse
###############
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils.decorators import method_decorator

from .utils import render_to_pdf

###################

   
# Insertar datos


# Para insertar un nuevo contacto en la tabla Contactos

@method_decorator(login_required(login_url='login'), name='dispatch')
class registroNuevo(SuccessMessageMixin, CreateView):
    
    model = CosechaCampokg
    form = CosechaCampokg
    fields = '__all__'
    widgets = {'fecha': forms.DateInput(attrs={'type': 'date'})}
    
    # Mensaje que se mostrará cuando se inserte el registro
    success_message = 'Registro añadido exitosamente.'

    # Redirigimos a la página principal tras insertar el registro
   
    def get_success_url(self):
        return reverse('listar')
    

# Para eliminar un contacto de la tabla Contactos


class eliminarRegistro(SuccessMessageMixin, DeleteView):
    model = CosechaCampokg
    form = CosechaCampokg
    fields = '__all__'
    
    # Redireccionamos a la página principal tras de eliminar el registro
    def get_success_url(self):
        # Mensaje que se mostrará cuando se elimine el registro
        success_message = 'Registro eliminado correctamente.'
        messages.success(self.request, (success_message))
        return reverse('listar')

# Para modificar un contacto existente de la tabla Contactos


class actualizarRegistro(SuccessMessageMixin, UpdateView):
    model = CosechaCampokg
    form = CosechaCampokg
    fields = '__all__'
    # Mensaje que se mostrará cuando se actualice el registro
    success_message = 'Registro actualizado correctamente.'

    # Redireccionamos a la página principal tras actualizar el registro
    def get_success_url(self):
        return reverse('listar')


def homeViews(request):
    return render(request, 'AlphaC/home.html')


def registroUser(request):

    if request.method == 'GET':
        return render(request, 'AlphaC/registroUser.html', {
            'form': UserCreationForm
        })

    else:
        if request.POST['password1'] == request.POST['password2']:
            # registrar usuario
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return  redirect('login')
            except IntegrityError:
                return render(request, 'AlphaC/registroUser.html', {
                    'form': UserCreationForm,
                    "error": 'Usuario ya existe.'
                })

        return render(request, 'AlphaC/registroUser.html', {
            'form': UserCreationForm,
            "error": 'Constraseñas no coinciden.'
        })

@login_required(login_url='/login')
def principalViews(request):
    return render(request, 'AlphaC/principal.html')


def cerrarViews(request):
    logout(request)
    return redirect('home')

def iniciarSesionViews(request):
    if request.method == 'GET':
        return render(request, 'AlphaC/login.html', {
            "form":AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password']
        )
        if user is None:
            return render(request, 'AlphaC/login.html', {
            "form":AuthenticationForm, 
            "error": 'Usuario o contraseña incorrectos.'
            })
        else:
            login(request, user)
            return redirect('principal')



# Chile BLOCKY MENU
# INVERNADERO COSECHA POR UNIDADES------------------------------------------------------------------------------
@login_required(login_url='/login')
def homeViewsBlocky(request):
    return render(request, 'AlphaC/homeChileBlocky.html')

@method_decorator(login_required(login_url='login'), name='dispatch')
class InvernaderoViews(ListView):
    
    model = CosechaCampo

@method_decorator(login_required(login_url='login'), name='dispatch')
class registroNuevoCosechaUnidades(SuccessMessageMixin, CreateView):
    
    model = CosechaCampo
    form = CosechaCampo
    fields = '__all__'
    
    
    # Mensaje que se mostrará cuando se inserte el registro
    success_message = 'Registro añadido exitosamente.'

    # Redirigimos a la página principal tras insertar el registro
   
    def get_success_url(self):
        return reverse('Invernadero')

class eliminarBlockyCosechaUni(SuccessMessageMixin, DeleteView):
    model = CosechaCampo
    form = CosechaCampo
    fields = '__all__'
    
    # Redireccionamos a la página principal tras de eliminar el registro
    def get_success_url(self):
        # Mensaje que se mostrará cuando se elimine el registro
        success_message = 'Registro eliminado correctamente.'
        messages.success(self.request, (success_message))
        return reverse('Invernadero')

@method_decorator(login_required(login_url='login'), name='dispatch')
class actualizarRegistroInvernadero(SuccessMessageMixin, UpdateView): 
    model = CosechaCampo
    form = CosechaCampo
    fields = '__all__'
    # Mensaje que se mostrará cuando se actualice el registro
    success_message = 'Registro actualizado correctamente.'

    # Redireccionamos a la página principal tras actualizar el registro
    def get_success_url(self):
        return reverse('Invernadero')
#-------------------------------------------------------------------------------------------------------------
      



#INVERNADERO COSECHA BLOCKY POR KG------------------------------------------------------------------------

@login_required(login_url='/login')
def homeViewsBlocky(request):
    return render(request, 'AlphaC/HomeChileBlocky.html')

@method_decorator(login_required(login_url='login'), name='dispatch')
class BcampokgViews(ListView):
    
    model = CosechaCampokg

@method_decorator(login_required(login_url='login'), name='dispatch')
class registroNuevoCosechakg(SuccessMessageMixin, CreateView):
    
    model = CosechaCampokg
    form = CosechaCampokg
    fields = '__all__'
    
    
    # Mensaje que se mostrará cuando se inserte el registro
    success_message = 'Registro añadido exitosamente.'

    # Redirigimos a la página principal tras insertar el registro
   
    def get_success_url(self):
        return reverse('Bcampokg')

class eliminarBlockyCosechaKg(SuccessMessageMixin, DeleteView):
    model = CosechaCampokg
    form = CosechaCampokg
    fields = '__all__'
    
    # Redireccionamos a la página principal tras de eliminar el registro
    def get_success_url(self):
        # Mensaje que se mostrará cuando se elimine el registro
        success_message = 'Registro eliminado correctamente.'
        messages.success(self.request, (success_message))
        return reverse('Bcampokg')

@method_decorator(login_required(login_url='login'), name='dispatch')
class actualizarRegistroInvernaderoKg(SuccessMessageMixin, UpdateView): 
    model = CosechaCampokg
    form = CosechaCampokg
    fields = '__all__'
    # Mensaje que se mostrará cuando se actualice el registro
    success_message = 'Registro actualizado correctamente.'

    # Redireccionamos a la página principal tras actualizar el registro
    def get_success_url(self):
        return reverse('Bcampokg')


#---------------------------------------------------------------------------------------------




#BLOCKY POR EMPACADOR--------------------------------------------------------------------------

@login_required(login_url='/login')
def homeViewsBlocky(request):
    return render(request, 'AlphaC/HomeChileBlocky.html')

@method_decorator(login_required(login_url='login'), name='dispatch')
class EmpacadorViews(ListView):
    
    model = EmpacadorEmpaque

@method_decorator(login_required(login_url='login'), name='dispatch')
class registroNuevoEmpacador(SuccessMessageMixin, CreateView):
    
    model = EmpacadorEmpaque
    form = EmpacadorEmpaque
    fields = '__all__'
    
    
    # Mensaje que se mostrará cuando se inserte el registro
    success_message = 'Registro añadido exitosamente.'

    # Redirigimos a la página principal tras insertar el registro
   
    def get_success_url(self):
        return reverse('Empacador')

class eliminarRegistroEmpacador(SuccessMessageMixin, DeleteView):
    model = EmpacadorEmpaque
    form = EmpacadorEmpaque
    fields = '__all__'
    
    # Redireccionamos a la página principal tras de eliminar el registro
    def get_success_url(self):
        # Mensaje que se mostrará cuando se elimine el registro
        success_message = 'Registro eliminado correctamente.'
        messages.success(self.request, (success_message))
        return reverse('Empacador')

@method_decorator(login_required(login_url='login'), name='dispatch')
class actualizarRegistroEmpacador(SuccessMessageMixin, UpdateView): 
    model = EmpacadorEmpaque
    form = EmpacadorEmpaque
    fields = '__all__'
    # Mensaje que se mostrará cuando se actualice el registro
    success_message = 'Registro actualizado correctamente.'

    # Redireccionamos a la página principal tras actualizar el registro
    def get_success_url(self):
        return reverse('Empacador')






#Calidad de recepcion --------------------------------------------------------------------------

@login_required(login_url='/login')
def homeViewsBlocky(request):
    return render(request, 'AlphaC/HomeChileBlocky.html')

@method_decorator(login_required(login_url='login'), name='dispatch')
class RecepcionViews(ListView):
    
    model = CalidadRecepcion



#home chile mini-----------------------------------------------------------------------------------------
#chile en campo


@login_required(login_url='/login')
def HomeChileMini(request):
    return render(request, 'AlphaC/HomeChileMini.html')


@method_decorator(login_required(login_url='login'), name='dispatch')
class ChileminiViews(ListView):
    
    model =  ChileminiCosecha
    template_name = "AlphaC/minicampo.html"
    context_object_name = 'minicampo'

#PDF
class ListChileMiniCampoPdf(View):

    def get(self, request, *args, **kwargs):
        chilesMini = ChileminiCosecha.objects.all()
        data = {
            'count': chilesMini.count(),
            'chilesMini': chilesMini
        }
        pdf = render_to_pdf('AlphaC/chileminicampopdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
    


@method_decorator(login_required(login_url='login'), name='dispatch')
class registroNuevoChileMiniCosecha(SuccessMessageMixin, CreateView):
    
    model = ChileminiCosecha
    form = ChileminiCosecha
    fields = '__all__'
    
    
    # Mensaje que se mostrará cuando se inserte el registro
    success_message = 'Registro añadido exitosamente.'

    # Redirigimos a la página principal tras insertar el registro
   
    def get_success_url(self):
        return reverse('ChileminiCampo')

class eliminarRegistroChileMiniCosecha(SuccessMessageMixin, DeleteView):
    model = ChileminiCosecha
    form = ChileminiCosecha
    fields = '__all__'
    
    # Redireccionamos a la página principal tras de eliminar el registro
    def get_success_url(self):
        # Mensaje que se mostrará cuando se elimine el registro
        success_message = 'Registro eliminado correctamente.'
        messages.success(self.request, (success_message))
        return reverse('ChileminiCampo')

@method_decorator(login_required(login_url='login'), name='dispatch')
class actualizarRegistroChileMiniCosecha(SuccessMessageMixin, UpdateView): 
    model = ChileminiCosecha
    form = ChileminiCosecha
    fields = '__all__'
    # Mensaje que se mostrará cuando se actualice el registro
    success_message = 'Registro actualizado correctamente.'

    # Redireccionamos a la página principal tras actualizar el registro
    def get_success_url(self):
        return reverse('ChileminiCampo')





#Chile Mini Empaque------------------------------------------------------------------------------------------------
@method_decorator(login_required(login_url='login'), name='dispatch')
class ChileminiEmpaqueViews(ListView):
    
    model =  ChileminiEmpaque

@method_decorator(login_required(login_url='login'), name='dispatch')
class registroNuevoChileMiniEmpaque(SuccessMessageMixin, CreateView):
    
    model = ChileminiEmpaque
    form = ChileminiEmpaque
    fields = '__all__'
    
    
    # Mensaje que se mostrará cuando se inserte el registro
    success_message = 'Registro añadido exitosamente.'

    # Redirigimos a la página principal tras insertar el registro
   
    def get_success_url(self):
        return reverse('ChileminiEmpaque')

class eliminarRegistroChileMiniEmpaque(SuccessMessageMixin, DeleteView):
    model = ChileminiEmpaque
    form = ChileminiEmpaque
    fields = '__all__'
    
    # Redireccionamos a la página principal tras de eliminar el registro
    def get_success_url(self):
        # Mensaje que se mostrará cuando se elimine el registro
        success_message = 'Registro eliminado correctamente.'
        messages.success(self.request, (success_message))
        return reverse('ChileminiEmpaque')

@method_decorator(login_required(login_url='login'), name='dispatch')
class actualizarRegistroChileMiniEmpaque(SuccessMessageMixin, UpdateView): 
    model = ChileminiEmpaque
    form = ChileminiEmpaque
    fields = '__all__'
    # Mensaje que se mostrará cuando se actualice el registro
    success_message = 'Registro actualizado correctamente.'

    # Redireccionamos a la página principal tras actualizar el registro
    def get_success_url(self):
        return reverse('ChileminiEmpaque')




#HOME TOMATE-----------------------------------------------------------------------------------
#Cosecha
@login_required(login_url='/login')
def HomeTomate(request):
    return render(request, 'AlphaC/HomeTomate.html')


@method_decorator(login_required(login_url='login'), name='dispatch')
class TomateCosechaViews(ListView):
    
    model =  TomateCosecha

@method_decorator(login_required(login_url='login'), name='dispatch')
class registroNuevoTomateCosecha(SuccessMessageMixin, CreateView):
    
    model = TomateCosecha
    form = TomateCosecha
    fields = '__all__'
    
    
    # Mensaje que se mostrará cuando se inserte el registro
    success_message = 'Registro añadido exitosamente.'

    # Redirigimos a la página principal tras insertar el registro
   
    def get_success_url(self):
        return reverse('TomateCosecha')

class eliminarRegistroTomateCosecha(SuccessMessageMixin, DeleteView):
    model = TomateCosecha
    form = TomateCosecha
    fields = '__all__'
    
    # Redireccionamos a la página principal tras de eliminar el registro
    def get_success_url(self):
        # Mensaje que se mostrará cuando se elimine el registro
        success_message = 'Registro eliminado correctamente.'
        messages.success(self.request, (success_message))
        return reverse('TomateCosecha')

@method_decorator(login_required(login_url='login'), name='dispatch')
class actualizarRegistroTomateCosecha(SuccessMessageMixin, UpdateView): 
    model = TomateCosecha
    form = TomateCosecha
    fields = '__all__'
    # Mensaje que se mostrará cuando se actualice el registro
    success_message = 'Registro actualizado correctamente.'

    # Redireccionamos a la página principal tras actualizar el registro
    def get_success_url(self):
        return reverse('TomateCosecha')


#Tomate Empaque-------------------------------------------------------------------------------------
@method_decorator(login_required(login_url='login'), name='dispatch')
class TomateEmpaqueViews(ListView):
    
    model =  TomateEmpaque

@method_decorator(login_required(login_url='login'), name='dispatch')
class registroNuevoTomateEmpaque(SuccessMessageMixin, CreateView):
    
    model = TomateEmpaque
    form = TomateEmpaque
    fields = '__all__'
    
    
    # Mensaje que se mostrará cuando se inserte el registro
    success_message = 'Registro añadido exitosamente.'

    # Redirigimos a la página principal tras insertar el registro
   
    def get_success_url(self):
        return reverse('TomateEmpaque')

class eliminarRegistroTomateEmpaque(SuccessMessageMixin, DeleteView):
    model = TomateEmpaque
    form = TomateEmpaque
    fields = '__all__'
    
    # Redireccionamos a la página principal tras de eliminar el registro
    def get_success_url(self):
        # Mensaje que se mostrará cuando se elimine el registro
        success_message = 'Registro eliminado correctamente.'
        messages.success(self.request, (success_message))
        return reverse('TomateEmpaque')

@method_decorator(login_required(login_url='login'), name='dispatch')
class actualizarRegistroTomateEmpaque(SuccessMessageMixin, UpdateView): 
    model = TomateEmpaque
    form = TomateEmpaque
    fields = '__all__'
    # Mensaje que se mostrará cuando se actualice el registro
    success_message = 'Registro actualizado correctamente.'

    # Redireccionamos a la página principal tras actualizar el registro
    def get_success_url(self):
        return reverse('TomateEmpaque')



#HOME TRANSPORTE
@login_required(login_url='/login')
def HomeTransporte(request):
    return render(request, 'AlphaC/hometransporte.html')


# Transporte Invernandero---------------------------------------------------------------
@method_decorator(login_required(login_url='login'), name='dispatch')
class TransporteInvernaderoViews(ListView):
    
    model =  TransporteInvernadero

@method_decorator(login_required(login_url='login'), name='dispatch')
class registroNuevoTransInvernadero(SuccessMessageMixin, CreateView):
    
    model = TransporteInvernadero
    form = TransporteInvernadero
    fields = '__all__'
    
    
    # Mensaje que se mostrará cuando se inserte el registro
    success_message = 'Registro añadido exitosamente.'

    # Redirigimos a la página principal tras insertar el registro
   
    def get_success_url(self):
        return reverse('TransporteInvernadero')

class eliminarRegistroTransInvernadero(SuccessMessageMixin, DeleteView):
    model = TransporteInvernadero
    form = TransporteInvernadero
    fields = '__all__'
    
    # Redireccionamos a la página principal tras de eliminar el registro
    def get_success_url(self):
        # Mensaje que se mostrará cuando se elimine el registro
        success_message = 'Registro eliminado correctamente.'
        messages.success(self.request, (success_message))
        return reverse('TransporteInvernadero')

@method_decorator(login_required(login_url='login'), name='dispatch')
class actualizarRegistroTransInvernadero(SuccessMessageMixin, UpdateView): 
    model = TransporteInvernadero
    form = TransporteInvernadero
    fields = '__all__'
    # Mensaje que se mostrará cuando se actualice el registro
    success_message = 'Registro actualizado correctamente.'

    # Redireccionamos a la página principal tras actualizar el registro
    def get_success_url(self):
        return reverse('TransporteInvernadero')



#Transporte Empaque----------------------------------------------------------------------
@method_decorator(login_required(login_url='login'), name='dispatch')
class TrasnporteEmpaqueViews(ListView):
    
    model =  TransporteEmpaque

@method_decorator(login_required(login_url='login'), name='dispatch')
class registroNuevoTransEmpaque(SuccessMessageMixin, CreateView):
    
    model = TransporteEmpaque
    form = TransporteEmpaque
    fields = '__all__'
    
    
    # Mensaje que se mostrará cuando se inserte el registro
    success_message = 'Registro añadido exitosamente.'

    # Redirigimos a la página principal tras insertar el registro
   
    def get_success_url(self):
        return reverse('TransporteEmpaque')

class eliminarRegistroTransEmpaque(SuccessMessageMixin, DeleteView):
    model = TransporteEmpaque
    form = TransporteEmpaque
    fields = '__all__'
    
    # Redireccionamos a la página principal tras de eliminar el registro
    def get_success_url(self):
        # Mensaje que se mostrará cuando se elimine el registro
        success_message = 'Registro eliminado correctamente.'
        messages.success(self.request, (success_message))
        return reverse('TransporteEmpaque')

@method_decorator(login_required(login_url='login'), name='dispatch')
class actualizarRegistroTransEmpaque(SuccessMessageMixin, UpdateView): 
    model = TransporteEmpaque
    form = TransporteEmpaque
    fields = '__all__'
    # Mensaje que se mostrará cuando se actualice el registro
    success_message = 'Registro actualizado correctamente.'

    # Redireccionamos a la página principal tras actualizar el registro
    def get_success_url(self):
        return reverse('TransporteEmpaque')


#HOME CADENA FRIO
@login_required(login_url='/login')
def HomeCadenaFrio(request):
    return render(request, 'AlphaC/homecadenafrio.html')

@method_decorator(login_required(login_url='login'), name='dispatch')
class CadenaFrioViews(ListView):
    
    model =  CadenaFrio

@method_decorator(login_required(login_url='login'), name='dispatch')
class registroNuevoCadenaFrio(SuccessMessageMixin, CreateView):
    
    model = CadenaFrio
    form = CadenaFrio
    fields = '__all__'
    
    
    # Mensaje que se mostrará cuando se inserte el registro
    success_message = 'Registro añadido exitosamente.'

    # Redirigimos a la página principal tras insertar el registro
   
    def get_success_url(self):
        return reverse('CadenaFrio')

class eliminarRegistroCadenaFrio(SuccessMessageMixin, DeleteView):
    model = CadenaFrio
    form = CadenaFrio
    fields = '__all__'
    
    # Redireccionamos a la página principal tras de eliminar el registro
    def get_success_url(self):
        # Mensaje que se mostrará cuando se elimine el registro
        success_message = 'Registro eliminado correctamente.'
        messages.success(self.request, (success_message))
        return reverse('CadenaFrio')

@method_decorator(login_required(login_url='login'), name='dispatch')
class actualizarRegistroCadenaFrio(SuccessMessageMixin, UpdateView): 
    model = CadenaFrio
    form = CadenaFrio
    fields = '__all__'
    # Mensaje que se mostrará cuando se actualice el registro
    success_message = 'Registro actualizado correctamente.'

    # Redireccionamos a la página principal tras actualizar el registro
    def get_success_url(self):
        return reverse('CadenaFrio')




















