# Generated by Django 3.1.7 on 2021-03-22 23:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FantasyTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=100)),
                ('created_date', models.DateField()),
                ('last_modified_date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('player_id', models.IntegerField()),
                ('points_per_game', models.FloatField()),
                ('rebounds_per_game', models.FloatField()),
                ('assists_per_game', models.FloatField()),
                ('created_date', models.DateField()),
                ('last_modified_date', models.DateField()),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.fantasyteam')),
            ],
        ),
    ]
