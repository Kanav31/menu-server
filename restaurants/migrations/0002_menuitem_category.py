# Generated by Django 4.2.3 on 2024-06-06 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='category',
            field=models.CharField(default='Uncategorized', max_length=255),
        ),
    ]
