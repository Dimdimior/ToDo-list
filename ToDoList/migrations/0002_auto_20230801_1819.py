from django.db import migrations


def create_superuser(apps, schema_editor):
    user = apps.get_model('auth', 'User')
    user.objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='test'
    )


def remove_superuser(apps, schema_editor):
    user = apps.get_model('auth', 'User')
    user.objects.filter(username='admin', email='admin@example.com').delete()


class Migration(migrations.Migration):
    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),  # Adding this line
        ('ToDoList', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_superuser, remove_superuser)
    ]
