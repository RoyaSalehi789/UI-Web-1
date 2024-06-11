# Generated by Django 5.0.6 on 2024-06-10 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_product_images_remove_product_videos_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='product',
        ),
        migrations.RemoveField(
            model_name='video',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ManyToManyField(related_name='products', to='products.image'),
        ),
        migrations.AddField(
            model_name='product',
            name='videos',
            field=models.ManyToManyField(related_name='products', to='products.video'),
        ),
    ]