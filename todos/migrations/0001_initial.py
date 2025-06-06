# Generated by Django 5.2 on 2025-04-08 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('due_datetime', models.DateTimeField()),
                ('state', models.CharField(choices=[('PENDING', 'Pending'), ('COMPLETED', 'Completed'), ('POSTPONED', 'Postponed'), ('CANCELLED', 'Cancelled')], default='PENDING', max_length=9)),
            ],
        ),
    ]
