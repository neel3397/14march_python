# Generated by Django 4.2.1 on 2023-05-25 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Chairman", "0002_chairman_pic_societymember_pic"),
    ]

    operations = [
        migrations.CreateModel(
            name="EventGallery",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("media_type", models.CharField(max_length=30)),
                (
                    "video",
                    models.FileField(
                        blank=True, null=True, upload_to="media/videos", verbose_name=""
                    ),
                ),
                (
                    "pic",
                    models.FileField(blank=True, null=True, upload_to="media/images"),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Chairman.user"
                    ),
                ),
            ],
        ),
    ]