from django import forms
# from . models import Add_Rainfall

class TestForm(forms.Form):
    '''
    classs that creates the Rainfall addition form
    ''' 
    name = forms.CharField(label='City',max_length = 30)
    number = forms.IntegerField(label = 'Amount of Rainfall(mm)') 