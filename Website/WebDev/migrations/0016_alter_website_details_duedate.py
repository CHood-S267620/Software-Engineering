# Generated by Django 5.1.7 on 2025-03-16 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebDev', '0015_alter_billing_datepaid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website_details',
            name='DueDate',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
