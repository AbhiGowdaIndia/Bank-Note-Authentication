import pandas as pd
import numpy as np
import pickle
import streamlit as st

pickle_in=open('classifier.pkl','rb')
classifier=pickle.load(pickle_in)
dict={'Variance':[5,6,1,2],
      'Skewness':[-1,0,3,2],
      'Curtosis' :[3,2,5,6],
	  'Entropy':[1,5,3,6]}

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
	st.write('The model is trained on Data extracted from images that were taken from genuine and forged banknote-like specimens. For digitization, an industrial camera usually used for print inspection was used. The final images have 400x 400 pixels. Due to the object lens and distance to the investigated object gray-scale pictures with a resolution of about 660 dpi were gained. Wavelet Transform tool were used to extract features from images.')
	st.text('We can test it in two ways.')
	st.text('1. with dataset containing the attributes varience, skewness,curtosis and entropy')
	st.text('Example :')
	st.dataframe(dict)
	st.text('2. By entering the values for attributes.')
	st.text('Example : 5,1,-2,3')
	
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
	
	if st.button("Predict"):
		try:
			result=predict_note_authentication(variance,skewness,curtosis,entropy)
			st.success('The output is :  {} '.format(result))
			st.info('0 -> Fake Note')
			st.info('1 -> Original Note')
		except:
			st.error('Please enter the values')
	
	st.subheader("Select file to test")
	filename = st.file_uploader("Upload a file", type=("csv"))
	
	if st.button("predict with file"):
		try:
			result=predict_note_file(filename)
			st.success('The output is {}'.format(result))
			st.info('0 -> Fake Note')
			st.info('1 -> Original Note')
		except:
			st.error('Please choose a file')
		
    
if __name__=='__main__':
	main()
