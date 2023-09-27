# YouTube-Summarizer
NLP Project

## DESCRIPTION

It is a Python Flask web application that allows users to summarize the transcripts of YouTube videos using various summarization techniques which are mentioned in the description below. The key components of the code:

1. **Flask Web Application** (`app.py`):
   - The application is created using the Flask framework.
   - It has three main routes:
     - `'/'`: This is the home route, which renders a template called `'web.html'`. This is where users can input the URL of the YouTube video they want to summarize.
     - `'/about'`: This route renders a template called `'root.html'`, which could be an "About" page explaining the application.
     - `'/summarize'`: This route handles the video summarization process. It takes parameters from the user, including the video URL, summarization technique choice, and the desired percentage of the summary length.

2. **Video Summarization Logic** (`'/summarize'` route):
   - The `YouTubeTranscriptApi` is used to fetch the transcript of the provided video URL.
   - The chosen summarization technique (e.g., Spacy, NLTK, LSA, Luhn, TextRank) is applied to the transcript text based on the user's choice.
   - The summarized text is then displayed on the `'summary.html'` template.

3. **Summarization Techniques** (`summarizer.py`):
   - The `summarizer.py` module defines five summarization techniques: `spacy_summarize`, `nltk_summarize`, `sumy_lsa_summarize`, `sumy_luhn_summarize`, and `sumy_text_rank_summarize`.
   - These functions use different libraries and algorithms to perform text summarization. They calculate word frequencies, sentence scores, and select the top sentences to form the summary.

4. **Exception Handling**:
   - The code includes exception handling to catch errors that may occur during the summarization process. If an error occurs, it renders an error page with an error message.

5. **Server Initialization**:
   - The Flask application is served using Waitress on host `'0.0.0.0'` and port `4050`. This makes the web application accessible from outside the local machine.

Overall, this project provides a web interface for users to extract summaries from YouTube video transcripts using different summarization techniques. Users can choose their preferred technique and specify the length of the summary as a percentage of the original transcript. If any errors occur during the process, appropriate error messages are displayed to the user.

# Implementation Screenshots

1. **The video (Take the ID from URL)**

![Screenshot (165)](https://github.com/AyushmanRF/YouTube-Summarizer/assets/84237760/cd9ab965-b1bc-4793-8a12-e67ff5b6651e)


2. **Choose the parameters** 

![Screenshot (166)](https://github.com/AyushmanRF/YouTube-Summarizer/assets/84237760/08a45306-a180-4369-a203-156bb9139070)


3. **Result** 

![Screenshot (167)](https://github.com/AyushmanRF/YouTube-Summarizer/assets/84237760/fd038df0-ade8-4bd2-a431-6459fe0ffa24)



