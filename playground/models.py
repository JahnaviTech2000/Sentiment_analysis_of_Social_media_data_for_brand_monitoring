from django.db import models
import uuid
from datetime import datetime


class Brand(models.Model):
    
    
    id = models.CharField(primary_key=True, max_length=6, unique=True)
    # Other fields in your model
    name =models.CharField(max_length=100)
    overall_brand_sentiment_category= models.CharField(max_length=10,null=True)
    overall_brand_sentiment_score = models.IntegerField(null=True)
    total_positive_comments = models.IntegerField(null=True)
    total_negative_comments = models.IntegerField(null=True)
    total_neutral_comments = models.IntegerField(null=True)
    csv= models.FileField(upload_to= "csv_files", null= True)
    def save(self, *args, **kwargs):
        if not self.id:
            # Generate a random 6-digit ID
            self.id = self.generate_random_id()
        super().save(*args, **kwargs)

    def generate_random_id(self):
        import random
        return str(random.randint(100000, 999999))

    def _str_(self):
        return self.id
    #created_at = models.DateTimeField(default=datetime.now)
    
    
class Comment(models.Model):
    b_id = models.ForeignKey(Brand, null= True, on_delete=models.CASCADE)
    cmt = models.TextField(null=True)
    type = models.CharField(max_length=10,null=True)










# user = models.CharField(max_length=100)
   # image = models.ImageField(upload_to='post_images')
    #caption = models.TextField()
#no_of_likes = models.IntegerField(default=0)