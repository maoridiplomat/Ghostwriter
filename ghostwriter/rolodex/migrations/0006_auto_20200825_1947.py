# Generated by Django 2.2.3 on 2020-08-25 19:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import ghostwriter.rolodex.models


class Migration(migrations.Migration):
    dependencies = [
        ("rolodex", "0005_auto_20191122_2304"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="codename",
            field=models.CharField(
                blank=True,
                help_text="A codename for the client that might be used to discuss the client in public",
                max_length=255,
                null=True,
                verbose_name="Client Codename",
            ),
        ),
        migrations.AlterField(
            model_name="client",
            name="name",
            field=models.CharField(
                help_text="Provide the client's full name as you want it to appear in a report",
                max_length=255,
                unique=True,
                verbose_name="Client Name",
            ),
        ),
        migrations.AlterField(
            model_name="client",
            name="note",
            field=models.TextField(
                blank=True,
                help_text="Describe the client or provide some additional information",
                null=True,
                verbose_name="Client Note",
            ),
        ),
        migrations.AlterField(
            model_name="client",
            name="short_name",
            field=models.CharField(
                blank=True,
                help_text="Provide an abbreviated name to be used in reports",
                max_length=255,
                null=True,
                verbose_name="Client Short Name",
            ),
        ),
        migrations.AlterField(
            model_name="clientcontact",
            name="email",
            field=models.CharField(
                blank=True,
                help_text="Enter an email address for this contact",
                max_length=255,
                null=True,
                verbose_name="Email",
            ),
        ),
        migrations.AlterField(
            model_name="clientcontact",
            name="job_title",
            field=models.CharField(
                blank=True,
                help_text="Enter the contact's job title or project role as you want it to appear in a report",
                max_length=255,
                null=True,
                verbose_name="Title or Role",
            ),
        ),
        migrations.AlterField(
            model_name="clientcontact",
            name="name",
            field=models.CharField(
                help_text="Enter the contact's full name", max_length=255, null=True, verbose_name="Name"
            ),
        ),
        migrations.AlterField(
            model_name="clientcontact",
            name="note",
            field=models.TextField(
                blank=True,
                help_text="Provide additional information about the contact",
                null=True,
                verbose_name="Client Note",
            ),
        ),
        migrations.AlterField(
            model_name="clientcontact",
            name="phone",
            field=models.CharField(
                blank=True,
                help_text="Enter a phone number for this contact",
                max_length=50,
                null=True,
                verbose_name="Phone",
            ),
        ),
        migrations.AlterField(
            model_name="clientnote",
            name="note",
            field=models.TextField(
                blank=True, help_text="Leave the client or related projects", null=True, verbose_name="Notes"
            ),
        ),
        migrations.AlterField(
            model_name="clientnote",
            name="timestamp",
            field=models.DateField(auto_now_add=True, help_text="Creation timestamp", verbose_name="Timestamp"),
        ),
        migrations.AlterField(
            model_name="objectivestatus",
            name="objective_status",
            field=models.CharField(
                help_text="Enter an objective status (e.g. Active, On Hold)",
                max_length=255,
                unique=True,
                verbose_name="Objective Status",
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="client",
            field=models.ForeignKey(
                help_text="Select the client to which this project should be attached",
                on_delete=django.db.models.deletion.CASCADE,
                to="rolodex.Client",
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="codename",
            field=models.CharField(
                blank=True,
                help_text="A codename for the client that might be used to discuss the client in public",
                max_length=255,
                null=True,
                verbose_name="Project Codename",
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="complete",
            field=models.BooleanField(
                default=False, help_text="Mark this project as complete", verbose_name="Completed"
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="end_date",
            field=models.DateField(
                help_text="Enter the end date of this project", max_length=12, verbose_name="End Date"
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="note",
            field=models.TextField(
                blank=True,
                help_text="Provide additional information about the project and planning",
                null=True,
                verbose_name="Notes",
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="slack_channel",
            field=models.CharField(
                blank=True,
                help_text="Provide an Slack channel to be used for project notifications",
                max_length=255,
                null=True,
                verbose_name="Project Slack Channel",
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="start_date",
            field=models.DateField(
                help_text="Enter the start date of this project", max_length=12, verbose_name="Start Date"
            ),
        ),
        migrations.AlterField(
            model_name="projectassignment",
            name="end_date",
            field=models.DateField(
                blank=True, help_text="Enter the end date of the project", null=True, verbose_name="End Date"
            ),
        ),
        migrations.AlterField(
            model_name="projectassignment",
            name="note",
            field=models.TextField(
                blank=True,
                help_text="Provide additional information about the project role and assignment",
                null=True,
                verbose_name="Notes",
            ),
        ),
        migrations.AlterField(
            model_name="projectassignment",
            name="operator",
            field=models.ForeignKey(
                blank=True,
                help_text="Select a user to assign to this project",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="projectassignment",
            name="role",
            field=models.ForeignKey(
                blank=True,
                help_text="Select a role that best describes the selected user's role in this project",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="rolodex.ProjectRole",
            ),
        ),
        migrations.AlterField(
            model_name="projectassignment",
            name="start_date",
            field=models.DateField(
                blank=True, help_text="Enter the start date of the project", null=True, verbose_name="Start Date"
            ),
        ),
        migrations.AlterField(
            model_name="projectnote",
            name="note",
            field=models.TextField(
                blank=True,
                help_text="Leave a note about the project or related client",
                null=True,
                verbose_name="Notes",
            ),
        ),
        migrations.AlterField(
            model_name="projectnote",
            name="timestamp",
            field=models.DateField(auto_now_add=True, help_text="Creation timestamp", verbose_name="Timestamp"),
        ),
        migrations.AlterField(
            model_name="projectobjective",
            name="deadline",
            field=models.DateField(
                blank=True,
                help_text="Provide a deadline for this objective",
                max_length=12,
                null=True,
                verbose_name="Due Date",
            ),
        ),
        migrations.AlterField(
            model_name="projectobjective",
            name="status",
            field=models.ForeignKey(
                default=ghostwriter.rolodex.models.ProjectObjective.get_status,
                help_text="Set the status for this objective",
                on_delete=django.db.models.deletion.PROTECT,
                to="rolodex.ObjectiveStatus",
            ),
        ),
        migrations.AlterField(
            model_name="projectrole",
            name="project_role",
            field=models.CharField(
                help_text="Enter an operator role used for project assignments",
                max_length=255,
                unique=True,
                verbose_name="Project Role",
            ),
        ),
        migrations.AlterField(
            model_name="projecttype",
            name="project_type",
            field=models.CharField(
                help_text="Enter a project type (e.g. red team, penetration test)",
                max_length=255,
                unique=True,
                verbose_name="Project Type",
            ),
        ),
    ]
