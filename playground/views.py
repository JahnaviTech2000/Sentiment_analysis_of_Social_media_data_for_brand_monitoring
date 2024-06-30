from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
import pandas as pd
from .sentiment_model import pred
import json

# from .utils import get_tweets_and_comments


# Create your views here.
def home(request):
    if request.method == 'POST':
        brand = Brand()
        name = request.POST['brand_name']
        fil = request.FILES['fil']
        fil2 = request.FILES.get('fil')
        brand.name = name
        brand.csv = fil
        brand.save()
        print(fil2)
    # Process the uploaded CSV file (assuming 'Comment' is the column name)
        # if overall_sentiment_score >= 0.5:
        #     overall_sentiment = 'Positive'
        # else:
        #     overall_sentiment = 'Negative'
        
        # df = pd.read_csv(stored_file_path)
        # comments = df['Comment'].tolist()

        # sentiment_model = SentimentModel.objects.first()
        # overall_sentiment = sentiment_model.predict(comments)

        # comments = handle_csv_upload(stored_file_path)
        # overall_sentiment = calculate_overall_sentiment([comment['Comment'] for comment in comments])

        # context = {'overall_brand_sentiment_category': overall_brand_sentiment_category,'overall_brand_sentiment_score':overall_brand_sentiment_score,'top_positive_comments':top_positive_comments,'top_neutral_comments':top_neutral_comments,'top_negative_comments':top_negative_comments,'chart_data': json.dumps(chart_data)}
        return redirect('playground:dashboard',id=brand.id)
    return render(request, 'index.html',{})


def dashboard(request,id):

    brand = Brand.objects.get(id=id)
    stored_file_path = brand.csv.path
    data = pred(stored_file_path)
    overall_brand_sentiment_category = data[0]
    overall_brand_sentiment_score = data[1]
    top_positive_comments = data[2]
    top_neutral_comments = data[4]
    top_negative_comments = data[3]
    total_positive_comments = data[5]
    total_neutral_comments = data[6]
    total_negative_comments = data[7]
    brand.overall_brand_sentiment_category = overall_brand_sentiment_category
    brand.overall_brand_sentiment_score = round(overall_brand_sentiment_score,2)
    brand.total_positive_comments= total_positive_comments
    brand.total_neutral_comments = total_neutral_comments
    brand.total_negative_comments = total_negative_comments
    brand.save()

    bname = brand.name
    overall_score = round(((overall_brand_sentiment_score/3)*100),2)



    for c in top_positive_comments:
        comment = Comment()
        
        comment.b_id = brand
        comment.cmt = c
        comment.type = "positive"
        comment.save()

    for c in top_neutral_comments:
        comment2 = Comment()
        comment2.cmt = c
        comment2.type = "neutral"
        comment2.save()

    for c in top_negative_comments:
        comment3 = Comment()
        comment3.cmt = c
        comment3.type = "negative"
        comment3.save()


    values = []
    values.append(total_positive_comments)
    values.append(total_negative_comments)
    values.append(total_neutral_comments)
    labels = ["positive","negative","neutral"]
    chart_data = {
    "labels": labels,
    "values": values,}

   
    
    context = {'bname':bname,'overall_brand_sentiment_category': overall_brand_sentiment_category,'overall_brand_sentiment_score':overall_score,'top_positive_comments':top_positive_comments,'top_neutral_comments':top_neutral_comments,'top_negative_comments':top_negative_comments,'chart_data': json.dumps(chart_data)}

    return render(request,'dashboard.html',context)
