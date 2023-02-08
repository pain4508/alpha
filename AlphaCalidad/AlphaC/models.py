from django.db import models


# Create your models here.
class danosCampoCosecha(models.Model):
    idDanos = models.AutoField(primary_key=True)
    maduracion = models.DecimalField(db_column='Maduracion', max_digits=19, decimal_places=2)  # Field name made lowercase.
    flacido = models.DecimalField(db_column='Flacido', max_digits=19, decimal_places=2)  # Field name made lowercase.
    blossom = models.DecimalField(db_column='Blossom', max_digits=19, decimal_places=2)  # Field name made lowercase.
    agujero = models.DecimalField(db_column='Agujero', max_digits=19, decimal_places=2)  # Field name made lowercase.
    tijera = models.DecimalField(db_column='Tijera', max_digits=19, decimal_places=2)  # Field name made lowercase.
    cortependulo = models.DecimalField(db_column='CortePendulo', max_digits=19, decimal_places=2)  # Field name made lowercase.
    golpes = models.DecimalField(db_column='Golpes', max_digits=19, decimal_places=2)  # Field name made lowercase.
    dañomecanico = models.DecimalField(db_column='DañoMecanico', max_digits=19, decimal_places=2)  # Field name made lowercase.
    gusano = models.DecimalField(db_column='Gusano', max_digits=19, decimal_places=2)  # Field name made lowercase.
    cracking = models.DecimalField(db_column='Cracking', max_digits=19, decimal_places=2)  # Field name made lowercase.
    cicatriz = models.DecimalField(db_column='Cicatriz', max_digits=19, decimal_places=2)  # Field name made lowercase.
    cortenavaja = models.DecimalField(db_column='CorteNavaja', max_digits=19, decimal_places=2)  # Field name made lowercase.
    hongo = models.DecimalField(db_column='Hongo', max_digits=19, decimal_places=2)  # Field name made lowercase.
    grillo = models.DecimalField(db_column='Grillo', max_digits=19, decimal_places=2)  # Field name made lowercase.
    silverado = models.DecimalField(db_column='Silverado', max_digits=19, decimal_places=2)  # Field name made lowercase.
    deforme = models.DecimalField(max_digits=19, decimal_places=2)

class Capilla(models.Model):
    idcapilla = models.AutoField(db_column='IdCapilla', primary_key=True)  # Field name made lowercase.
    numerocapilla = models.IntegerField(db_column='NumeroCapilla')  # Field name made lowercase.

    class Meta:
        
        db_table = 'Capilla'

class Tallas(models.Model):
    idtalla = models.AutoField(db_column='IdTalla', primary_key=True)  # Field name made lowercase.
    talla = models.CharField(db_column='Talla', max_length=5, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'Tallas'

class Invernadero(models.Model):
    idinvernadero = models.AutoField(db_column='IdInvernadero', primary_key=True)  # Field name made lowercase.
    nombreinvernadero = models.CharField(db_column='NombreInvernadero', max_length=20, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.

    class Meta:
        
        db_table = 'Invernadero'
        
        
    def __str__(self):
        return self.nombreinvernadero

class Variedad1(models.Model):
    idvariedad1 = models.AutoField(db_column='IdVariedad1', primary_key=True)  # Field name made lowercase.
    nombrevariedad1 = models.CharField(db_column='NombreVariedad1', max_length=20, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.

    class Meta:
     
        db_table = 'Variedad1'

class Variedad2(models.Model):
    idvariedad2 = models.AutoField(db_column='IdVariedad2', primary_key=True)  # Field name made lowercase.
    nombrevariedad = models.CharField(db_column='NombreVariedad', max_length=20, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.

    class Meta:
        
        db_table = 'Variedad2'

class Variedad3(models.Model):
    idvariedad3 = models.AutoField(db_column='IdVariedad3', primary_key=True)  # Field name made lowercase.
    nombrevariedad = models.CharField(db_column='NombreVariedad', max_length=20, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.

    class Meta:
        
        db_table = 'Variedad3'
    
    def __str__(self):
        return self.nombrevariedad

class Variedad(models.Model):
    idvariedad = models.AutoField(db_column='IdVariedad', primary_key=True)  # Field name made lowercase.
    nombrevariedad = models.CharField(db_column='NombreVariedad', max_length=20, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.

    class Meta:
       
        db_table = 'variedad'

class CadenaFrio(models.Model):
    idcadena = models.AutoField(db_column='Idcadena', primary_key=True)  # Field name made lowercase.
    fecha = models.DateField()
    hora = models.TimeField() 
    idvariedad = models.ForeignKey(Variedad, on_delete=models.CASCADE, db_column='IdVariedad')  # Field name made lowercase.
    idinvernadero = models.ForeignKey(Invernadero, on_delete=models.CASCADE, db_column='IdInvernadero')  # Field name made lowercase.
    preenfriamiento = models.DecimalField(db_column='Preenfriamiento', max_digits=19, decimal_places=2)  # Field name made lowercase.
    elevadorcesta = models.DecimalField(db_column='ElevadorCesta', max_digits=19, decimal_places=2)  # Field name made lowercase.
    clasificadoratalla = models.DecimalField(db_column='ClasificadoraTalla', max_digits=19, decimal_places=2)  # Field name made lowercase.
    tolva = models.DecimalField(db_column='Tolva', max_digits=19, decimal_places=2)  # Field name made lowercase.
    pallets = models.DecimalField(db_column='Pallets', max_digits=19, decimal_places=2)  # Field name made lowercase.
    almacenamiento = models.DecimalField(max_digits=19, decimal_places=2)
    carga = models.DecimalField(db_column='Carga', max_digits=19, decimal_places=2)  # Field name made lowercase.

    class Meta:
        
        db_table = 'Cadena_frio'

class EmpacadorEmpaque(models.Model):
    idempacador = models.AutoField(db_column='IdEmpacador', primary_key=True)  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha')  # Field name made lowercase.
    hora = models.DateField()
    nombre_auxiliar = models.CharField(db_column='nombre_Auxiliar', max_length=25, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    codigo = models.IntegerField()
    idvariedad1 = models.ForeignKey(Variedad1, on_delete=models.CASCADE, db_column='IdVariedad1')  # Field name made lowercase.
    revision = models.IntegerField()
    idtalla = models.ForeignKey(Tallas, on_delete=models.CASCADE, db_column='IdTalla')  # Field name made lowercase.
    clasificacion = models.IntegerField()
    #totalevaluados = models.IntegerField(db_column='TotalEvaluados')  #Nivel Programacionm
    #totaldañados = models.IntegerField(db_column='TotalDañados')  # Nivel Programacion
    maduracion = models.DecimalField(db_column='Maduracion', max_digits=19, decimal_places=2)  # Field name made lowercase.
    flacido = models.DecimalField(db_column='Flacido', max_digits=19, decimal_places=2)  # Field name made lowercase.
    blossom = models.DecimalField(db_column='Blossom', max_digits=19, decimal_places=2)  # Field name made lowercase.
    agujero = models.DecimalField(db_column='Agujero', max_digits=19, decimal_places=2)  # Field name made lowercase.
    tijera = models.DecimalField(db_column='Tijera', max_digits=19, decimal_places=2)  # Field name made lowercase.
    cortependulo = models.DecimalField(db_column='CortePendulo', max_digits=19, decimal_places=2)  # Field name made lowercase.
    golpes = models.DecimalField(db_column='Golpes', max_digits=19, decimal_places=2)  # Field name made lowercase.
    dañomecanico = models.DecimalField(db_column='DañoMecanico', max_digits=19, decimal_places=2)  # Field name made lowercase.
    gusano = models.DecimalField(db_column='Gusano', max_digits=19, decimal_places=2)  # Field name made lowercase.
    sobremaduro  = models.DecimalField(db_column='sobremaduro', max_digits=19, decimal_places=2)  # Field name made lowercase.  
    cracking = models.DecimalField(db_column='Cracking', max_digits=19, decimal_places=2)  # Field name made lowercase.
    cicatriz = models.DecimalField(db_column='Cicatriz', max_digits=19, decimal_places=2)  # Field name made lowercase.
    cortenavaja = models.DecimalField(db_column='CorteNavaja', max_digits=19, decimal_places=2)  # Field name made lowercase.
    hongo = models.DecimalField(db_column='Hongo', max_digits=19, decimal_places=2)  # Field name made lowercase.
    grillo = models.DecimalField(db_column='Grillo', max_digits=19, decimal_places=2)  # Field name made lowercase.
    silverado = models.DecimalField(db_column='Silverado', max_digits=19, decimal_places=2)  # Field name made lowercase.
    deforme = models.DecimalField(max_digits=19, decimal_places=2)
    
    class Meta:
        
        db_table = 'Empacador_Empaque'



class ChileminiEmpaque(models.Model):
    idchile_mini2 = models.AutoField(db_column='IdChile_Mini2', primary_key=True)  # Field name made lowercase.
    fecha = models.DateField()
    idinvernadero = models.ForeignKey(Invernadero, db_column='IdInvernadero', on_delete=models.CASCADE, null=True)  # Field name made lowercase.
    idvariedad3 = models.ForeignKey(Variedad3, db_column='IdVariedad3', on_delete=models.CASCADE)  # Field name made lowercase.
    iodtalla = models.ForeignKey(Tallas, db_column='IdTalla', on_delete=models.CASCADE)  # Field name made lowercase.
    kilogramo = models.DecimalField(max_digits=19, decimal_places=2)
    cajas_cosechas = models.DecimalField(max_digits=19, decimal_places=2)
    #kg_caja = models.DecimalField(max_digits=19, decimal_places=2) Nivel Programacion
    calizdañado = models.DecimalField(max_digits=19, decimal_places=2)
    
    mecanico = models.DecimalField(max_digits=19, decimal_places=2)
    gusano = models.DecimalField(max_digits=19, decimal_places=2)
    grado_optimo = models.DecimalField(max_digits=19, decimal_places=2)
    
    silverado = models.DecimalField(max_digits=19, decimal_places=2)
    materiaextraña = models.DecimalField(max_digits=19, decimal_places=2)
    
    sobremaduro = models.DecimalField(max_digits=19, decimal_places=2)
    blossom = models.DecimalField(max_digits=19, decimal_places=2)
    cracking = models.DecimalField(max_digits=19, decimal_places=2)
    deforme = models.DecimalField(max_digits=19, decimal_places=2)
    flacido = models.DecimalField(max_digits=19, decimal_places=2)
    hongo = models.DecimalField(max_digits=19, decimal_places=2)
    podrido = models.DecimalField(max_digits=19, decimal_places=2)
    tamaño = models.DecimalField(max_digits=19, decimal_places=2)
    
    class Meta:
        
        db_table = 'ChileMini_Empaque'

class ChileminiCosecha(models.Model):
    idchile_mini = models.AutoField(db_column='IdChile_Mini', primary_key=True)  # Field name made lowercase.
    fecha = models.DateField()
    hora = models.TimeField()
    idinvernadero = models.ForeignKey(Invernadero, db_column='IdInvernadero', on_delete=models.CASCADE )  # Field name made lowercase.
    idvariedad3 = models.ForeignKey(Variedad3, db_column='IdVariedad3', on_delete=models.CASCADE)  # Field name made lowercase.
    kilogramo = models.DecimalField(max_digits=5, decimal_places=2)
    cajas_cosechas = models.DecimalField(max_digits=5, decimal_places=2)
    #kg_caja = models.DecimalField(max_digits=19, decimal_places=2) Nivel Programacion
    calizdanado = models.DecimalField(max_digits=19, decimal_places=2)
    mecanico = models.DecimalField(max_digits=19, decimal_places=2)
    gusano = models.DecimalField(max_digits=19, decimal_places=2)
    grado_optimo = models.DecimalField(max_digits=19, decimal_places=2)
    
    silverado = models.DecimalField(max_digits=19, decimal_places=2)
    materiaextrana = models.DecimalField(max_digits=19, decimal_places=2)
    
    sobremaduro = models.DecimalField(max_digits=19, decimal_places=2)
    blossom = models.DecimalField(max_digits=19, decimal_places=2)
    cracking = models.DecimalField(max_digits=19, decimal_places=2)
    deforme = models.DecimalField(max_digits=19, decimal_places=2)
    flacido = models.DecimalField(max_digits=19, decimal_places=2)
    hongo = models.DecimalField(max_digits=19, decimal_places=2)
    podrido = models.DecimalField(max_digits=19, decimal_places=2)
    tamano = models.DecimalField(max_digits=19, decimal_places=2)
    temperatura = models.DecimalField(db_column='temperatura', max_digits=19, decimal_places=2)  # Field name made lowercase.

    class Meta:
        
        db_table = 'ChileMini_cosecha'

class CosechaCampo(models.Model): 
    idcosecha_campo = models.AutoField(db_column='IdCosecha_Campo', primary_key=True)  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha')  # Field name made lowercase.
    hora = models.TimeField()
    nombreauxliar = models.CharField(db_column='NombreAuxliar', max_length=25, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    idinvernadero = models.ForeignKey(Invernadero, on_delete=models.CASCADE, db_column='IdInvernadero')  # Field name made lowercase.
    idcapilla = models.ForeignKey(Capilla,on_delete=models.CASCADE , db_column='IdCapilla')  # Field name made lowercase.
    idvariedad1 = models.ForeignKey(Variedad1, on_delete=models.CASCADE, db_column='IdVariedad1')  # Field name made lowercase.
    aptos = models.DecimalField(db_column='Aptos', max_digits=5, decimal_places=2)  # Field name made lowercase.
    dañados = models.IntegerField(db_column='Dañados')  # Field name made lowercase.

    
    class Meta:
        
        db_table = 'Cosecha_Campo'

class CosechaCampokg(models.Model): 
    idcampokg = models.AutoField(db_column='IdCampoKg', primary_key=True)  # Field name made lowercase.
    fecha = models.DateField()
    hora = models.TimeField()
    idinvernadero = models.IntegerField(db_column='IdInvernadero')  # Field name made lowercase.
    idvariedad1 = models.IntegerField(db_column='IdVariedad1')  # Field name made lowercase.
    kilogramo = models.DecimalField(db_column='Kilogramo',max_digits=5, decimal_places=2)
    cajas_cosechas = models.DecimalField(max_digits=5, decimal_places=2)
    #kg_caja = models.DecimalField(max_digits=5, decimal_places=2) Nivel Programacion
    maduracion = models.DecimalField(db_column='Maduracion', max_digits=19, decimal_places=2)  # Field name made lowercase.
    flacido = models.DecimalField(db_column='Flacido', max_digits=19, decimal_places=2)  # Field name made lowercase.
    blossom = models.DecimalField(db_column='Blossom', max_digits=19, decimal_places=2)  # Field name made lowercase.
    agujero = models.DecimalField(db_column='Agujero', max_digits=19, decimal_places=2)  # Field name made lowercase.
    tijera = models.DecimalField(db_column='Tijera', max_digits=19, decimal_places=2)  # Field name made lowercase.
    sol = models.DecimalField(max_digits=19, decimal_places=2)
    inferior = models.DecimalField(max_digits=19, decimal_places=2)
    podrido = models.DecimalField(max_digits=19, decimal_places=2)
    cortependulo = models.DecimalField(db_column='CortePendulo', max_digits=19, decimal_places=2)  # Field name made lowercase.
    golpes = models.DecimalField(db_column='Golpes', max_digits=19, decimal_places=2)  # Field name made lowercase.
    dañomecanico = models.DecimalField(db_column='DañoMecanico', max_digits=19, decimal_places=2)  # Field name made lowercase.
    gusano = models.DecimalField(db_column='Gusano', max_digits=19, decimal_places=2)  # Field name made lowercase.
    cracking = models.DecimalField(db_column='Cracking', max_digits=19, decimal_places=2)  # Field name made lowercase.
    cicatriz = models.DecimalField(db_column='Cicatriz', max_digits=19, decimal_places=2)  # Field name made lowercase.
    cortenavaja = models.DecimalField(db_column='CorteNavaja', max_digits=19, decimal_places=2)  # Field name made lowercase.
    hongo = models.DecimalField(db_column='Hongo', max_digits=19, decimal_places=2)  # Field name made lowercase.
    grillo = models.DecimalField(db_column='Grillo', max_digits=19, decimal_places=2)  # Field name made lowercase.
    silverado = models.DecimalField(db_column='Silverado', max_digits=19, decimal_places=2)  # Field name made lowercase.
    deforme = models.DecimalField(max_digits=19, decimal_places=2)
    tamaño_pequeño = models.DecimalField(max_digits=19, decimal_places=2)
    temperatura = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        
        db_table = 'Cosecha_CampoKg'
        
class CalidadRecepcion(models.Model):
    idcalidad_recepcion = models.AutoField(db_column='IdCalidad_Recepcion', primary_key=True)  # Field name made lowercase.
    fecha = models.DateField()
    hora = models.TimeField()
    nombre_auxiliar = models.CharField(db_column='nombre_Auxiliar', max_length=25, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    idinvernadero = models.ForeignKey(Invernadero, on_delete=models.CASCADE, db_column='IdInvernadero')  # Field name made lowercase.
    idvariedad1 = models.ForeignKey(Variedad1, on_delete=models.CASCADE, db_column='IdVariedad1')  # Field name made lowercase.
    kilogramo = models.DecimalField(max_digits=5, decimal_places=2)
    cajas_cosechas = models.DecimalField(max_digits=5, decimal_places=2)
    #kg_caja = models.DecimalField(max_digits=5, decimal_places=2) Nivel Programacion
    cortenavaja = models.DecimalField(db_column='cortenavaja', max_digits=5, decimal_places=2)  # Field name made lowercase.
    
    gradomaduracion = models.DecimalField(db_column='GradoMaduracion', max_digits=5, decimal_places=2)  # Field name made lowercase.
    flacido = models.DecimalField(db_column='Flacido', max_digits=19, decimal_places=2)  # Field name made lowercase.
    blossom = models.DecimalField(db_column='Blossom', max_digits=19, decimal_places=2)  # Field name made lowercase.
    agujero = models.DecimalField(db_column='Agujero', max_digits=19, decimal_places=2)  # Field name made lowercase.
    sobremaduro = models.DecimalField(db_column='sobremaduro', max_digits=19, decimal_places=2)  # Field name made lowercase.
    quemadosol = models.DecimalField(db_column='quemadosol', max_digits=19, decimal_places=2)  # Field name made lowercase.
    dañomecanico = models.DecimalField(db_column='DañoMecanico', max_digits=19, decimal_places=2)  # Field name made lowercase.
    gusano = models.DecimalField(db_column='Gusano', max_digits=19, decimal_places=2)  # Field name made lowercase.
    cracking = models.DecimalField(db_column='Cracking', max_digits=19, decimal_places=2)  # Field name made lowercase.
    cicatriz = models.DecimalField(db_column='Cicatriz', max_digits=19, decimal_places=2)  # Field name made lowercase.
    podrido = models.DecimalField(db_column='podrido', max_digits=19, decimal_places=2)  # Field name made lowercase.
    hongo = models.DecimalField(db_column='Hongo', max_digits=19, decimal_places=2)  # Field name made lowercase.
    grillo = models.DecimalField(db_column='Grillo', max_digits=19, decimal_places=2)  # Field name made lowercase.
    silverado = models.DecimalField(db_column='Silverado', max_digits=19, decimal_places=2)  # Field name made lowercase.
    deforme = models.DecimalField(db_column='deforme', max_digits=19, decimal_places=2)
    tamaño_pequeño = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        
        db_table = 'Calidad_Recepcion'





class TomateCosecha(models.Model):
    idtomate_cosecha = models.AutoField(db_column='IdTomate_Cosecha', primary_key=True)  # Field name made lowercase.
    fecha = models.DateField()
    hora = models.TimeField()
    idinvernadero = models.ForeignKey(Invernadero, on_delete=models.CASCADE, db_column='IdInvernadero')  # Field name made lowercase.
    idvariedad2 = models.ForeignKey(Variedad2, on_delete=models.CASCADE, db_column='IdVariedad2')  # Field name made lowercase.
    kilogramo = models.DecimalField(max_digits=5, decimal_places=2)
    cajas_cosechas = models.DecimalField(max_digits=19, decimal_places=2)
    #kg_caja = models.DecimalField(max_digits=19, decimal_places=2) Nivel Programacion
    mecanico = models.DecimalField(max_digits=19, decimal_places=2)
    gusano = models.DecimalField(max_digits=19, decimal_places=2)
    grado_optimo = models.DecimalField(max_digits=19, decimal_places=2)
    materia = models.DecimalField(max_digits=19, decimal_places=2)
    silverado = models.DecimalField(max_digits=19, decimal_places=2)
    sobre = models.DecimalField(max_digits=19, decimal_places=2)
    blossom = models.DecimalField(max_digits=19, decimal_places=2)
    cracking = models.DecimalField(max_digits=19, decimal_places=2)
    deforme = models.DecimalField(max_digits=19, decimal_places=2)
    flacido = models.DecimalField(max_digits=19, decimal_places=2)
    hongo = models.DecimalField(max_digits=19, decimal_places=2)
    podrido = models.DecimalField(max_digits=19, decimal_places=2)
    tamaño = models.DecimalField(max_digits=19, decimal_places=2)
    temperatura = models.DecimalField(max_digits=19, decimal_places=2)
    class Meta:
      
        db_table = 'Tomate_Cosecha'

class TomateEmpaque(models.Model):
    idtomate_empaque = models.AutoField(db_column='IdTomate_Empaque', primary_key=True)  # Field name made lowercase.
    fecha = models.DateField()
    idinvernadero = models.ForeignKey(Invernadero, on_delete=models.CASCADE, db_column='IdInvernadero')  # Field name made lowercase.
    idvariedad2 = models.ForeignKey(Variedad2, on_delete=models.CASCADE, db_column='IdVariedad2')  # Field name made lowercase.
    idtalla = models.ForeignKey(Tallas, on_delete=models.CASCADE, db_column='IdTalla')  # Field name made lowercase.
    kilogramo = models.DecimalField(max_digits=19, decimal_places=2)
    cajas_cosechas = models.DecimalField(max_digits=19, decimal_places=2)
    #kg_caja = models.DecimalField(max_digits=19, decimal_places=2)  Nivel Programacion
    mecanico = models.DecimalField(max_digits=19, decimal_places=2)
    gusano = models.DecimalField(max_digits=19, decimal_places=2)
    grado_optimo = models.DecimalField(max_digits=19, decimal_places=2)
    materia = models.DecimalField(max_digits=19, decimal_places=2)
    silverado = models.DecimalField(max_digits=19, decimal_places=2)
    sobre = models.DecimalField(max_digits=19, decimal_places=2)
    blossom = models.DecimalField(max_digits=19, decimal_places=2)
    cracking = models.DecimalField(max_digits=19, decimal_places=2)
    deforme = models.DecimalField(max_digits=19, decimal_places=2)
    flacido = models.DecimalField(max_digits=19, decimal_places=2)
    hongo = models.DecimalField(max_digits=19, decimal_places=2)
    podrido = models.DecimalField(max_digits=19, decimal_places=2)
    tamaño = models.DecimalField(max_digits=19, decimal_places=2)
    
    class Meta:
        
        db_table = 'Tomate_Empaque'

class TransporteEmpaque(models.Model):
    idtransempaque = models.IntegerField(db_column='IdTransEmpaque', primary_key=True)  # Field name made lowercase.
    fecha = models.DateField()
    nombre_conductor = models.CharField(max_length=25, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    placa_vehiculo = models.CharField(db_column='Placa_Vehiculo', max_length=8, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    hora_llegada = models.TimeField()
    hora_descarga = models.TimeField()
    peso_descargadochile = models.DecimalField(max_digits=19, decimal_places=2)
    peso_descargadotomate = models.DecimalField(max_digits=19, decimal_places=2)
    hora_salida = models.TimeField()
    temperatura = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
       
        db_table = 'Transporte_Empaque'

class TransporteInvernadero(models.Model):
    idtransinver = models.IntegerField(db_column='IdTransInver', primary_key=True)  # Field name made lowercase.
    fecha = models.DateField()
    nombre_conductor = models.CharField(max_length=25, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    placa_vehiculo = models.CharField(db_column='Placa_Vehiculo', max_length=8, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    hora_llegada = models.TimeField()
    hora_carga = models.TimeField()
    peso_cargadochile = models.DecimalField(max_digits=19, decimal_places=2)
    peso_cargadotomate = models.DecimalField(max_digits=19, decimal_places=2)
    tiempo_salida = models.TimeField()
    temperatura = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        
        db_table = 'Transporte_Invernadero'


