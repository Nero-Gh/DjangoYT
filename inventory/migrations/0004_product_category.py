# Generated by Django 4.1.5 on 2023-01-16 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_remove_product_category_alter_category_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(to='inventory.category'),
        ),
    ]
