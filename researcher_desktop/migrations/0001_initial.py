# Generated by Django 3.2.9 on 2021-11-24 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('researcher_workspace', '0003_add_terms_agreed'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvailabilityZone',
            fields=[
                ('name', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('zone_weight', models.IntegerField()),
                ('enabled', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('name', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='domains', to='researcher_desktop.availabilityzone')),
            ],
        ),
        migrations.CreateModel(
            name='DesktopType',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('logo', models.URLField(blank=True, null=True)),
                ('image_name', models.CharField(max_length=256)),
                ('default_flavor_name', models.CharField(max_length=32)),
                ('big_flavor_name', models.CharField(max_length=32)),
                ('volume_size', models.IntegerField(default=20, help_text='Size in GB')),
                ('enabled', models.BooleanField(default=True)),
                ('details', models.JSONField(blank=True, null=True)),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='researcher_workspace.feature')),
                ('restrict_to_zones', models.ManyToManyField(blank=True, to='researcher_desktop.AvailabilityZone')),
            ],
        ),
    ]
