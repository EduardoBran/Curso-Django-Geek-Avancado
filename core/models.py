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

    servico = models.CharField('Serviço', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    # vai ser transformado em combobox no cadsatro
    icone = models.CharField('Ícone', max_length=20, choices=ICONE_CHOICES)

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
    imagem = StdImageField('Foto', upload_to=get_file_path, variations={
                           'thumb': {'width': 480, 'height': 480, 'crop': True}})
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey(
        Cargo, verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

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

    nome = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Ícone', max_length=25, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Recurso'
        verbose_name_plural = 'Recursos'

    def __str__(self):
        return self.nome
