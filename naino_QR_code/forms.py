from django import forms
 
class qr_code(forms.Form):
    qr_code_name = forms.CharField(
        max_length=100, 
        label='QR_code_name',
        widget=forms.TextInput(attrs={
            'class':'form-control' ,
            'placeholder':'Enter the name of the QR code'
        })
        )
    url = forms.URLField(
        max_length=200, 
        label='Link', 
        widget=forms.TextInput(attrs={
            'class':'form-control' ,
            'placeholder':'Enter the Link here'
        })
        )



 
