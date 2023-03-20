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

def Abalone_prediction(length,height,whole_weight,sex_I,sex_M):

    prediction=model.predict([[length,height,whole_weight,sex_I,sex_M]])
    print(prediction)
    return prediction


def main():
    
    
    # giving a title
    st.title('Abalone Prediction Web App')
    
    
    # getting the input data from the user
    
    
    length = st.text_input('length')
    height=st.text_input("height")
    whole_weight=st.text_input("whole_weight")
    sex_I=st.text_input("sex_I")
    sex_M=st.text_input("sex_M")
    
    
    
    # code for Prediction
    Result = ''
    
    # creating a button for Prediction
    
    if st.button('predict'):
        Result= Abalone_prediction(length,height,whole_weight,sex_I,sex_M)
    st.success('The output is {}'.format(Result))
    if st.button("About"):
       st.text('Lets LEarn')
       st.text("Built with Streamilt")
    
        
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
  
    
  