import torch
from transformers import BertTokenizer, BertForSequenceClassification
import pandas as pd

# Define the device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def sentiment_analysis_on_comments(model, tokenizer, device, csv_file):
    # Read CSV file containing comments
    comments_df = pd.read_csv(csv_file)
    comments = comments_df['Comment'].tolist()

    # Preprocess comments
    encoded_comments = tokenizer(comments, padding='max_length', truncation=True, max_length=128, return_tensors='pt')
    input_ids = encoded_comments['input_ids'].to(device)
    attention_mask = encoded_comments['attention_mask'].to(device)

    # Perform inference
    model.eval()
    with torch.no_grad():
        outputs = model(input_ids, attention_mask=attention_mask)
        logits = outputs.logits
        probabilities = torch.softmax(logits, dim=1)
    
    # Determine positive, negative, and neutral comments
    positive_comments = [(prob, comment) for prob, comment in zip(probabilities[:, 2].cpu().numpy(), comments) if prob >= 0.5]
    neutral_comments = [(prob, comment) for prob, comment in zip(probabilities[:, 1].cpu().numpy(), comments) if 0.4 <= prob <= 0.6]
    negative_comments = [(prob, comment) for prob, comment in zip(probabilities[:, 0].cpu().numpy(), comments) if prob >= 0.5]

    # Sort comments by sentiment probability
    positive_comments.sort(reverse=True)
    neutral_comments.sort(reverse=True)
    negative_comments.sort(reverse=True)

    # Calculate overall sentiment score
    positive_sentiment_score = sum(probabilities[:, 2].cpu().numpy()) / len(positive_comments) if positive_comments else 0
    neutral_sentiment_score = sum(probabilities[:, 1].cpu().numpy()) / len(neutral_comments) if neutral_comments else 0
    negative_sentiment_score = sum(probabilities[:, 0].cpu().numpy()) / len(negative_comments) if negative_comments else 0
    overall_brand_sentiment_score = (positive_sentiment_score + neutral_sentiment_score + negative_sentiment_score) / 3

    # Determine overall brand sentiment category
    if overall_brand_sentiment_score >= 0.6:
        overall_brand_sentiment_category = 'Positive'
    elif overall_brand_sentiment_score <= 0.4:
        overall_brand_sentiment_category = 'Negative'
    else:
        overall_brand_sentiment_category = 'Neutral'

    return (overall_brand_sentiment_category,
            overall_brand_sentiment_score,
            positive_sentiment_score,
            neutral_sentiment_score,
            negative_sentiment_score,
            len(positive_comments),
            len(neutral_comments),
            len(negative_comments),
            [comment for _, comment in positive_comments[:5]],
            [comment for _, comment in neutral_comments[:5]],
            [comment for _, comment in negative_comments[:5]])

def pred(csvfile):
    # Load pre-trained BERT model and tokenizer
    model_name = 'bert-base-uncased'
    tokenizer = BertTokenizer.from_pretrained(model_name)
    model = BertForSequenceClassification.from_pretrained(model_name, num_labels=3)  # 3 output classes

    # Fine-tune the model (Omitted for brevity)

    # Load fine-tuned model
    model.load_state_dict(torch.load('fine_tuned_bert_sentiment_model.pth', map_location=device))
    model.eval()

    # Perform sentiment analysis on comments from CSV file
    csv_file = csvfile  # Replace 'comments.csv' with the path to your CSV file
    (overall_brand_sentiment_category,
    overall_brand_sentiment_score,
    positive_sentiment_score,
    neutral_sentiment_score,
    negative_sentiment_score,
    total_positive_comments,
    total_neutral_comments,
    total_negative_comments,
    top_positive_comments,
    top_neutral_comments,
    top_negative_comments) = sentiment_analysis_on_comments(model, tokenizer, device, csv_file)

    print(f'Overall Brand Sentiment Category: {overall_brand_sentiment_category}, Overall Brand Sentiment Score: {overall_brand_sentiment_score:.4f}')
    print(f'Total Positive Comments: {total_positive_comments}, Total Neutral Comments: {total_neutral_comments}, Total Negative Comments: {total_negative_comments}\n')

    if top_positive_comments:
        print('Top 5 positive comments:')
        for i, comment in enumerate(top_positive_comments, 1):
            print(f'{i}. {comment}')
        print()

    if top_neutral_comments:
        print('Top 5 neutral comments:')
        for i, comment in enumerate(top_neutral_comments, 1):
            print(f'{i}. {comment}')
        print()

    if top_negative_comments:
        print('Top 5 negative comments:')
        for i, comment in enumerate(top_negative_comments, 1):
            print(f'{i}. {comment}')
        print()
    
    return overall_brand_sentiment_category,overall_brand_sentiment_score,top_positive_comments,top_negative_comments,top_neutral_comments,total_positive_comments,total_neutral_comments,total_negative_comments
