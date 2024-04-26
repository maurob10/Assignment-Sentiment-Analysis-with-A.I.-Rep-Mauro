import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from tkinter import *

# Ensure you have the necessary resources
nltk.download('vader_lexicon')

def analyze_sentiment():
    text = text_entry.get("1.0", END)  # Retrieves text from the text widget
    sia = SentimentIntensityAnalyzer()
    score = sia.polarity_scores(text)
    sentiment = 'Positive' if score['compound'] >= 0 else 'Negative'
    result_label.config(text=f"Sentiment: {sentiment} ({score['compound']:.2f})")

# Creating the UI
root = Tk()
root.title("Sentiment Analysis Tool")

# UI Components
Label(root, text="AI Sentiment Analysis Program", font=('Helvetica', 16, 'bold')).pack(pady=10)
Label(root, text="Enter your text below and press the button to analyze its sentiment.").pack(pady=10)

text_entry = Text(root, height=10, width=50)
text_entry.pack(pady=10)

result_label = Label(root, text="Sentiment: ", font=('Helvetica', 14))
result_label.pack(pady=20)

analyze_button = Button(root, text="Analyze Sentiment", command=analyze_sentiment)
analyze_button.pack(pady=20)

root.mainloop()

