from django import forms
from .models import Pemesanan, Barang

class BarangDatangForm(forms.ModelForm):

    jumlah_rusak = forms.IntegerField(
        min_value=0,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'min': 0
        })
    )

    class Meta:
        model = Pemesanan
        fields = [
            'jumlah_datang',
            'jumlah_rusak',
            'keterangan'
        ]

        widgets = {
              
              'jumlah_datang': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

            'keterangan': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': ''
            }),
        }

class BarangForm(forms.ModelForm):

    class Meta:
        model = Barang

        fields = [
            'nama_barang',
            'stock',
            'harga',
        ]

        widgets = {

            'nama_barang': forms.TextInput(attrs={
                'class': 'form-control'
            }),


            'stock': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0
            }),

            'harga': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0
            }),
        }
