# Generated by Django 3.2.5 on 2021-09-11 16:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=300)),
                ('short_intro', models.CharField(max_length=500)),
                ('bio', models.TextField(max_length=2000)),
                ('profile_image', models.ImageField(blank=True, default='profiles/user-default.png', null=True, upload_to='profiles/')),
                ('github', models.CharField(blank=True, max_length=400, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=400, null=True)),
                ('youtube', models.CharField(blank=True, max_length=400, null=True)),
                ('website', models.CharField(blank=True, max_length=400, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
