# Generated by Django 4.1.7 on 2024-03-10 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0006_sentimentmodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SentimentModel',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='negfive',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='pstfive',
        ),
        migrations.AddField(
            model_name='brand',
            name='overall_brand_sentiment_category',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='brand',
            name='overall_brand_sentiment_score',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='brand',
            name='total_negative_comments',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='brand',
            name='total_neutral_comments',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='brand',
            name='total_positive_comments',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='cmt',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='type',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
