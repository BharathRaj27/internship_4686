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

def Fall_prediction(TIME,SL,EEG,BP,HR,CIRCLUATION):

    prediction=model.predict([[TIME,SL,EEG,BP,HR,CIRCLUATION]])
    print(prediction)
    return prediction


def main():
    
    
    # giving a title
    st.title('Fall Prediction Web App')
    
    
    # getting the input data from the user
    
    
    TIME = st.text_input('monitoring time')
    SL=st.text_input("sugar level")
    EEG=st.text_input("EEG monitoring rate")
    BP=st.text_input("Blood pressure")
    HR=st.text_input("Heart beat rate")
    CIRCLUATION=st.text_input("Blood circulation")
    
    
    # code for Prediction
    Result = ''
    
    # creating a button for Prediction
    
    if st.button('predict'):
        Result= Fall_prediction(TIME,SL,EEG,BP,HR,CIRCLUATION)
    st.success('The output is {}'.format(Result))
    if st.button("About"):
       st.text('Lets LEarn')
       st.text("Built with Streamilt")
    
        
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
  
    
  