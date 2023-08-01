from django import forms

class CreateNoteForm(forms.Form):
    title = forms.CharField(max_length=120, required=True)
    content = forms.CharField(max_length=300, required=True)

