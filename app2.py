# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 19:15:01 2021

@author: siddhardhan
"""

import numpy as np
import pandas as pd
import pickle
import streamlit as st

from PIL import Image

pickel_in=open('model.pkl', 'rb') 
model=pickle.load(pickel_in)

# creating a function for Prediction

def adult_income_prediction(age,workclass,fnlwgt,education,occupation,relationship,race,sex):

    prediction=model.predict([[age,workclass,fnlwgt,education,occupation,relationship,race,sex]])
    print(prediction)
    return prediction


def main():
    
    
    # giving a title
    st.title('adult_income_Prediction Web App')
    
    
    # getting the input data from the user
    
    
    age = st.text_input('age')
    workclass=st.text_input("workclass")
    fnlwgt=st.text_input("fnlwgt")
    education=st.text_input("education")
    occupation = st.text_input('occupation')
    relationship=st.text_input("relationship")
    race=st.text_input("race")
    sex=st.text_input("sex")
    
    
    
    # code for Prediction
    Result = ''
    
    # creating a button for Prediction
    
    if st.button('predict'):
        Result= adult_income_prediction(age,workclass,fnlwgt,education,occupation,relationship,race,sex)
    st.success('The output is {}'.format(Result))
    if st.button("About"):
       st.text('Lets LEarn')
       st.text("Built with Streamilt")
    
        
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
  
    
  