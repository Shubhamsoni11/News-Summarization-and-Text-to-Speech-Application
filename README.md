# News-Summarization-and-Text-to-Speech-Application

Overview
This project is a web-based application that extracts key details from multiple news articles related to a given company, performs sentiment analysis, conducts a comparative analysis, and generates a Hindi text-to-speech (TTS) output. The tool allows users to input a company name and receive a structured sentiment report along with an audio summary.

Features
News Extraction:
Fetches news articles from multiple sources (e.g., Economic Times, MoneyControl).
Extracts titles, summaries, and metadata from at least 10 unique articles.

Sentiment Analysis:
Analyzes the sentiment of each article (Positive, Negative, Neutral) using TextBlob and VADER.

Comparative Analysis:
Compares sentiment distribution across articles.
Identifies common and unique topics using spaCy for keyword extraction.

Text-to-Speech (TTS):
Converts the summarized content into Hindi speech using gTTS.

User Interface:
Provides a simple web-based interface using Streamlit.
Users can input a company name and view the sentiment report.

API Integration:
The backend is built using FastAPI for scraping, sentiment analysis, and TTS generation.
The frontend communicates with the backend via APIs.

Technologies Used
Web Scraping: BeautifulSoup, requests
Sentiment Analysis: TextBlob, nltk.Vader
Keyword Extraction: spaCy
Text-to-Speech: gTTS
Backend: FastAPI
Frontend: Streamlit
Deployment: Hugging Face Spaces, Streamlit Cloud
