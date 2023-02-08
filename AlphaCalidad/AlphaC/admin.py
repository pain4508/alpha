from django.contrib import admin
from .models import Invernadero, ChileminiEmpaque,CosechaCampokg, CosechaCampo,TransporteInvernadero, Variedad ,Variedad1,Variedad2,Variedad3, EmpacadorEmpaque , CalidadRecepcion, Tallas, ChileminiCosecha,CadenaFrio,TransporteEmpaque

# Register your models here.

admin.site.register(Invernadero)
admin.site.register(CosechaCampokg)
admin.site.register(CosechaCampo)

admin.site.register(Variedad)
admin.site.register(Variedad1)
admin.site.register(Variedad2)
admin.site.register(Variedad3)

admin.site.register(EmpacadorEmpaque)
admin.site.register(CalidadRecepcion)
admin.site.register(Tallas)
admin.site.register(ChileminiCosecha)
admin.site.register(CadenaFrio)
admin.site.register(TransporteEmpaque)
admin.site.register(TransporteInvernadero)
admin.site.register(ChileminiEmpaque)




