# file ini untuk setting form html pada tab alternatif
from django import forms
from .models import alternatif #Import fungsi alternatif dari file models
class formtabel(forms.ModelForm):
    class Meta:
        model = alternatif
        fields = ['kodealternatif', 'namaalternatif', 'c1','c2','c3','c4','c5']
        widgets = {
            'kodealternatif': forms.TextInput(attrs={'class':'form-control border focus:border-sky-500 rounded-[4px] w-1/4 h-[2.5rem] px-[.5rem] mt-[.5rem]', 'placeholder':'KODE ALTERNATIF'}),
            'namaalternatif': forms.TextInput(attrs={'class':'form-control border focus:border-sky-500 rounded-[4px] w-1/4 h-[2.5rem] px-[.5rem] mt-[.5rem]', 'placeholder':'NAMA ALTERNATIF'}),
            'c1': forms.TextInput(attrs={'class':'form-control border focus:border-sky-500 rounded-[4px] w-3/4 h-[2.5rem] px-[.5rem] mt-[.5rem]', 'placeholder':'Rp.', 'type':"number", }),
            'c2': forms.Select(attrs={'class':'form-control border focus:border-sky-500 rounded-[4px] w-3/4 h-[2.5rem] px-[.5rem] mt-[.5rem]', 'placeholder':'℃'}),
            # 'c2': forms.TextInput(attrs={'class':'form-control border focus:border-sky-500 rounded-[4px] w-3/4 h-[2.5rem] px-[.5rem] mt-[.5rem]', 'placeholder':'prosentase (%)'}),
            'c3': forms.Select(attrs={'class':'form-control border focus:border-sky-500 rounded-[4px] w-3/4 h-[2.5rem] px-[.5rem] mt-[.5rem]', 'placeholder':'Transportasi Publik'}),
            'c4': forms.Select(attrs={'class':'form-control border focus:border-sky-500 rounded-[4px] w-3/4 h-[2.5rem] px-[.5rem] mt-[.5rem]', 'placeholder':'Tingkat Kriminalitas'}),
            'c5': forms.Select(attrs={'class':'form-control border focus:border-sky-500 rounded-[4px] w-3/4 h-[2.5rem] px-[.5rem] mt-[.5rem]', 'placeholder':'Biaya Pengurusan Visa'}),            
        }
        labels ={
            'kodealternatif':'KODE ALTERNATIF',
            'namaalternatif':'NAMA',
            'c1':'Biaya Perjalanan',
            'c2':'Suhu Harian ',
            'c3':'Transportasi Public',
            'c4':'Tingkat Kriminalitas',
            'c5':'Biaya Pengurusan Visa',
        }
    