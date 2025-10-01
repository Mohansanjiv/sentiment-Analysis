
import streamlit as st
from textblob import TextBlob
import pandas as pd
import emoji
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

st.set_page_config(page_title="Sentiment Analysis Web App", layout="centered")

# @st.cache_data
# def get_text(raw_url):
#     page = urlopen(raw_url)
#     soup = BeautifulSoup(page, 'html.parser')
#     fetched_text = " ".join(map(lambda p: p.text, soup.find_all('p')))
#     return fetched_text
@st.cache_data
def get_text(raw_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0 Safari/537.36"
    }
    response = requests.get(raw_url, headers=headers)
    response.raise_for_status()  

    soup = BeautifulSoup(response.text, "html.parser")
    fetched_text = " ".join(p.text for p in soup.find_all("p"))
    return fetched_text

def main():
    """ Sentiment Analysis Emoji App """
    st.title("🧠 Sentiment Analysis Web App using NLP & ML!")

    menu = ["Text Analysis", "Text Analysis from a Web URL", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Text Analysis":
        raw_text = st.text_area("Enter your Text", "Type here...")
        if st.button("Analyze"):
            blob = TextBlob(raw_text)
            result = blob.sentiment.polarity

            if result > 0.0:
                custom_emoji = emoji.emojize(":smile:", language="alias")
                st.success(f"Positive Sentiment {custom_emoji}")
            elif result < 0.0:
                custom_emoji = emoji.emojize(":disappointed:", language="alias")
                st.error(f"Negative Sentiment {custom_emoji}")
            else:
                custom_emoji = emoji.emojize(":neutral_face:", language="alias")
                st.warning(f"Neutral Sentiment {custom_emoji}")

    elif choice == "Text Analysis from a Web URL":
        st.subheader("Text Analysis from a Web URL")

        raw_url = st.text_input("Enter a URL", "https://en.wikipedia.org/wiki/Natural_language_processing")
        text_preview_length = st.slider("Length to Preview", 50, 500)
        if st.button("Submit"):
            if raw_url:
                result = get_text(raw_url)
                blob = TextBlob(result)

                len_of_full_text = len(result)
                len_of_short_text = round(len(result) / text_preview_length)

                st.success(f"Length of Full text: {len_of_full_text}")
                st.success(f"Length of Short text: {len_of_short_text}")
                st.info(result[:len_of_short_text])

                c_sentences = [str(sent) for sent in blob.sentences]
                c_sentiment = [sent.sentiment.polarity for sent in blob.sentences]

                new_df = pd.DataFrame(zip(c_sentences, c_sentiment), columns=["Sentence", "Sentiment"])
                st.dataframe(new_df)

    else:
        st.subheader("About This App")
        st.info(
            "This is a sentiment analysis web app built using NLP. "
            "You can analyze your own text or fetch text from websites. "
            "We return sentiment values and emojis for a fun touch 😁😂😍."
        )

if __name__ == "__main__":
    main()
