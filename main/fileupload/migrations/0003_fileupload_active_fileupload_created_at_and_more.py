# Generated by Django 4.0.2 on 2022-02-08 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0002_category_fileupload_name_fileupload_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileupload',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='fileupload',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='fileupload',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='fileupload',
            name='expiration_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='fileupload',
            name='internal_notes',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='fileupload',
            name='release_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='fileupload',
            name='text_number',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='fileupload',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
