from transformers import pipeline
from textblob import TextBlob

# Load sentiment analysis model
sentiment_analyzer = pipeline("sentiment-analysis")

def analyze_sentiment(message):
    """Detect sentiment of user message."""
    sentiment = sentiment_analyzer(message)[0]
    sentiment_label = sentiment['label']

    if sentiment_label == 'POSITIVE':
        return "positive"
    elif sentiment_label == 'NEGATIVE':
        return "negative"
    else:
        return "neutral"

def chatbot_response(user_message):
    """Generate appropriate response based on sentiment."""
    sentiment = analyze_sentiment(user_message)
    
    if sentiment == "positive":
        response = "I'm glad you're feeling good! 😊 How can I assist further?"
    elif sentiment == "negative":
        response = "I'm sorry you're feeling that way. 💙 How can I help you?"
    else:
        response = "I see. What else can I do for you?"

    return response

# Test the chatbot interaction
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        print("Chatbot:", chatbot_response(user_input))
