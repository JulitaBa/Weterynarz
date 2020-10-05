# Generated by Django 3.1.1 on 2020-09-13 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200, verbose_name='Email')),
                ('subject', models.CharField(max_length=200, verbose_name='Tytuł')),
                ('message', models.TextField(max_length=1000, verbose_name='Wiadomość')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='ContactForm',
        ),
    ]
