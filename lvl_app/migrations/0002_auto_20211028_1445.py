# Generated by Django 3.1 on 2021-10-28 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lvl_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfoprofile',
            old_name='user_portfolio_Site',
            new_name='user_portfolio_site',
        ),
    ]