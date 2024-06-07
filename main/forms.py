from django import forms

class ContatoForm(forms.Form):
    assunto = forms.CharField(label="Assunto:", max_length=100)
    mensagem = forms.CharField(label="Mensagem:", widget=forms.Textarea)
    email = forms.EmailField(label="E-mail:" )
    me_copiar = forms.BooleanField(label="Me Copiar")

    