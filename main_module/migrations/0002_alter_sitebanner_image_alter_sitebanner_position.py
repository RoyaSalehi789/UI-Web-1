# Generated by Django 5.0.6 on 2024-06-09 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitebanner',
            name='image',
            field=models.ImageField(upload_to='images/banners', verbose_name='banner image'),
        ),
        migrations.AlterField(
            model_name='sitebanner',
            name='position',
            field=models.CharField(choices=[('home_page', 'صفحه اصلی'), ('product_list', 'صفحه لیست محصولات'), ('product_detail', 'صفحه جزئیات محصولات'), ('about_us', 'درباره ما')], max_length=200, verbose_name='banner position'),
        ),
    ]
