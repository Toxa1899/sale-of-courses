# Generated by Django 5.1 on 2024-08-30 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_card', '0008_productcard_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcard',
            name='cap',
            field=models.ImageField(upload_to='product_card/', verbose_name='шапка курса'),
        ),
        migrations.AlterField(
            model_name='productcard',
            name='description',
            field=models.TextField(verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='productcard',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='активна ли карточка'),
        ),
        migrations.AlterField(
            model_name='productcard',
            name='name',
            field=models.CharField(max_length=100, verbose_name='название курса'),
        ),
        migrations.AlterField(
            model_name='productcard',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='цена курса'),
        ),
    ]
