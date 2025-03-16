# Generated by Django 5.1.7 on 2025-03-14 19:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebDev', '0007_remove_website_clientid'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='website_details',
            old_name='ClientID',
            new_name='Userid',
        ),
        migrations.AddField(
            model_name='website',
            name='ClientID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
