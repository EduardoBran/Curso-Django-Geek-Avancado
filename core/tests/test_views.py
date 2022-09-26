# serve para criar como se fosse um navegador onde executamos GET, POST, qualquer método Http
from django.test import Client, TestCase
from django.urls import reverse_lazy


class IndexViewTestCase(TestCase):
    def setUp(self):
        # gerando dados para teste
        self.dados = {
            'nome': 'Felicity Jones',
            'email': 'felicity@gmail.com',
            'assunto': 'Um assunto qualquer',
            'mensagem': 'Uma mensagem qualquer'
        }
        self.cliente = Client() # criando o navegador
        
    def test_form_valid(self):
        # aplicando um post para esta rota com dados de self.dados
        request = self.cliente.post(reverse_lazy('index'), data=self.dados) # reverse lazy faz enviar para a rota index

        self.assertEquals(request.status_code, 302) # 302 é para representar o código http ao fazer um post

    def test_form_invalid(self):
        # gerando dados incompletos propositalmente para o formulário ficar inválido
        dados = {
            'nome': 'Felicity Jones',
            'assunto': 'Um assunto qualquer'
        }
        request = self.cliente.post(reverse_lazy('index'), data=dados)
        
        self.assertEquals(request.status_code, 200)
