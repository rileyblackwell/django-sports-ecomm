# Generated by Django 3.2.9 on 2021-11-12 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(default='no brand', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(max_length=2),
        ),
    ]
