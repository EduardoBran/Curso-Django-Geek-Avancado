import uuid  # gera valores hexadecimais aleatórios

from django.db import models
from stdimage.models import StdImageField


# necessário para gerar nomes diferentes para as imagens
def get_file_path(_instance, filename):
    extensao = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{extensao}'
    return filename


class Base(models.Model):
    criados = models.DateField(verbose_name='Criação', auto_now_add=True)
    modificado = models.DateField(verbose_name='Atualização', auto_now=True)
    ativo = models.BooleanField(verbose_name='Ativo', default=True)

    class Meta:
        abstract = True


class Servico(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )

    servico = models.CharField(verbose_name='Serviço', max_length=100)
    descricao = models.TextField(verbose_name='Descrição', max_length=200)
    # vai ser transformado em combobox no cadsatro
    icone = models.CharField(verbose_name='Ícone', max_length=20, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico


class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo


class Funcionario(Base):
    imagem = StdImageField(verbose_name='Foto', upload_to=get_file_path, variations={
                           'thumb': {'width': 480, 'height': 480, 'crop': True}})
    nome = models.CharField(verbose_name='Nome', max_length=100)
    cargo = models.ForeignKey(
        Cargo, verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField(verbose_name='Bio', max_length=200)
    facebook = models.CharField(verbose_name='Facebook', max_length=100, default='#')
    twitter = models.CharField(verbose_name='Twitter', max_length=100, default='#')
    instagram = models.CharField(verbose_name='Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome


class Recurso(Base):
    ICONE_CHOICES = (
        ('lni-layers', 'Camadas'),
        ('lni-cog', 'Engrenagem'),
        ('lni-rocket', 'Foguete'),
        ('lni-leaf', 'Folha'),
        ('lni-laptop-phone', 'Laptop'),
        ('lni-mobile', 'Mobile'),
        ('lni-users', 'Usuários'),
    )

    nome = models.CharField(verbose_name='Nome', max_length=100)
    descricao = models.TextField(verbose_name='Descrição', max_length=200)
    icone = models.CharField(verbose_name='Ícone', max_length=25, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Recurso'
        verbose_name_plural = 'Recursos'

    def __str__(self):
        return self.nome

class NamePrice(Base):
    nome = models.CharField(verbose_name='Nomes', max_length=20)
    
    class Meta:
        verbose_name = 'Nome'
        verbose_name_plural = 'Nomes'

    def __str__(self):
        return self.nome
    
class TotalUsuarios(Base):
    total = models.CharField(verbose_name='Total de Usuário', max_length=20)
    
    class Meta:
        verbose_name = 'Total de Usuário'
        verbose_name_plural = 'Total de Usuários'

    def __str__(self):
        return self.total

class TotalArmazenamento(Base):
    total = models.CharField(verbose_name='Total de Armazenamento', max_length=20)
    
    class Meta:
        verbose_name = 'Total de Armazenamento'
        verbose_name_plural = 'Total de Armazenamento'

    def __str__(self):
        return self.total

class Suporte(Base):
    tipo = models.CharField(verbose_name='Tipo de Suporte', max_length=50)
    
    class Meta:
        verbose_name = 'Tipo de Suporte'
        verbose_name_plural = 'Tipos de Suporte'

    def __str__(self):
        return self.tipo


class Atualizacao(Base):
    tipo = models.CharField(verbose_name='Tipo de Suporte', max_length=50)
    
    class Meta:
        verbose_name = 'Tipo de Atualização'
        verbose_name_plural = 'Tipos de Atualizações'

    def __str__(self):
        return self.tipo

class Preco(Base):
    ICONE_CHOICES = (
        ('lni-package', 'Ícone Pro'),
        ('lni-drop', 'Ícone Plus'),
        ('lni-star', 'Ícone Estrela'),
    ) 

    icone = models.CharField(verbose_name='Ícone', max_length=25, choices=ICONE_CHOICES)
    nome = models.ForeignKey(NamePrice, verbose_name='Nome', on_delete=models.CASCADE)
    preco = models.FloatField(verbose_name='Preço', default=0)
    usuarios = models.ForeignKey(TotalUsuarios, verbose_name='Usuários', on_delete=models.CASCADE)
    armazenamento = models.ForeignKey(TotalArmazenamento, verbose_name='Armazenamento', on_delete=models.CASCADE)
    suporte = models.ForeignKey(Suporte, verbose_name='Tipo de Suporte', on_delete=models.CASCADE)
    atualizacao = models.ForeignKey(Atualizacao, verbose_name='Atualização', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Preço'
        verbose_name_plural = 'Preços'

    def __str__(self):
        return str(self.nome)
