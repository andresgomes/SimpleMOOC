# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(verbose_name='Nome', max_length=100)),
                ('slug', models.SlugField(verbose_name='Atalho')),
                ('description', models.TextField(verbose_name='Descrição', blank=True)),
                ('start_date', models.DateField(verbose_name='Data de Inicio', blank=True, null=True)),
                ('image', models.ImageField(upload_to='courses/images', verbose_name='Imagem')),
                ('creater_at', models.DateTimeField(verbose_name='Criado em', auto_now_add=True)),
                ('upload_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
        ),
    ]
