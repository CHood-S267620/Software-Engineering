# Generated by Django 5.1.7 on 2025-03-15 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebDev', '0013_remove_website_details_timeframeid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website_details',
            name='DueDate',
            field=models.CharField(blank=True, default=1, max_length=255),
            preserve_default=False,
        ),
    ]
