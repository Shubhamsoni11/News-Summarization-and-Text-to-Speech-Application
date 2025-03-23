{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "a090b48a-b2aa-46d6-b68b-a00ec0057d1b",
   "metadata": {},
   "outputs": [],
   "source": [
    "from fastapi import FastAPI\n",
    "from fastapi.responses import FileResponse\n",
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "from textblob import TextBlob\n",
    "from gtts import gTTS\n",
    "import os\n",
    "\n",
    "app = FastAPI()\n",
    "\n",
    "# News Scraper\n",
    "def scrape_news(company):\n",
    "    url = f\"https://economictimes.indiatimes.com/topic/{company}\"\n",
    "    headers = {\"User-Agent\": \"Mozilla/5.0\"}\n",
    "    response = requests.get(url, headers=headers)\n",
    "\n",
    "    if response.status_code != 200:\n",
    "        return {\"error\": \"Failed to fetch news\"}\n",
    "\n",
    "    soup = BeautifulSoup(response.text, \"html.parser\")\n",
    "    articles = soup.find_all(\"div\", class_=\"eachStory\")[:10]\n",
    "\n",
    "    results = []\n",
    "    for article in articles:\n",
    "        title = article.find(\"h3\").text.strip() if article.find(\"h3\") else \"No title\"\n",
    "        summary = article.find(\"p\").text.strip() if article.find(\"p\") else \"No summary\"\n",
    "        sentiment = analyze_sentiment(summary)\n",
    "        results.append({\"title\": title, \"summary\": summary, \"sentiment\": sentiment})\n",
    "    \n",
    "    return results\n",
    "\n",
    "# Sentiment Analysis\n",
    "def analyze_sentiment(text):\n",
    "    sentiment_score = TextBlob(text).sentiment.polarity\n",
    "    return \"Positive\" if sentiment_score > 0 else \"Negative\" if sentiment_score < 0 else \"Neutral\"\n",
    "\n",
    "# TTS Function\n",
    "def generate_tts(text):\n",
    "    file_path = \"output.mp3\"\n",
    "    tts = gTTS(text=text, lang=\"hi\")\n",
    "    tts.save(file_path)\n",
    "    return file_path\n",
    "\n",
    "# API Endpoints\n",
    "@app.get(\"/\")\n",
    "def home():\n",
    "    return {\"message\": \"API is running!\"}\n",
    "\n",
    "@app.get(\"/news/{company}\")\n",
    "def get_news(company: str):\n",
    "    return {\"company\": company, \"articles\": scrape_news(company)}\n",
    "\n",
    "@app.get(\"/tts/{text}\")\n",
    "def tts_api(text: str):\n",
    "    file_path = generate_tts(text)\n",
    "    return FileResponse(file_path, media_type=\"audio/mpeg\", filename=\"output.mp3\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eeb6a237-d450-4d6e-bf19-2c2958aa611f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
