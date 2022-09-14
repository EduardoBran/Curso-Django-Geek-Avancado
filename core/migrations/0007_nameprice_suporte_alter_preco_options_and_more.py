# Generated by Django 4.1 on 2022-09-14 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_preco'),
    ]

    operations = [
        migrations.CreateModel(
            name='NamePrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('nome', models.CharField(max_length=20, verbose_name='Nomes')),
            ],
            options={
                'verbose_name': 'Nome',
                'verbose_name_plural': 'Nomes',
            },
        ),
        migrations.CreateModel(
            name='Suporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('tipo', models.CharField(max_length=50, verbose_name='Tipo de Suporte')),
            ],
            options={
                'verbose_name': 'Tipo de Suporte',
                'verbose_name_plural': 'Tipos de Suporte',
            },
        ),
        migrations.AlterModelOptions(
            name='preco',
            options={'verbose_name': 'Preço', 'verbose_name_plural': 'Preços'},
        ),
        migrations.AlterField(
            model_name='preco',
            name='nome',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.nameprice', verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='preco',
            name='suporte',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.suporte', verbose_name='Tipo de Suporte'),
        ),
    ]
