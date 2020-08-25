# Generated by Django 2.2.3 on 2020-08-25 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shepherd', '0012_auto_20200616_0441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='burned_explanation',
            field=models.TextField(blank=True, help_text='Provide details such as how the domain was detected, why it was blacklisted for spam, if it was flagged with a bad category, etc.', null=True, verbose_name='Health Explanation'),
        ),
        migrations.AlterField(
            model_name='domain',
            name='dns_record',
            field=models.TextField(blank=True, help_text="Enter the domain's DNS records - leave blank if you will run DNS updates later", null=True, verbose_name='DNS Records'),
        ),
        migrations.AlterField(
            model_name='domainnote',
            name='note',
            field=models.TextField(blank=True, help_text='Use this area to add a note to this domain', null=True, verbose_name='Notes'),
        ),
        migrations.AlterField(
            model_name='servernote',
            name='note',
            field=models.TextField(blank=True, help_text='Use this area to add a note to this server', null=True, verbose_name='Notes'),
        ),
    ]
