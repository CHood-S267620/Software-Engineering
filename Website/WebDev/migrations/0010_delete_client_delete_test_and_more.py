# Generated by Django 5.1.7 on 2025-03-15 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebDev', '0009_test'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.RenameField(
            model_name='website_details',
            old_name='Userid',
            new_name='ClientID',
        ),
        migrations.AlterField(
            model_name='website_details',
            name='WebsiteStatus',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
