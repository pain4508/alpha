"""AlphaCalidad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

###
from AlphaC.views import   ListChileMiniCampoPdf, actualizarRegistroTransEmpaque, eliminarRegistroTransEmpaque, registroNuevoTransEmpaque,  actualizarRegistroTransInvernadero, eliminarRegistroTransInvernadero, registroNuevoTransInvernadero, actualizarRegistroCadenaFrio, eliminarRegistroCadenaFrio, registroNuevoCadenaFrio, actualizarRegistroTomateEmpaque, eliminarRegistroTomateEmpaque, registroNuevoTomateEmpaque, actualizarRegistroTomateCosecha, eliminarRegistroTomateCosecha, registroNuevoTomateCosecha, actualizarRegistroChileMiniEmpaque, eliminarRegistroChileMiniEmpaque, registroNuevoChileMiniEmpaque, actualizarRegistroChileMiniCosecha, eliminarRegistroChileMiniCosecha, registroNuevoChileMiniCosecha, actualizarRegistroEmpacador, eliminarRegistroEmpacador, registroNuevoEmpacador, HomeChileMini, registroNuevoCosechakg, actualizarRegistroInvernaderoKg, eliminarBlockyCosechaKg, registroNuevoCosechaUnidades, eliminarBlockyCosechaUni, actualizarRegistroInvernadero, HomeTomate,HomeTransporte,HomeCadenaFrio,CadenaFrioViews,registroNuevo,TrasnporteEmpaqueViews,TransporteInvernaderoViews,ChileminiEmpaqueViews,TomateCosechaViews,TomateEmpaqueViews, eliminarRegistro, ChileminiViews, actualizarRegistro, InvernaderoViews,BcampokgViews,EmpacadorViews,RecepcionViews, homeViewsBlocky, cerrarViews, iniciarSesionViews, registroUser, homeViews, principalViews, iniciarSesionViews
                           

urlpatterns = [
    
   

    path('admin/', admin.site.urls),
    ############
    #Home
    path('Home/', homeViews, name='home' ),
    #login
    path('login/', iniciarSesionViews, name='login'),
    #registro-
    path('registro/',registroUser, name="registro"),
    
    #Principal dentro de la sesion
    path('principal/', principalViews, name='principal' ),
    #Cerrar sesion
    path('cerrar/', cerrarViews, name='cerrar' ),
    #iniciar sesion
    path('iniciarSesion/', iniciarSesionViews, name='iniciarsesion' ),
   
    #Insertar registros
    path('nuevo/', registroNuevo.as_view(template_name = "AlphaC/cInsertarNuevoCampo.html"), name='nuevo'),

    #Eliminar un registro
    path('eliminar/<int:pk>', eliminarRegistro.as_view(), name='eliminar'), 

     #Mostrar formulario de modificación de registro
    path('editar/<int:pk>', actualizarRegistro.as_view(template_name = "AlphaC/cEditarcampo.html"), name='actualizar'), 


    #url home chile blocky por unidades------------------------------------------------------------------

    path('homeChileBlocky/', homeViewsBlocky, name='homeChileBlocky'),
    #Invernaderos por cosecha unidades
    path('Invernadero/', InvernaderoViews.as_view(template_name = "AlphaC/listarInvernadero.html"), name='Invernadero'),
    #Nuevo Blocky Cosecha
    path('nuevoBlockyCosecha/', registroNuevoCosechaUnidades.as_view(template_name = "AlphaC/insertarFBlockyCUnidades.html"), name='nuevoBlockyCosecha'),
    #Editar 
    path('editarBlockyCosecha/<int:pk>', actualizarRegistroInvernadero.as_view(template_name = "AlphaC/editarFBlockyCUnidades.html"), name='editarBlockyCosecha'), 
    #Eliminar
    path('eliminarBlockyCosechaUni/<int:pk>', eliminarBlockyCosechaUni.as_view(), name='eliminarBlockyCosechaUni'), 

    #campo cosecha rechazo kG-------------------------------------------------------------------------
    path('Bcampokg/', BcampokgViews.as_view(template_name = "AlphaC/Bcampokg.html"), name='Bcampokg'),
   
    #Nuevo Blocky Cosecha kg---------------
    path('nuevoBlockyCosechakg/', registroNuevoCosechakg.as_view(template_name = "AlphaC/insertarFBlockykg.html"), name='nuevoBlockyCosechakg'),
      #Editar 
    path('editarBlockyCosechakg/<int:pk>', actualizarRegistroInvernaderoKg.as_view(template_name = "AlphaC/editarFBlockyCUnidades.html"), name='editarBlockyCosechakg'), 
    #Eliminar
    path('eliminarBlockyCosechakg/<int:pk>', eliminarBlockyCosechaKg.as_view(), name='eliminarBlockyCosechakg'), 


    #empaque empacador------------------------------------------------------------------------------
    path('Empacador/',EmpacadorViews.as_view(template_name = "AlphaC/Bempacador.html"), name='Empacador'),
      #Nuevo 
    path('nuevoEmpacador/', registroNuevoEmpacador.as_view(template_name = "AlphaC/insertarEmpacador.html"), name='nuevoEmpacador'),
      #Editar 
    path('editarEmpacador/<int:pk>', actualizarRegistroEmpacador.as_view(template_name = "AlphaC/editarEmpacador.html"), name='editarEmpacador'), 
    #Eliminar
    path('eliminarEmpacador/<int:pk>', eliminarRegistroEmpacador.as_view(), name='eliminarEmpacador'), 




    #recepcion de calidad------------------------------------------------------------------------------------
    path('Recepcion/',RecepcionViews.as_view(template_name = "AlphaC/Recepcion.html"), name='Recepcion'),


    
    path('editar/<int:pk>', actualizarRegistroInvernadero.as_view(template_name = "AlphaC/editarInvernadero.html"), name='actualizar'),

#CHILE MINI HOME
    #
    path('ChileminiCampoPDF/',ListChileMiniCampoPdf.as_view(), name="ChileminiCampoPDF"),   
    #
    path('HomeChileMini/', HomeChileMini, name='HomeChileMini'),
    path('ChileminiCampo/',ChileminiViews.as_view(template_name = "AlphaC/minicampo.html"), name='ChileminiCampo'),
      #Nuevo 
    path('nuevoChileMiniCosecha/', registroNuevoChileMiniCosecha.as_view(template_name = "AlphaC/insertarFChileMiniCosecha.html"), name='nuevoChileMiniCosecha'),
      #Editar 
    path('editarChileMiniCosecha/<int:pk>', actualizarRegistroChileMiniCosecha.as_view(template_name = "AlphaC/editarChileMiniCosecha.html"), name='editarChileMiniCosecha'), 
    #Eliminar
    path('eliminarChileMiniCosecha/<int:pk>', eliminarRegistroChileMiniCosecha.as_view(), name='eliminarChileMiniCosecha'), 
 
#Chile Mini Empaque--------------------------------------------------------------------------------------
    path('ChileminiEmpaque/',ChileminiEmpaqueViews.as_view(template_name = "AlphaC/miniempaque.html"), name='ChileminiEmpaque'),
    #Nuevo 
    path('nuevoChileMiniEmpaque/', registroNuevoChileMiniEmpaque.as_view(template_name = "AlphaC/insertarChileMiniEmpaque.html"), name='nuevoChileMiniEmpaque'),
    #Editar 
    path('editarChileMiniEmpaque/<int:pk>', actualizarRegistroChileMiniEmpaque.as_view(template_name = "AlphaC/editarChileMiniEmpaque.html"), name='editarChileMiniEmpaque'), 
    #Eliminar
    path('eliminarChileMiniEmpaque/<int:pk>', eliminarRegistroChileMiniEmpaque.as_view(), name='eliminarChileMiniEmpaque'), 


#HOME TOMATE Cosecha
    path('HomeTomate/', HomeTomate, name='HomeTomate'),
    path('TomateCosecha/',TomateCosechaViews.as_view(template_name = "AlphaC/tomatecampo.html"), name='TomateCosecha'),
     #Nuevo 
    path('nuevoTomateCosecha/', registroNuevoTomateCosecha.as_view(template_name = "AlphaC/insertarTomateCosecha.html"), name='nuevoTomateCosecha'),
    #Editar 
    path('editarTomateCosecha/<int:pk>', actualizarRegistroTomateCosecha.as_view(template_name = "AlphaC/editarTomateCosecha.html"), name='editarTomateCosecha'), 
    #Eliminar
    path('eliminarTomateCosecha/<int:pk>', eliminarRegistroTomateCosecha.as_view(), name='eliminarTomateCosecha'), 

    
    #Tomate Empaque
    path('TomateEmpaque/',TomateEmpaqueViews.as_view(template_name = "AlphaC/tomateempaque.html"), name='TomateEmpaque'),
      #Nuevo 
    path('nuevoTomateEmpaque/', registroNuevoTomateEmpaque.as_view(template_name = "AlphaC/insertarTomateEmpaque.html"), name='nuevoTomateEmpaque'),
    #Editar 
    path('editarTomateEmpaque/<int:pk>', actualizarRegistroTomateEmpaque.as_view(template_name = "AlphaC/editarTomateEmpaque.html"), name='editarTomateEmpaque'), 
    #Eliminar
    path('eliminarTomateEmpaque/<int:pk>', eliminarRegistroTomateEmpaque.as_view(), name='eliminarTomateEmpaque'), 

  



#HOME TRANSPORTE
path('HomeTransporte/', HomeTransporte, name='HomeTransporte'),
#Transporte Invernadero---------------------------------------------------------------------------------------
path('TransporteInvernadero/',TransporteInvernaderoViews.as_view(template_name = "AlphaC/transporteinvernadero.html"), name='TransporteInvernadero'),
#Nuevo 
path('nuevoTransInvernandero/', registroNuevoTransInvernadero.as_view(template_name = "AlphaC/insertarTransInvernadero.html"), name='nuevoTransInvernandero'),
#Editar 
path('editarTransInvernandero/<int:pk>', actualizarRegistroTransInvernadero.as_view(template_name = "AlphaC/editarTransInvernandero.html"), name='editarTransInvernandero'), 
#Eliminar
path('eliminarTransInvernandero/<int:pk>', eliminarRegistroTransInvernadero.as_view(), name='eliminarTransInvernandero'), 



#Transporte Empaque---------------------------------------------------------------------------------------
 path('TransporteEmpaque/',TrasnporteEmpaqueViews.as_view(template_name = "AlphaC/transporteempaque.html"), name='TransporteEmpaque'),
#Nuevo 
path('nuevoTransEmpaque/', registroNuevoTransEmpaque.as_view(template_name = "AlphaC/insertarTransEmpaque.html"), name='nuevoTransEmpaque'),
#Editar 
path('editarTransEmpaque/<int:pk>', actualizarRegistroTransEmpaque.as_view(template_name = "AlphaC/editarTransEmpaque.html"), name='editarTransEmpaque'), 
#Eliminar
path('eliminarTransEmpaque/<int:pk>', eliminarRegistroTransEmpaque.as_view(), name='eliminarTransEmpaque'), 





#HOME CADENA FRIO
 path('HomeCadenaFrio/', HomeCadenaFrio, name='HomeCadenaFrio'),
 path('CadenaFrio/',CadenaFrioViews.as_view(template_name = "AlphaC/cadenafrio.html"), name='CadenaFrio'),
#Nuevo 
path('nuevoCadenaFrio/', registroNuevoCadenaFrio.as_view(template_name = "AlphaC/insertarCadenaFrio.html"), name='nuevoCadenaFrio'),
#Editar 
path('editarCadenaFrio/<int:pk>', actualizarRegistroCadenaFrio.as_view(template_name = "AlphaC/editarCadenaFrio.html"), name='editarCadenaFrio'), 
#Eliminar
path('eliminarCadenaFrio/<int:pk>', eliminarRegistroCadenaFrio.as_view(), name='eliminarCadenaFrio'), 





]