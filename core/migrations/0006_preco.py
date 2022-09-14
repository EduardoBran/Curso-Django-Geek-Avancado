# Generated by Django 4.1 on 2022-09-14 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_recurso_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('icone', models.CharField(choices=[('lni-package', 'Ícone Pro'), ('lni-drop', 'Ícone Plus'), ('lni-star', 'Ícone Estrela')], max_length=25, verbose_name='Ícone')),
                ('nome', models.CharField(max_length=20, verbose_name='Nome')),
                ('preco', models.FloatField(default=0, verbose_name='Preço')),
                ('usuarios', models.IntegerField(verbose_name='Usuários')),
                ('armazenamento', models.IntegerField(verbose_name='Armazenamento')),
                ('suporte', models.CharField(max_length=50, verbose_name='Suporte')),
                ('atualizacao', models.CharField(max_length=30, verbose_name='Atualizações')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
