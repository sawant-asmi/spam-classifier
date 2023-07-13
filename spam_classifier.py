import pickle
import streamlit as st 
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from win32com.client import Dispatch

def speak(text):
	speak=Dispatch(("SAPI.SpVoice"))
	speak.Speak(text)


model = pickle.load(open("spam.pkl","rb"))
cv = pickle.load(open("vectorizer.pkl","rb"))


def main():
    st.title("Spam Classifier")
    st.subheader("Build with streamlit & python")
    msg=st.text_input("Enter your text")
    if st.button("Predict"):

        data = [msg]
        vect = cv.transform(data).toarray()
        result=model.predict(vect)
        if result[0]==0:
            st.success("This is Not A Spam Email")
            speak("This is Not A Spam Email")
        else:
            st.error("This is A Spam Email")
            speak("This is A Spam Email")

main()