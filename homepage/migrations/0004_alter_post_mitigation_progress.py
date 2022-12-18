# Generated by Django 4.1.4 on 2022-12-18 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_post_mitigation_progress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='mitigation_progress',
            field=models.CharField(choices=[('Not Mitigated', 'Not Mitigated'), ('Partially Mitigated', 'Partially Mitigated'), ('Fully Mitigated', 'Fully Mitigated')], max_length=200, null=True),
        ),
    ]