# 🧠 Sentiment Analysis Web App using Streamlit

This project is a **Sentiment Analysis Web Application** built using **Python, Natural Language Processing (NLP)** and **Streamlit**.  
The application allows users to analyze sentiment from **custom text input** as well as **text extracted from web pages**.

---

## 📌 Project Overview

Sentiment Analysis is a technique used in **Natural Language Processing (NLP)** to determine whether a piece of text expresses a **positive, negative, or neutral** emotion.

This application uses the **TextBlob** library to compute sentiment polarity and presents the result in a **simple and interactive web interface**.

---

## 🚀 Features

- Analyze sentiment from user-entered text
- Extract and analyze text from any public web URL
- Emoji-based sentiment visualization
- Sentence-level sentiment analysis
- Fast performance using Streamlit caching
- Simple and clean UI

---

## 🛠️ Technologies Used

- **Python**
- **Streamlit** – Web framework
- **TextBlob** – NLP sentiment analysis
- **BeautifulSoup** – HTML parsing
- **Requests** – Fetch web content
- **Pandas** – Data processing
- **Emoji** – Visual sentiment representation

---

## 📂 Project Structure

sentiment-analysis-app/  
├── app.py  
├── requirements.txt  
└── README.md  

---

## ⚙️ Installation & Setup

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/sentiment-analysis-app.git
cd sentiment-analysis-app


🧠 Sentiment Analysis Project – Interview Q&A
🔰 Beginner Level Questions
1️⃣ What is Sentiment Analysis?

Answer:
Sentiment Analysis is a Natural Language Processing (NLP) technique used to identify whether a piece of text expresses positive, negative, or neutral emotion.

2️⃣ What problem does your project solve?

Answer:
My project allows users to analyze sentiment from:

Custom user text

Text extracted from web pages

It helps understand public opinion, feedback, or emotional tone quickly using NLP.

3️⃣ Which library did you use for sentiment analysis?

Answer:
I used TextBlob, which provides a simple API for sentiment analysis using polarity and subjectivity scores.

4️⃣ What is polarity in TextBlob?

Answer:
Polarity is a numerical value between -1 and +1:

0 → Positive

< 0 → Negative

= 0 → Neutral

5️⃣ What tech stack did you use?

Answer:

Python

Streamlit

TextBlob

BeautifulSoup

Requests

Pandas

🧪 Intermediate Level Questions
6️⃣ How does your application work internally?

Answer:

User inputs text or URL

Text is processed using TextBlob

Polarity score is calculated

Sentiment is classified

Result is displayed with emojis

7️⃣ How do you extract text from a URL?

Answer:
I use:

requests to fetch HTML content

BeautifulSoup to parse HTML

Extract text from <p> tags

8️⃣ Why did you use Streamlit?

Answer:
Streamlit helps quickly build interactive web apps in Python without frontend complexity. It’s ideal for ML and NLP demos.

9️⃣ What is @st.cache_data and why did you use it?

Answer:
@st.cache_data caches function output so:

Repeated URL fetches are avoided

App performance improves

Network calls are reduced

🔟 What is sentence-level sentiment analysis?

Answer:
Instead of analyzing the whole text at once, the text is split into sentences and each sentence’s sentiment is calculated separately.

🚀 Advanced Level Questions
1️⃣1️⃣ What are the limitations of TextBlob?

Answer:

Rule-based, not deep learning

Not very accurate for sarcasm

Weak on domain-specific language

Limited multi-language support

1️⃣2️⃣ How would you improve accuracy?

Answer:
I would:

Use VADER for social media text

Use BERT / Transformers

Fine-tune a model on domain data

1️⃣3️⃣ How does TextBlob perform sentiment analysis internally?

Answer:
TextBlob uses a lexicon-based approach, where words have predefined sentiment scores, and overall polarity is computed from them.

1️⃣4️⃣ How would you handle large web pages?

Answer:

Limit text length

Chunk text into smaller parts

Use background processing

Add timeout & error handling

1️⃣5️⃣ Is this project scalable?

Answer:
Currently, it’s suitable for small to medium usage.
For scalability:

Move logic to backend APIs

Use async processing

Deploy on cloud with load balancing

🧑‍💻 Coding & Design Questions
1️⃣6️⃣ Why did you use Pandas?

Answer:
To store sentence-wise sentiment results in a structured DataFrame and display them in a table easily.

1️⃣7️⃣ How do you handle invalid URLs?

Answer:
I use response.raise_for_status() to catch HTTP errors and prevent app crashes.

1️⃣8️⃣ How would you add charts?

Answer:
I would use:

Streamlit charts

Matplotlib or Plotly
to visualize sentiment distribution.

1️⃣9️⃣ Can this app support multiple languages?

Answer:
Not currently.
To support multi-language:

Detect language

Use multilingual models like mBERT

2️⃣0️⃣ How would you explain this project to a non-technical person?

Answer:
This app reads text and tells whether the emotion behind it is happy, sad, or neutral, similar to how humans understand feelings in language.

🎯 HR / Project Discussion Questions
2️⃣1️⃣ Why did you choose this project?

Answer:
Because it combines real-world NLP use cases with a simple UI and demonstrates both ML concepts and practical implementation.

2️⃣2️⃣ What did you learn from this project?

Answer:

NLP fundamentals

Sentiment analysis logic

Streamlit development

Web scraping

Performance optimization using caching

2️⃣3️⃣ How is this project useful in real life?

Answer:

Customer feedback analysis

Product reviews

Social media monitoring

Opinion mining

✅ One-Line Project Summary (Interview Gold)

“I built a Streamlit-based NLP application that analyzes sentiment from user text and web content using TextBlob and displays results with emojis and sentence-level breakdown.”
