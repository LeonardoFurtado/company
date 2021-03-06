# Generated by Django 3.2.8 on 2021-10-20 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trading_name', models.CharField(max_length=150, verbose_name='Trading name')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Name')),
                ('situation', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive'), ('E', 'Excluded')], default='A', max_length=1)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name='First name')),
                ('last_name', models.CharField(max_length=150, verbose_name='Last name')),
                ('username', models.CharField(max_length=150, unique=True, verbose_name='Username')),
                ('situation', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive'), ('E', 'Excluded')], default='A', max_length=1)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('company', models.ManyToManyField(related_name='employee', to='api.Company')),
            ],
        ),
    ]
