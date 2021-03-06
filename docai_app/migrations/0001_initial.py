# Generated by Django 3.2.5 on 2021-09-22 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('doc_id', models.AutoField(db_column='DOC_ID', primary_key=True, serialize=False)),
                ('title', models.CharField(db_column='TITLE', max_length=255, unique=True)),
                ('doc_url', models.URLField(db_column='DOC_URL')),
                ('doc_summary', models.TextField(blank=True, db_column='DOC_SUMMARY', null=True)),
                ('upload_date', models.DateField(db_column='UPLOAD_DATE')),
            ],
            options={
                'db_table': 'ibef_tb',
            },
        ),
    ]
