# Generated by Django 2.0 on 2018-03-18 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature', models.CharField(max_length=32)),
                ('text', models.TextField(verbose_name='text')),
            ],
        ),
    ]
