# Generated by Django 4.1.7 on 2024-03-07 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0005_rename_comments_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='SentimentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.BinaryField()),
            ],
        ),
    ]
