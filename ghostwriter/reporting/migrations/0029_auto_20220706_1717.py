# Generated by Django 3.2.11 on 2022-07-06 17:17

# Django Imports
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("reporting", "0028_auto_20220608_1808"),
    ]

    operations = [
        migrations.RunSQL("ALTER TABLE reporting_reportfindinglink ALTER COLUMN complete SET DEFAULT FALSE;"),
        migrations.RunSQL("ALTER TABLE reporting_reportfindinglink ALTER COLUMN position SET DEFAULT 1;"),
    ]
