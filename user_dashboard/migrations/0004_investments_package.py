# Generated by Django 3.2.9 on 2021-11-19 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_dashboard', '0003_rename_amount_packages_hours'),
    ]

    operations = [
        migrations.AddField(
            model_name='investments',
            name='package',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pack', to='user_dashboard.packages'),
        ),
    ]
