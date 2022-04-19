# Generated by Django 4.0.4 on 2022-04-19 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('around', '0009_remove_business_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='around.profile'),
        ),
    ]