{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "a090b48a-b2aa-46d6-b68b-a00ec0057d1b",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-03-23 21:16:37.471 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-23 21:16:39.482 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\HP\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2025-03-23 21:16:39.484 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-23 21:16:39.486 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-23 21:16:39.488 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-23 21:16:39.490 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-23 21:16:39.492 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-23 21:16:39.494 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-23 21:16:39.496 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-23 21:16:39.497 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-23 21:16:39.500 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-23 21:16:39.501 Session state does not function when running a script without `streamlit run`\n",
      "2025-03-23 21:16:39.505 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-23 21:16:39.505 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-23 21:16:39.510 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-23 21:16:39.515 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-23 21:16:39.516 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-23 21:16:39.518 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-03-23 21:16:39.521 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import requests\n",
    "\n",
    "# FastAPI backend URL\n",
    "FASTAPI_URL = \"http://localhost:8000\"\n",
    "\n",
    "# Streamlit UI\n",
    "st.title(\"Company News Sentiment Analyzer\")\n",
    "st.write(\"Enter a company name to fetch news articles, analyze sentiment, and generate a Hindi TTS summary.\")\n",
    "\n",
    "# Input: Company name\n",
    "company_name = st.text_input(\"Enter a company name\", \"Tesla\")\n",
    "\n",
    "# Button to trigger analysis\n",
    "if st.button(\"Analyze\"):\n",
    "    if company_name:\n",
    "        # Fetch news articles from FastAPI\n",
    "        response = requests.get(f\"{FASTAPI_URL}/news/{company_name}\")\n",
    "        if response.status_code == 200:\n",
    "            articles = response.json()[\"articles\"]\n",
    "            \n",
    "            # Display articles with sentiment and keywords\n",
    "            st.subheader(\"News Articles with Sentiment Analysis\")\n",
    "            for idx, article in enumerate(articles, 1):\n",
    "                st.write(f\"**{idx}. Title:** {article['title']}\")\n",
    "                st.write(f\"**Summary:** {article['summary']}\")\n",
    "                st.write(f\"**Sentiment:** {article['sentiment']}\")\n",
    "                st.write(f\"**Keywords:** {', '.join(article['keywords'])}\")\n",
    "                st.write(\"---\")\n",
    "            \n",
    "            # Generate a summary of all articles\n",
    "            summary = \"\\n\".join([f\"Title: {article['title']}\\nSummary: {article['summary']}\\nSentiment: {article['sentiment']}\\n\" for article in articles])\n",
    "            \n",
    "            # Generate Hindi TTS\n",
    "            tts_response = requests.get(f\"{FASTAPI_URL}/tts/{summary}\")\n",
    "            if tts_response.status_code == 200:\n",
    "                with open(\"output.mp3\", \"wb\") as f:\n",
    "                    f.write(tts_response.content)\n",
    "                st.subheader(\"Hindi TTS Summary\")\n",
    "                st.audio(\"output.mp3\", format=\"audio/mp3\")\n",
    "            else:\n",
    "                st.error(\"Failed to generate TTS.\")\n",
    "        else:\n",
    "            st.error(\"Failed to fetch news articles.\")\n",
    "    else:\n",
    "        st.error(\"Please enter a company name.\")"
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
