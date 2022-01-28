# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from structure.apps.authentication.models import CustomUser


def create_superuser(apps, schema_editor):
    superuser = CustomUser()
    superuser.is_active = True
    superuser.is_superuser = True
    superuser.is_staff = True
    superuser.username = 'admin'
    superuser.email = 'admin@admin.net'
    superuser.set_password('admin')
    superuser.save()


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_customuser_avatar'),
    ]

    operations = [
        migrations.RunPython(create_superuser)
    ]
