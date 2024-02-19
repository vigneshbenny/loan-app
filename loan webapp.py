

import numpy as np
import streamlit as st
import joblib
from PIL import Image
d=joblib.load("C:/Users/LENOVO/Downloads/archive (4)/loanpredict.pkl")

def loan(input_data):
    d=joblib.load("C:/Users/LENOVO/Downloads/archive (4)/loanpredict.pkl")
    input_data=(1,1,3.0,0,0,2,1)
    input_data_as_numpy_array=np.asarray(input_data)
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
    result=d.predict(input_data_reshaped)
    print("___________SEE THE RESULT__________")
    if result==0:
        return "loan is not approved"
    else:
        return "loan is approved"

def main():
    st.title("loan prediction")

    
    Gender=st.text_input("enter Gender")
    Married=st.text_input("enter Married")
    Dependents=st.text_input("number of Dependents")
    Education=st.text_input("number of Education")
    Self_Employed=st.text_input("number of Self_Employed")
    Property_Area=st.text_input("number of Property_Area")
    Credit_History=st.text_input("number of Credit_History")
    
    
    
    loans=''
    
    if st.button("loan result"):
        loans=loan([Gender	,Married,	Dependents	,Education	,Self_Employed	,Property_Area	,Credit_History	])
        st.success(loans)


if __name__ == '__main__':
    main()
    
        