import pandas as pd
import numpy as np
import pickle
import streamlit as st

pickle_in=open('classifier.pkl','rb')
classifier=pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def predict_note_authentication(variance,skewness,curtosis,entropy):
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    return prediction
	
def predict_note_file(filename):
	df_test=pd.read_csv(filename)
	prediction=classifier.predict(df_test)
	return str(list(prediction))
	
def main():
	st.title('Bank Auntenticator')
	html_temp="""
    <div style="background-color:tomato;padding:10px;">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App</h2>
    </div>
    """
	st.markdown(html_temp,unsafe_allow_html=True)
	st.subheader("Enter values to test")
	variance = st.text_input("Variance","")
	skewness = st.text_input("skewness","")
	curtosis = st.text_input("curtosis","")
	entropy = st.text_input("entropy","")
	result=""
	
	if st.button("Predict"):
		result=predict_note_authentication(variance,skewness,curtosis,entropy)
		st.success('The output is {}'.format(result))
	
	st.subheader("Select file to test")
	filename = st.file_uploader("Upload a file", type=("csv"))
	
	if st.button("predict with file"):
		result=predict_note_file(filename)
		st.success('The output is {}'.format(result))
    
if __name__=='__main__':
	main()
