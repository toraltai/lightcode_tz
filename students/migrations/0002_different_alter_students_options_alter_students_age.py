# Generated by Django 4.1.1 on 2022-09-12 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Different',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterModelOptions(
            name='students',
            options={'verbose_name_plural': 'Студенты'},
        ),
        migrations.AlterField(
            model_name='students',
            name='age',
            field=models.IntegerField(verbose_name='Возраст'),
        ),
    ]
