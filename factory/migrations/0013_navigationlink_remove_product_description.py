# Generated by Django 5.1.5 on 2025-01-26 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factory', '0012_alter_feature_options_feature_product_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NavigationLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('order', models.PositiveIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
    ]
