from flask import Flask, render_template, request, jsonify, redirect, url_for
from waitress import serve
from summarizer import (
    spacy_summarize,
    nltk_summarize,
    sumy_lsa_summarize,
    sumy_luhn_summarize,
    sumy_text_rank_summarize
)
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('web.html')

@app.route('/about')
def about():
    return render_template('root.html')

@app.route('/summarize', methods=['GET'])
def summarize():
    video_url = request.args.get('video_url')
    percent = request.args.get('percent')
    choice = request.args.get('choice')

    try:

        transcript = YouTubeTranscriptApi.get_transcript(video_url)


        transcript_text = ' '.join([entry['text'] for entry in transcript])

 
        if choice == 'spacy':
            summary = spacy_summarize(transcript_text, percent)
        elif choice == 'nltk':
            summary = nltk_summarize(transcript_text, percent)
        elif choice == 'lsa':
            summary = sumy_lsa_summarize(transcript_text, percent)
        elif choice == 'luhn':
            summary = sumy_luhn_summarize(transcript_text, percent)
        elif choice == 'text_rank':
            summary = sumy_text_rank_summarize(transcript_text, percent)
        else:
            return render_template('error.html', error_message="Invalid choice parameter")


        return render_template('summary.html', summary=summary)

    except Exception as e:
        return render_template('error.html', error_message=str(e))

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=4050)
