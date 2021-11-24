# Generated by Django 3.2 on 2021-06-10 02:21

from django.db import migrations

features = [
    {"name": "Virtual Desktop", "app_name": "researcher_desktop", "currently_available": True,
        "feature_or_service": True, "auto_approved": True, "beta": True, "closed_beta": False,
        "description": "Researcher desktop provides users access to an easy to use, quick to launch computer running in the Melbourne Research Cloud. This provides extra computing power for your research, a computer that's always on and always available to be running computation, scraping APIs, or running programs you can't run on your own computer."},
]


def add_group_data(apps, schema_editor):
    # We can't import the Group model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Group = apps.get_model('auth', 'Group')
    Group.objects.get_or_create(name='Support Staff')
    Group.objects.get_or_create(name='Closed Beta User')


def add_feature_data(apps, schema_editor):
    # We can't import the Feature model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Feature = apps.get_model('researcher_workspace', 'Feature')
    for feature_dict in features:
        feature = Feature.objects.get_or_create(name=feature_dict['name'])[0]
        for key, value in feature_dict.items():
            setattr(feature, key, value)
        feature.save()


class Migration(migrations.Migration):

    dependencies = [
        ('researcher_workspace', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_group_data),
        migrations.RunPython(add_feature_data),
    ]
