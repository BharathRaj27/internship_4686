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

def Bank_Loan_prediction(Experience,Income,Family,CD,Account,CreditCard):

    prediction=model.predict([[Experience,Income,Family,CD,Account,CreditCard]])
    print(prediction)
    return prediction


def main():
    
    
    # giving a title
    st.title('bank loan Prediction Web App')
    
    
    # getting the input data from the user
    
    
    Experience= st.text_input('Experience')
    Income=st.text_input("Income")
    Family=st.text_input("Family")
    CD=st.text_input("CD")
    Account=st.text_input("Account")
    CreditCard=st.text_input("CreditCard")
    
    
    # code for Prediction
    Result = ''
    
    # creating a button for Prediction
    
    if st.button('predict'):
        Result= Bank_Loan_prediction(Experience,Income,Family,CD,Account,CreditCard)
    st.success('The output is {}'.format(Result))
    if st.button("About"):
       st.text('Lets LEarn')
       st.text("Built with Streamilt")
    
        
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
  
    
  