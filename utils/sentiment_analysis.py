from transformers import pipeline

# Load the pre-trained Hugging Face sentiment analysis model
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_sentiment(text):
    """
    Analyze the sentiment of the input text using a pre-trained BERT model.
    Returns: 'Positive', 'Negative', or 'Neutral'
    """
    if not text.strip():
        return "Neutral"  # default for empty or whitespace-only input

    # Get sentiment prediction from the model
    result = sentiment_pipeline(text)[0]
    label = result['label']
    
    # Sentiment classification
    if label == 'NEGATIVE':
        return "Negative"
    elif label == 'POSITIVE':
        return "Positive"
    else:
        return "Neutral"
