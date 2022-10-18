# Generated by Django 4.1.2 on 2022-10-18 18:47

from django.db import migrations, models
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Enquiry",
            fields=[
                (
                    "pkid",
                    models.BigAutoField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                ("name", models.CharField(max_length=100, verbose_name="Your Name")),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        default="+306900000000",
                        max_length=128,
                        region=None,
                        verbose_name="Phone Number",
                    ),
                ),
                ("email", models.CharField(max_length=100, verbose_name="Email")),
                ("subject", models.CharField(max_length=100, verbose_name="Subject")),
                ("message", models.CharField(max_length=255, verbose_name="Message")),
            ],
            options={
                "verbose_name_plural": "Enqueries",
            },
        ),
    ]
