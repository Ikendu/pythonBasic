# Generated by Django 5.1.4 on 2024-12-13 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="students",
            name="date",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="students",
            name="email",
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name="students",
            name="phone",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="students",
            name="school",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
