from django.test import TestCase


def add_num(num):
    return num + 1

# estrutura que geralmente é padrão do TestCase
class SimplesTestCase(TestCase):
    
    # método que configura o teste -> roda toda vez
    def setUp(self) -> None: 
        print('iniciando o TestCase')
        
        self.numero = 41 # posso usar em qualquer lugar
    
    # testa a unidade de código , SEMPRE iniciar com 'test_'
    def test_add_num(self):
        valor = add_num(self.numero)
        self.assertTrue(valor == 44)
