# Generated by Django 4.2.5 on 2023-10-02 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_remove_order_robot_serial_order_robot_model1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='robot_model1',
            new_name='robot_model',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='robot_version1',
            new_name='robot_version',
        ),
    ]
