# Generated by Django 4.1.5 on 2023-01-18 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BulletinBoard', '0004_alter_advert_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='upload',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
