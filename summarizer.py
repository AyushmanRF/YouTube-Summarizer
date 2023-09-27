import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from string import punctuation
from heapq import nlargest

def spacy_summarize(text_content, percent):
    stop_words = list(STOP_WORDS)
    punctuation_items = punctuation + '\n'
    nlp = spacy.load('en_core_web_sm')
    nlp_object = nlp(text_content)
    word_frequencies = {}
    
    for word in nlp_object:
        if word.text.lower() not in stop_words:
            if word.text.lower() not in punctuation_items:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1

    max_frequency = max(word_frequencies.values())
    
    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word] / max_frequency

    sentence_token = [sentence for sentence in nlp_object.sents]
    sentence_scores = {}

    for sent in sentence_token:
        sentence = sent.text.split(" ")
        for word in sentence:
            if word.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word.lower()]
                else:
                    sentence_scores[sent] += word_frequencies[word.lower()]

    select_length = int(len(sentence_token) * (int(percent) / 100))
    summary = nlargest(select_length, sentence_scores, key=sentence_scores.get)
    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)
    return summary

def nltk_summarize(text_content, percent):
    tokens = word_tokenize(text_content)
    stop_words = stopwords.words('english')
    punctuation_items = punctuation + '\n'
    word_frequencies = {}

    for word in tokens:
        if word.lower() not in stop_words:
            if word.lower() not in punctuation_items:
                if word not in word_frequencies.keys():
                    word_frequencies[word] = 1
                else:
                    word_frequencies[word] += 1

    max_frequency = max(word_frequencies.values())

    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word] / max_frequency

    sentence_token = sent_tokenize(text_content)
    sentence_scores = {}

    for sent in sentence_token:
        sentence = sent.split(" ")
        for word in sentence:
            if word.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word.lower()]
                else:
                    sentence_scores[sent] += word_frequencies[word.lower()]

    select_length = int(len(sentence_token) * (int(percent) / 100))
    summary = nlargest(select_length, sentence_scores, key=sentence_scores.get)
    final_summary = [word for word in summary]
    summary = ' '.join(final_summary)
    return summary

def sumy_lsa_summarize(text_content, percent):
    parser = PlaintextParser.from_string(text_content, Tokenizer("english"))
    stemmer = Stemmer('english')
    summarizer = LsaSummarizer(stemmer)
    summarizer.stop_words = get_stop_words('english')
    sentence_token = sent_tokenize(text_content)
    select_length = int(len(sentence_token) * (int(percent) / 100))
    summary = ""

    for sentence in summarizer(parser.document, sentences_count=select_length):
        summary += str(sentence)

    return summary

def sumy_luhn_summarize(text_content, percent):
    parser = PlaintextParser.from_string(text_content, Tokenizer("english"))
    stemmer = Stemmer('english')
    summarizer = LuhnSummarizer(stemmer)
    summarizer.stop_words = get_stop_words('english')
    sentence_token = sent_tokenize(text_content)
    select_length = int(len(sentence_token) * (int(percent) / 100))
    summary = ""

    for sentence in summarizer(parser.document, sentences_count=select_length):
        summary += str(sentence)

    return summary

def sumy_text_rank_summarize(text_content, percent):
    parser = PlaintextParser.from_string(text_content, Tokenizer("english"))
    stemmer = Stemmer('english')
    summarizer = TextRankSummarizer(stemmer)
    summarizer.stop_words = get_stop_words('english')
    sentence_token = sent_tokenize(text_content)
    select_length = int(len(sentence_token) * (int(percent) / 100))
    summary = ""

    for sentence in summarizer(parser.document, sentences_count=select_length):
        summary += str(sentence)

    return summary