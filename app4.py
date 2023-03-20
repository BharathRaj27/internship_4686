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

def chess_prediction(White_King_file,White_King_rank,White_Rook_file,White_Rook_rank,Black_King_file,Black_King_rank):

    prediction=model.predict([[White_King_file,White_King_rank,White_Rook_file,White_Rook_rank,Black_King_file,Black_King_rank]])
    print(prediction)
    return prediction


def main():
    
    
    # giving a title
    st.title('chess Prediction Web App')
    
    
    # getting the input data from the user
    
    
    White_King_rank= st.text_input('White_King_rank')
    White_King_file=st.text_input("White_King_file")
    White_Rook_file=st.text_input("White_Rook_file")
    White_Rook_rank=st.text_input("White_Rook_rank")
    Black_King_file=st.text_input("Black_King_file")
    Black_King_rank=st.text_input("Black_King_rank")
    
    
    # code for Prediction
    Result = ''
    
    # creating a button for Prediction
    
    if st.button('predict'):
        Result= chess_prediction(White_King_file,White_King_rank,White_Rook_file,White_Rook_rank,Black_King_file,Black_King_rank)
    st.success('The output is {}'.format(Result))
    if st.button("About"):
       st.text('Lets LEarn')
       st.text("Built with Streamilt")
    
        
if __name__ == '__main__':
    main()
    
    

    
    
    
    
    
    
    
    
    
    
    
  
    
  