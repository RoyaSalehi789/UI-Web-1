# Generated by Django 5.0.6 on 2024-06-14 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='quantity',
            new_name='count',
        ),
        migrations.AddField(
            model_name='cart',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='final_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
