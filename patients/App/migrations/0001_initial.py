# Generated by Django 4.0.4 on 2022-04-26 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=40)),
                ('age', models.CharField(max_length=3)),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=1)),
                ('note', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
