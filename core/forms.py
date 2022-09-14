from django import forms
from django.core.mail.message import EmailMessage

# Temos o forms.ModelForm que utilizamos caso a gente 
# precise fazer algum cadastro na propria pagina
# Neste projeto o cadastro esta sendo feito todo
# no django administracao e o formulario de email ja esta pronto
# por isso usaremos o forms.Form

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=100)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        #recuperando os dados
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']
        
        conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'
        
        mail = EmailMessage(
            subject=assunto,
            body=conteudo,
            from_email='contato@fusion.com.br',
            to=['contato@fusion.com.br',],
            headers={'Reply To': email}
        )
        mail.send()
