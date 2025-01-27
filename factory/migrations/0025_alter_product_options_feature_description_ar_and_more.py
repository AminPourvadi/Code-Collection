# Generated by Django 5.1.5 on 2025-01-27 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factory', '0024_alter_product_options_remove_product_title_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'محصول', 'verbose_name_plural': 'products'},
        ),
        migrations.AddField(
            model_name='feature',
            name='description_ar',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='feature',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='feature',
            name='description_fa',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='feature',
            name='title_ar',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='feature',
            name='title_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='feature',
            name='title_fa',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
