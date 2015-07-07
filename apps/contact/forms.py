from django import forms

class ContactForm(forms.Form):
    author_name = forms.CharField(widget=forms.TextInput(), required=True)
    email = forms.EmailField(widget=forms.TextInput(), required=True)
    message = forms.CharField(widget=forms.TextInput(), required=True)




