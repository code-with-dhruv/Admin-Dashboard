# Generated by Django 4.1.3 on 2023-07-18 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_supplier_gst_id_alter_customer_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='number',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Projects', 'projects'), ('AMC', 'AMC'), ('Sales', 'Sales'), ('Supplier', 'Supplier')], max_length=50, null=True),
        ),
    ]
