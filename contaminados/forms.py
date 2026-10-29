from django import forms
from .models import BultoContaminado

class BultoContaminadoForm(forms.ModelForm):
    class Meta:
        model = BultoContaminado
        fields = [
            'codigo', 
            'tipo_material', 
            'subtipo_material', 
            'causa_contaminacion', 
            'fuente_origen', 
            'peso_neto_kg', 
            'observaciones'
        ]
        labels = {
            'codigo': 'Código Único (VARCHAR)',
            'tipo_material': 'Tipo de Material',
            'subtipo_material': 'Subtipo / Grado',
            'causa_contaminacion': 'Causa de Contaminación',
            'fuente_origen': 'Fuente de Origen',
            'peso_neto_kg': 'Peso Neto (kg)',
            'observaciones': 'Observaciones',
        }
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: BMP1321'}),
            'tipo_material': forms.Select(attrs={'class': 'form-select'}),
            'subtipo_material': forms.Select(attrs={'class': 'form-select'}),
        'causa_contaminacion': forms.Select(attrs={'class': 'form-select'}),
        'fuente_origen': forms.TextInput(attrs={
        'class': 'form-control', 
        'placeholder': 'Ej: Rotura, Pallet Dañado, Pallet Pequeño'
    }),
    
        'peso_neto_kg': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': '0.00'}),
        'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Detalles, responsables'}),
}