from django import forms
from .models import   TransporteEmpaque, TransporteInvernadero, CadenaFrio, CosechaCampokg, CosechaCampo, EmpacadorEmpaque, ChileminiCosecha, ChileminiEmpaque, TomateCosecha, TomateEmpaque
class FormCosechaCampoUni(forms.ModelForm):
    class Meta:
        model = CosechaCampo
        fields = '__all__'

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class FormCosechaCampokg(forms.ModelForm):
    class Meta:
        model = CosechaCampokg
        fields = '__all__'
            
class FormCosechaEmpacador(forms.ModelForm):
    class Meta:
        model = EmpacadorEmpaque
        fields = '__all__'

class FormChileMiniCosecha(forms.ModelForm):
    class Meta:
        model = ChileminiCosecha
        fields = '__all__'
        widgets = {
            
            'fecha': DateTimeInput(attrs={'class': 'form-control'})
            
        }
class FormChileMiniEmpaque(forms.ModelForm):
    class Meta:
        model = ChileminiEmpaque
        fields = '__all__'    

class FormTomateCosecha(forms.ModelForm):
    class Meta:
        model = TomateCosecha
        fields = '__all__' 

class FormTomateEmpaque(forms.ModelForm):
    class Meta:
        model = TomateEmpaque
        fields = '__all__' 

class FormCadenaFrio(forms.ModelForm):
    class Meta:
        model = CadenaFrio
        fields = '__all__' 

class FormTransInvernadero(forms.ModelForm):
    class Meta:
        model = TransporteInvernadero
        fields = '__all__' 

class FormTransEmpaque(forms.ModelForm):
    class Meta:
        model = TransporteEmpaque
        fields = '__all__' 
