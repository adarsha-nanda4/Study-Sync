# Generated by Django 5.0 on 2023-12-31 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField(max_length=10000)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
