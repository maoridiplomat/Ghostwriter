# Generated by Django 3.2.19 on 2024-05-16 17:22

from django.db import migrations, models
import ghostwriter.rolodex.validators


def replace_null_required_fields(apps, schema_editor):
    ClientContact = apps.get_model("rolodex", "ClientContact")
    ClientContact.objects.using(schema_editor.connection.alias).filter(email__isnull=True).update(email="fixme@example.com")
    ClientContact.objects.using(schema_editor.connection.alias).filter(job_title__isnull=True).update(job_title="(null job title)")

    ProjectContaxt = apps.get_model("rolodex", "ProjectContact")
    ProjectContaxt.objects.using(schema_editor.connection.alias).filter(email__isnull=True).update(email="fixme@example.com")
    ProjectContaxt.objects.using(schema_editor.connection.alias).filter(job_title__isnull=True).update(job_title="(null job title)")

    Evidence = apps.get_model("reporting", "Evidence")
    Evidence.objects.using(schema_editor.connection.alias).filter(friendly_name__isnull=True).update(friendly_name="null-name")


class Migration(migrations.Migration):

    dependencies = [
        ('rolodex', '0049_extra_fields_db_default'),
    ]

    operations = [
        migrations.RunPython(replace_null_required_fields, reverse_code=migrations.RunPython.noop),
        migrations.RunSQL('SET CONSTRAINTS ALL IMMEDIATE', reverse_sql='SET CONSTRAINTS ALL DEFERRED'),
        migrations.AlterField(
            model_name='client',
            name='address',
            field=models.TextField(blank=True, default='', help_text='An address to be used for reports or shipping', verbose_name='Client Business Address'),
        ),
        migrations.AlterField(
            model_name='client',
            name='codename',
            field=models.CharField(blank=True, default='', help_text='Give the client a codename (might be a ticket number, CMS reference, or something else)', max_length=255, verbose_name='Client Codename'),
        ),
        migrations.AlterField(
            model_name='client',
            name='note',
            field=models.TextField(blank=True, default='', help_text='Describe the client or provide some additional information', verbose_name='Client Note'),
        ),
        migrations.AlterField(
            model_name='client',
            name='short_name',
            field=models.CharField(blank=True, default='', help_text='Provide an abbreviated name to be used in reports', max_length=255, verbose_name='Client Short Name'),
        ),
        migrations.AlterField(
            model_name='clientcontact',
            name='email',
            field=models.CharField(help_text='Enter an email address for this contact', max_length=255, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='clientcontact',
            name='job_title',
            field=models.CharField(help_text="Enter the contact's job title or project role as you want it to appear in a report", max_length=255, verbose_name='Title or Role'),
        ),
        migrations.AlterField(
            model_name='clientcontact',
            name='note',
            field=models.TextField(blank=True, default='', help_text='Provide additional information about the contact', verbose_name='Contact Note'),
        ),
        migrations.AlterField(
            model_name='clientcontact',
            name='phone',
            field=models.CharField(blank=True, default='', help_text='Enter a phone number for this contact', max_length=50, verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='clientinvite',
            name='comment',
            field=models.TextField(blank=True, default='', help_text='Optional explanation for this invite', verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='clientnote',
            name='note',
            field=models.TextField(blank=True, default='', help_text='Leave the client or related projects', verbose_name='Notes'),
        ),
        migrations.AlterField(
            model_name='deconfliction',
            name='alert_source',
            field=models.CharField(blank=True, default='', help_text='Source of the alert (e.g., user reported, EDR, MDR, etc.)', max_length=255, verbose_name='Alert Source'),
        ),
        migrations.AlterField(
            model_name='deconfliction',
            name='description',
            field=models.TextField(blank=True, default='', help_text='Provide a brief description of this deconfliction request', verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='project',
            name='codename',
            field=models.CharField(blank=True, default='', help_text='Give the project a codename (might be a ticket number, PMO reference, or something else)', max_length=255, verbose_name='Project Codename'),
        ),
        migrations.AlterField(
            model_name='project',
            name='note',
            field=models.TextField(blank=True, default='', help_text='Provide additional information about the project and planning', verbose_name='Notes'),
        ),
        migrations.AlterField(
            model_name='project',
            name='slack_channel',
            field=models.CharField(blank=True, default='', help_text='Provide an Slack channel to be used for project notifications', max_length=255, verbose_name='Project Slack Channel'),
        ),
        migrations.AlterField(
            model_name='projectassignment',
            name='note',
            field=models.TextField(blank=True, default='', help_text='Provide additional information about the project role and assignment', verbose_name='Notes'),
        ),
        migrations.AlterField(
            model_name='projectcontact',
            name='email',
            field=models.CharField(help_text='Enter an email address for this contact', max_length=255, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='projectcontact',
            name='job_title',
            field=models.CharField(help_text="Enter the contact's job title or project role as you want it to appear in a report", max_length=255, verbose_name='Title or Role'),
        ),
        migrations.AlterField(
            model_name='projectcontact',
            name='note',
            field=models.TextField(blank=True, default='', help_text='Provide additional information about the contact', verbose_name='Contact Note'),
        ),
        migrations.AlterField(
            model_name='projectcontact',
            name='phone',
            field=models.CharField(blank=True, default='', help_text='Enter a phone number for this contact', max_length=50, verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='projectinvite',
            name='comment',
            field=models.TextField(blank=True, default='', help_text='Optional explanation for this invite', verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='projectnote',
            name='note',
            field=models.TextField(blank=True, default='', help_text='Leave a note about the project or related client', verbose_name='Notes'),
        ),
        migrations.AlterField(
            model_name='projectobjective',
            name='description',
            field=models.TextField(blank=True, default='', help_text='Provide a more detailed description, purpose, or context', verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='projectobjective',
            name='objective',
            field=models.CharField(blank=True, default='', help_text='Provide a high-level objective – add sub-tasks later for planning or as you discover obstacles', max_length=255, verbose_name='Objective'),
        ),
        migrations.AlterField(
            model_name='projectscope',
            name='description',
            field=models.TextField(blank=True, default='', help_text='Provide a brief description of this list', verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='projectscope',
            name='name',
            field=models.CharField(blank=True, default='', help_text='Provide a descriptive name for this list (e.g., External IPs, Cardholder Data Environment)', max_length=255, verbose_name='Scope Name'),
        ),
        migrations.AlterField(
            model_name='projectscope',
            name='scope',
            field=models.TextField(blank=True, default='', help_text='Provide a list of IP addresses, ranges, hostnames, or a mix with each entry on a new line', verbose_name='Scope'),
        ),
        migrations.AlterField(
            model_name='projectsubtask',
            name='task',
            field=models.TextField(blank=True, default='', help_text='Provide a concise objective', verbose_name='Task'),
        ),
        migrations.AlterField(
            model_name='projecttarget',
            name='hostname',
            field=models.CharField(blank=True, default='', help_text="Provide the target's hostname, fully qualified domain name, or other identifier", max_length=255, verbose_name='Hostname / FQDN'),
        ),
        migrations.AlterField(
            model_name='projecttarget',
            name='ip_address',
            field=models.CharField(blank=True, default='', help_text='Enter the IP address or range of the target host(s)', max_length=45, validators=[ghostwriter.rolodex.validators.validate_ip_range], verbose_name='IP Address'),
        ),
        migrations.AlterField(
            model_name='projecttarget',
            name='note',
            field=models.TextField(blank=True, default='', help_text='Provide additional information about the target(s) or the environment', verbose_name='Notes'),
        ),
        migrations.AlterField(
            model_name='whitecard',
            name='description',
            field=models.TextField(blank=True, default='', help_text='Provide a brief description of this white card', verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='whitecard',
            name='title',
            field=models.CharField(blank=True, default='', help_text='Provide a descriptive headline for this white card (e.g., a username, hostname, or short sentence', max_length=255, verbose_name='Title'),
        ),
        migrations.RunSQL('SET CONSTRAINTS ALL DEFERRED', reverse_sql='SET CONSTRAINTS ALL IMMEDIATE'),
    ]
