from django import forms

class InputForm(forms.Form):
    Cp_value = forms.DecimalField(min_value=0)
    Thalach_value = forms.DecimalField(min_value=0)
    oldpeak_value = forms.DecimalField(min_value=0)
    exang_value = forms.DecimalField(min_value=0)
    slope_value = forms.DecimalField(min_value=0)
    chol_value = forms.DecimalField(min_value=0)