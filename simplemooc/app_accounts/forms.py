from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):

    email = forms.EmailField(label='E-mail')
    
    def clean_email(self): #Verifica se o email digitado já existe no banco de dados
        email_x = self.cleaned_data['email'] #email digitado pelo usuário
        if User.objects.filter(email=email_x).exists(): #Se existir, enviar mensagem de erro
            raise forms.ValidationError('Já existe usuário com este email')
        return email_x #Se não, matenha o email no campo normalmente
    
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
    