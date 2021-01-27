from django import forms
from .models import QuranReg, TajweedReg, EgazatReg
 
class MyForm(forms.ModelForm):
  class Meta:
    model = QuranReg
    fields = ["fullname", "mobile_number", "quota"]
    labels = {'fullname': "الاســــــــــم", "mobile_number": "رقم الهاتــف", 'quota': 'نوع البرنامج'}

class MyForm2(forms.ModelForm):
  class Meta:
    model = TajweedReg
    fields = ["fullname", "mobile_number", "quota"]
    labels = {'fullname': "الاســــــــــم", "mobile_number": "رقم الهاتــف", 'quota': 'نوع البرنامج'}

class MyForm3(forms.ModelForm):
  class Meta:
    model = EgazatReg
    fields = ["fullname", "mobile_number", "quota"]
    labels = {'fullname': "الاســــــــم", "mobile_number": "رقم الهاتف", 'quota': 'اسم الاجازة'}