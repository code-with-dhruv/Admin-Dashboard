# Generated by Django 4.1.3 on 2023-07-09 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('software', 'software'), ('Hardware', 'Hardware')], max_length=50, null=True),
        ),
    ]