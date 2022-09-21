import uuid  # está no metodo get_file_path

from core.models import get_file_path
from django.test import TestCase
from model_mommy import mommy


# vamos testar o get_file_path necessário para gerar nomes diferentes para as imagens
class GetFilePathTestCase(TestCase):
    
    # método que configura o teste -> roda toda vez
    def setUp(self):
        # criando arquivo que gera uma string na mesma estrutura/formato que está na funcao originarl em models que fica disponivel pra gente
        self.filename = f'{uuid.uuid4()}.png' 
    
    
    # criando o teste
    def test_get_file_path(self):
        arquivo = get_file_path(None, 'teste.png') # None é o parâmetro _instance da funcao original

        # fazendo a verificação
        # vendo se a função está gerando o nome e a quantidade de caracteres correto
        self.assertTrue(len(arquivo), len(self.filename))


# testando as funções __str__
class ServicoTestCase(TestCase):
    # quando for executar, o Mommy cria um serviço (objeto) para testar    
    def setUp(self):
        self.servico = mommy.make('Servico')

    # como a funcao original retorna o servico, foi criado um servico novo com o mommy make
    # e estamos testando para ver se ele é igual o self.servico
    def test_str(self):
        self.assertEquals(str(self.servico), self.servico.servico)
        
        
class CargoTestCase(TestCase):        
    def setUp(self):
        self.cargo = mommy.make('Cargo')
    
    def test_str(self):
        self.assertEquals(str(self.cargo), self.cargo.cargo)


class FuncionarioTestCase(TestCase):
    def setUp(self):
        self.funcionario = mommy.make('Funcionario')
    
    def test_str(self):
        self.assertEquals(str(self.funcionario), self.funcionario.nome)

class RecursoTestCase(TestCase):
    def setUp(self):
        self.recurso = mommy.make('Recurso')
    
    def test_str(self):
        self.assertEquals(str(self.recurso), self.recurso.nome)


class NamePriceTestCase(TestCase):
    def setUp(self):
        self.namePrice = mommy.make('NamePrice')
    
    def test_str(self):
        self.assertEquals(str(self.namePrice), self.namePrice.nome)
            
            
class TotalUsuariosTestCase(TestCase):
    def setUp(self):
        self.totalUsuarios = mommy.make('TotalUsuarios')

    def test_str(self):
        self.assertEquals(str(self.totalUsuarios), self.totalUsuarios.total)

class TotalArmazenamentoTestCase(TestCase):
    def setUp(self):
        self.totalArmazenamento = mommy.make('TotalArmazenamento')

    def test_str(self):
        self.assertEquals(str(self.totalArmazenamento), self.totalArmazenamento.total)
        

class SuporteTestCase(TestCase):
    def setUp(self):
        self.suporte = mommy.make('Suporte')

    def test_str(self):
        self.assertEquals(str(self.suporte), self.suporte.tipo)        
    

class AtualizacaoTestCase(TestCase):
    def setUp(self):
        self.atualizacao = mommy.make('Atualizacao')

    def test_str(self):
        self.assertEquals(str(self.atualizacao), self.atualizacao.tipo)        

class PrecoTestCase(TestCase):
    def setUp(self):
        self.nome = mommy.make('Preco')

    def test_str(self):
        self.assertEquals(str(self.nome), self.nome.nome)  
