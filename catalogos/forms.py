from django import forms 
from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        
        fields = [
            'descripcion',
            'precio',
            'categoria', 
        ]
        
        labels = {
            'descripcion' : 'Descripción del producto',
            'precio' : 'Precio',
            'categoria': 'Categoria del producto'
        }
        
        widget = {
            'descripcion' : forms.TextInput(),
            'precio': forms.TextInput(),
            'categoria': forms.TextInput()  
        }
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})
       
 
        
        
        
        

'''
    class Meta:
        model = Producto
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})
'''


'''    

    class Meta:
        model = Producto 
        fields = [
            'descripcion',
            'precio',
            'categoria', 
        ]
'''