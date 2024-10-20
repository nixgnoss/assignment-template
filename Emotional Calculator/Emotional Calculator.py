import streamlit as st
from textblob import TextBlob
from nltk.stem.wordnet import WordNetLemmatizer
import nltk
import re

nltk.download('wordnet')


def main():
    # user input
    st.title("Emotional calculator")
    st.subheader("Welcome to use the emotional calculator")
    text = st.text_input(label="Please type your emotion (*include words related to emotion like happy/sad etc.)")

    # clean text
    text = re.sub(r"[^A-Za-z0-9]"," ", text) # keep characters and numbers

    # split text
    text = text.split()
    # recover
    lm = WordNetLemmatizer()
    lemmatized_words = [lm.lemmatize(word) for word in text]
    # reconnected
    text = ' '.join(lemmatized_words)

    # if
    if st.button("Start analyse"):
        blob = TextBlob(text)
        result = blob.sentiment.polarity

        if result > 0.0:
            custom_emoji = ':blush:'
            st.success('happy : {}'.format(custom_emoji))
        elif result < 0.0:
            custom_emoji = ':disappointed:'
            st.warning('sad : {}'.format(custom_emoji))
        else:
            custom_emoji = ':confused:'
            st.info('neutral : {}'.format(custom_emoji))

        st.success('score = {}'.format(result))


if __name__ == "__main__":
    main()
