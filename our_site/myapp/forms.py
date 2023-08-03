from django import forms

from myapp.models import Note

class CreateNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ("title", "content")
