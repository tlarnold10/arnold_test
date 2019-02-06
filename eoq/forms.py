from django import forms

class UploadFileForm(forms.Form):
	file = forms.FileField()
	holding_cost = forms.CharField()
	reorder = forms.CharField()
