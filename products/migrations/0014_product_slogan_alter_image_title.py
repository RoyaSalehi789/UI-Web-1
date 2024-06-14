# Generated by Django 5.0.6 on 2024-06-14 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_product_set_as_site_background'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slogan',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(choices=[('off-box', 'Off-box'), ('detail-box', 'Detail-box'), ('banner', 'Banner'), ('background', 'Background')], default='', max_length=100),
        ),
    ]
