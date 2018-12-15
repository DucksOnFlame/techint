# Generated by Django 2.1.3 on 2018-12-15 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Imię')),
                ('date_of_birth', models.DateField(verbose_name='Data urodzenia')),
                ('email', models.EmailField(max_length=254, verbose_name='Adres e-mail')),
                ('height', models.IntegerField(default=170, verbose_name='Wzrost')),
            ],
        ),
    ]
