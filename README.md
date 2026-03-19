# Early Warning Risk Prediction for Cyberbullying in Social Media
## Introduction
Social media platforms allow easy communication among users. However, they also enable cyberbullying and online harassment which can negatively affect a person's mental health, confidence, and safety.
This project uses Machine Learning and Natural Language Processing techniques to automatically detect harmful comments and provide early warning signals.
## Problem Statement
Most existing cyberbullying detection systems use only binary classification (Cyberbullying / Not Cyberbullying).
This project proposes an improved multi-class prediction system that classifies comments into three categories:
* Safe – Normal conversation
* Risky – Comments that may lead to harmful discussions
* Cyberbullying – Direct abusive comments

This helps in identifying early warning signs before conversations become toxic.
## Dataset Description
Dataset contains social media comments collected from YouTube
* Total Records: 5850
* Features:video_id, comment_text, likes, published_at, reply_count
## Data Preprocessing
The following preprocessing steps were performed:
* Removing missing values
* Converting text to lowercase
* Removing URLs and special characters
* Tokenization
* Lemmatization
* Sentiment analysis
* TF-IDF vectorization
## Feature Extraction
TF-IDF vectorization was used to convert text comments into numerical vectors.
* N-grams (1–3) were used to capture:
* Single words
* Word pairs
* Short phrases

This improves harmful language detection.
## Machine Learning Models Used
* Logistic Regression
* Linear SVC
* Decision Tree
* Random Forest
* Gradient Boosting Classifier
## Best Model Selection
Linear SVC was selected as the best model based on:
* Accuracy: 74%
* Better Precision & Recall
* Lower misclassification of harmful comments
## System Output Examples
### Safe Comment  
Input: "This video is very informative and helpful."  
Prediction: Safe  
System Message: This comment is **Safe** and allowed.

---

### Risky Comment  
Input: "You always talk nonsense, stop commenting."  
Prediction: Risky  
System Message: This comment may be **Risky or harmful**. Please rephrase it.

---

### Cyberbullying Comment  
Input: "You are useless and stupid."  
Prediction: Cyberbullying  
System Message: This comment contains **Cyberbullying content** and is blocked.
###  How to Run the Project
1. Clone the repository  
git clone <your-repo-link>

2. Install required libraries  
pip install -r requirements.txt

3. Run the Streamlit app  
streamlit run app.py
###  Project Structure

- app.py → Streamlit application  
- model.pkl → Trained ML model  
- tfidf.pkl → Vectorizer  
- dataset.csv → Dataset used  
- requirements.txt → Libraries required
### Conclusion
This project helps in early detection of cyberbullying comments by classifying them into Safe, Risky, and Cyberbullying categories using Machine Learning techniques.
### Future Improvements
- Improve accuracy using Deep Learning  
- Real-time deployment in social media platforms  
- Support multiple languages    
