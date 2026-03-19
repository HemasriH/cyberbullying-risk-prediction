
import streamlit as st
import pickle
import re

st.set_page_config(
    page_title="Cyberbullying Detection",
    page_icon="🛡️",
    layout="centered"
)

model = pickle.load(open("model.pkl", "rb"))
tfidf = pickle.load(open("tfidf.pkl", "rb"))

def cleantext(text):
    text = str(text).lower()
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r"[^a-z\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^\x00-\x7F]+", "", text)
    return text.strip()

def predict_comment(comment):
    cleaned = cleantext(comment)
    vector = tfidf.transform([cleaned])
    pred = model.predict(vector)[0]
    return pred

st.title("Cyberbullying Comment Predicition")
st.markdown(
"""
This system analyzes online comments and detects **cyberbullying, risky, or safe content**.

Enter a comment below to check whether it is appropriate.
"""
)

st.divider()

comment = st.text_area("Enter your comment", height=150)

if st.button("Check Comment"):

    if comment.strip() == "":
        st.warning("Please enter a comment to analyze.")
    else:
        prediction = predict_comment(comment)

        st.subheader("Result")

        if prediction == "Safe":
            st.success("This comment is **Safe** and allowed.")

        elif prediction == "Cyberbullying":
            st.error("This comment contains **Cyberbullying content** and is blocked.")

        else:
            st.warning("This comment may be **Risky or harmful**. Please rephrase it.")

st.divider()
