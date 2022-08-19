# Generated by Django 4.0.5 on 2022-08-07 03:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('id_material', models.IntegerField(primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=50)),
                ('format', models.CharField(max_length=20)),
                ('done_by', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserLogin',
            fields=[
                ('email', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=500)),
                ('occupation', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Coordinator',
            fields=[
                ('user_login', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='site_ong.userlogin')),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('user_login', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='site_ong.userlogin')),
                ('reviewText', models.CharField(max_length=800)),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('user_login', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='site_ong.userlogin')),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=12)),
            ],
        ),
    ]
