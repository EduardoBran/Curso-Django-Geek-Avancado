from core.forms import ContatoForm
from django.test import TestCase

# geralmente é válidado em formulario se após submetido os dados o formulario é válido

class ContatoFormTestCase(TestCase):
    def setUp(self):
        self.nome = 'Felicity Jones'
        self.email = 'felicity@gmail.com'
        self.assunto = 'Um assunto qualquer'
        self.mensagem = 'Uma mensagem qualquer'
        
        self.dados = {
            'nome': self.nome,
            'email': self.email,
            'assunto': self.assunto,
            'mensagem': self.mensagem
        }
        
        self.form = ContatoForm(data=self.dados) # estamos criando a mesma coisa que quando faz isso -> ContatoForm(request.POST)

    def test_sendmail(self):
        # criando dois formularios e verificando se o retorno de ambos são iguais
        
        form1 = ContatoForm(data=self.dados)
        form1.is_valid()
        res1 = form1.send_mail()
        
        # recebendo dados de setUp
        form2 = self.form
        form2.is_valid()
        res2 = form1.send_mail()
        
        self.assertEquals(res1, res2) # o res1 é igual a res2
